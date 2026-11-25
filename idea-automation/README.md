# IDEA Architecture 24 — one-click office standards

Two small tools:

- `standards.lsp` — applies your office standard inside IDEA Architecture 24 / 4MCAD.
- `make_batch.py` — generates a `.scr` file to run it on a whole folder of DWGs.

## 1. Set up the standard once

Open `standards.lsp` in Notepad and edit the **CONFIG** section at the top:

| Section | What to change |
|---|---|
| `STD-LAYERS` | Layer names, ACI colour numbers, linetypes |
| `STD-TEXTSTYLES` | Font file (e.g. `arial.ttf`), text height, width factor |
| `STD-ARROW` | `_CLOSED`, `_OPEN`, or `_ARCHTICK` |
| `STD-DIMVARS` | Text height, arrow size, extension offsets, decimal places, lineweight |
| `STD-DIMSTYLE` | Name of the dimension style the script creates |
| `STD-CURLAYER` / `STD-CURTEXT` | What becomes current after setup |

Values are in **millimetres at 1:1** (model space). If she dimensions inside scaled viewports, change `DIMSCALE`.

## 2. Apply to the current drawing

1. In IDEA Architecture 24, type `APPLOAD` and load `standards.lsp`.
   - Tip: add it to **Startup Suite** so it loads automatically every time.
2. Type `STDSETUP` and press Enter.
3. Type `STDLIST` any time to review the configured settings.

It will:
- create or update every layer (colour + linetype),
- create or update the text styles,
- set dimension variables and save them as the named dimension style,
- make the standard layer and text style current.

> **Test on a copy of a drawing first.** Layers that already exist are updated in place; objects on them keep their layer assignment but inherit the new colour/linetype.

## 3. Apply to a whole project folder

```powershell
python make_batch.py "C:\Projects\Job123" --backup "C:\Backups\Job123"
```

Options:
- `--recursive` — include subfolders.
- `--lisp "path\to\standards.lsp"` — use a different LISP file.
- `--out "path\to\my.scr"` — choose the script filename.

Then in IDEA:
1. Type `SCRIPT`.
2. Select the generated `batch_standards.scr`.
3. Let it run — it opens each DWG, applies the standards, saves and closes it.

## Troubleshooting

| Problem | Fix |
|---|---|
| `STDSETUP` unknown command | The LISP did not load. Run `APPLOAD` again, or check the file path. |
| Linetype looks wrong | The linetype is not in the drawing — the script falls back to `CONTINUOUS`. Load the linetype file first, or use `CONTINUOUS` in the config. |
| Arrows look wrong | The arrow block was missing, so the default was used. Check the `STD-ARROW` block exists in the drawing. |
| Prompt appears during batch run | Make sure no drawing has unsaved changes before running the script. |
| IDEA-specific BIM objects do not respond | These scripts handle standard DWG entities (layers, text styles, dimensions). Native IDEA BIM objects may need IDEA's .NET API — we can add that next. |

## Next automations to build

1. Auto-dimension a selected room with the standard style.
2. Space detection + room labels + Excel room schedule.
3. Furniture layout rules engine (room use → block placement).
4. Wall-type assistant and ventilation schedule.
5. Drawing QA/QC auditor.
