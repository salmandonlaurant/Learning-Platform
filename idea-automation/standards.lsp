;;; ==============================================================
;;; IDEA Architecture 24 / 4MCAD - Office Standards Setup
;;; --------------------------------------------------------------
;;; Load with APPLOAD (or via make_batch.py), then type STDSETUP.
;;; Edit the CONFIG section below to match your office standard.
;;; Test on a COPY of a drawing first.
;;; ==============================================================

;;; ------------------ CONFIG - EDIT THIS -----------------------

;; Layers: (name  colour-number  linetype)
;; Colour numbers: 1=Red 2=Yellow 3=Green 4=Cyan 5=Blue
;;                 6=Magenta 7=Black/White 8=Dark grey 256=ByLayer
(setq STD-LAYERS
  (list
    (list "0"               7   "CONTINUOUS")
    (list "A-WALL-EXT"      1   "CONTINUOUS")
    (list "A-WALL-INT"      8   "CONTINUOUS")
    (list "A-DOOR"          2   "CONTINUOUS")
    (list "A-WINDOW"        4   "CONTINUOUS")
    (list "A-SPACE"         5   "CONTINUOUS")
    (list "A-FURNITURE"     3   "CONTINUOUS")
    (list "A-DIM"           6   "CONTINUOUS")
    (list "A-TEXT"          7   "CONTINUOUS")
    (list "A-VENT"        140   "DASHED")
    (list "A-FIRE"          1   "CONTINUOUS")
  )
)

;; Text styles: (name  font-file  height  width-factor  oblique-angle)
;; Font examples: "arial.ttf", "txt.shx", "romans.shx"
(setq STD-TEXTSTYLES
  (list
    (list "STD-NOTE"    "arial.ttf"  2.5  1.0  0.0)
    (list "STD-TITLE"   "arial.ttf"  3.5  1.0  0.0)
    (list "STD-DIMTXT"  "arial.ttf"  2.5  1.0  0.0)
  )
)

;; Arrowhead block used by dimensions and leaders.
;; Try "_CLOSED" (filled), "_OPEN" (open), or "_ARCHTICK" (architectural tick).
;; If the block is not in the drawing, the script falls back to the default.
(setq STD-ARROW "_CLOSED")

;; Dimension variables (mm, 1:1 model space).
;; Change DIMSCALE if she dimensions in paper space / annotated viewports.
(setq STD-DIMVARS
  (list
    (cons "DIMTXSTY"   "STD-DIMTXT")   ; text style used by dimensions
    (cons "DIMTXT"     2.5)            ; dimension text height
    (cons "DIMASZ"     2.5)            ; arrow size
    (cons "DIMBLK"     STD-ARROW)      ; arrow block
    (cons "DIMBLK1"    STD-ARROW)
    (cons "DIMBLK2"    STD-ARROW)
    (cons "DIMLDRBLK"  STD-ARROW)      ; leader arrow
    (cons "DIMEXE"     1.25)           ; extension line beyond dim line
    (cons "DIMEXO"     0.625)          ; extension line offset from object
    (cons "DIMGAP"     0.625)          ; gap around dimension text
    (cons "DIMTAD"     1)              ; text above dimension line (0=centred)
    (cons "DIMDEC"     0)              ; decimal places (mm = 0)
    (cons "DIMTIX"     1)              ; force text between extension lines
    (cons "DIMSOXD"    0)              ; do not suppress outside extension lines
    (cons "DIMZIN"     8)              ; suppress leading/trailing zeros
    (cons "DIMSCALE"   1.0)            ; overall dimension scale
    (cons "DIMCLRD"    256)            ; dimension line colour (ByLayer)
    (cons "DIMCLRE"    256)            ; extension line colour (ByLayer)
    (cons "DIMCLRT"    256)            ; dimension text colour (ByLayer)
    ;; Uncomment these if your IDEA build supports lineweight variables:
    ;; (cons "DIMLWD"   -2)            ; dimension lineweight (ByLayer)
    ;; (cons "DIMLWE"   -2)
  )
)

(setq STD-DIMSTYLE   "STD-DIM")        ; name of the dimension style to create
(setq STD-CURLAYER   "A-WALL-EXT")     ; layer made current after setup
(setq STD-CURTEXT    "STD-NOTE")       ; text style made current after setup

;;; ---------------- END CONFIG ---------------------------------


;;; --- helper: replace/add an association list entry -----------
(defun std-put (rec code val / old)
  (if (setq old (assoc code rec))
    (subst (cons code val) old rec)
    (append rec (list (cons code val)))
  )
)

;;; --- helper: only use a linetype that actually exists --------
(defun std-safe-ltype (name)
  (if (tblsearch "LTYPE" name) name "CONTINUOUS")
)

;;; --- helper: only use an arrow block that actually exists ----
(defun std-safe-arrow (name)
  (if (tblsearch "BLOCK" name) name "")
)

;;; --- ensure a layer exists and has the right settings --------
(defun std-ensure-layer (name colour ltype / rec)
  (setq ltype (std-safe-ltype ltype))
  (if (setq rec (tblsearch "LAYER" name))
    (entmod
      (std-put
        (std-put (std-put rec 62 colour) 6 ltype) 70 0
      )
    )
    (entmake
      (list
        '(0 . "LAYER")
        (cons 2 name)
        '(70 . 0)
        (cons 62 colour)
        (cons 6 ltype)
      )
    )
  )
)

;;; --- ensure a text style exists and has the right settings ---
(defun std-ensure-style (name font height width oblique / rec)
  (if (setq rec (tblsearch "STYLE" name))
    (entmod
      (std-put
        (std-put
          (std-put
            (std-put (std-put (std-put rec 3 font) 40 height) 41 width)
            50 oblique
          )
          42 height
        )
        71 0
      )
    )
    (entmake
      (list
        '(0 . "STYLE")
        (cons 2 name)
        '(70 . 0)
        (cons 40 height)
        (cons 41 width)
        (cons 50 oblique)
        '(71 . 0)
        (cons 42 height)
        (cons 3 font)
        (cons 4 "")
      )
    )
  )
)

;;; --- set dimension variables, guarding arrow block names -----
(defun std-set-vars (lst / name val)
  (foreach item lst
    (setq name (car item)
          val  (cdr item)
    )
    (if (member name '("DIMBLK" "DIMBLK1" "DIMBLK2" "DIMLDRBLK"))
      (setq val (std-safe-arrow val))
    )
    (setvar name val)
  )
)

;;; ==============================================================
;;; COMMAND: STDSETUP - apply all standards to the current drawing
;;; ==============================================================
(defun c:STDSETUP (/ item)
  (princ "\nIDEA Architecture - applying office standards...")

  (foreach item STD-LAYERS
    (std-ensure-layer (car item) (cadr item) (caddr item))
  )

  (foreach item STD-TEXTSTYLES
    (std-ensure-style
      (car item) (cadr item) (caddr item) (cadddr item)
      (car (cddddr item))
    )
  )

  (std-set-vars STD-DIMVARS)

  ;; Save the current settings as the office dimension style.
  (if (tblsearch "DIMSTYLE" STD-DIMSTYLE)
    (command "_.-DIMSTYLE" "_S" STD-DIMSTYLE "_Y")
    (command "_.-DIMSTYLE" "_S" STD-DIMSTYLE)
  )
  (command "_.-DIMSTYLE" "_R" STD-DIMSTYLE)

  (setvar "CLAYER"   STD-CURLAYER)
  (setvar "TEXTSTYLE" STD-CURTEXT)

  (princ (strcat "\nDone.  Dimstyle: " STD-DIMSTYLE
                 " | Current layer: " STD-CURLAYER))
  (princ)
)

;;; ==============================================================
;;; COMMAND: STDLIST - print the settings that will be applied
;;; ==============================================================
(defun c:STDLIST (/ item)
  (princ "\n--- Office standard settings ---")
  (princ "\nLayers:")
  (foreach item STD-LAYERS
    (princ (strcat "\n  " (car item) "  colour=" (itoa (cadr item))
                   "  linetype=" (caddr item)))
  )
  (princ "\nText styles:")
  (foreach item STD-TEXTSTYLES
    (princ (strcat "\n  " (car item) "  font=" (cadr item)
                   "  height=" (rtos (caddr item) 2 2)))
  )
  (princ (strcat "\nDimension style: " STD-DIMSTYLE
                 " | Arrow: " STD-ARROW))
  (princ "\n")
  (princ)
)

(princ "\nLoaded: IDEA standards.  Type STDSETUP to apply, STDLIST to review.")
(princ)
