import { api, showToast, renderMarkdown } from '/js/app.js';

export class ReaderPage {
    constructor(slug) {
        this.slug = slug;
        this.readingStartTime = null;
        this.timeInterval = null;
    }

    async render(container) {
        container.innerHTML = `<div class="page-with-nav loading-page"><div class="spinner"></div></div>`;

        try {
            const chapter = await api(`/api/chapters/${this.slug}`);
            if (chapter.error) {
                container.innerHTML = `<div class="page-with-nav"><div class="empty-state"><p>${chapter.error}</p></div></div>`;
                return;
            }
            this.chapter = chapter;
            this.renderContent(container);
            this.startReadingTimer();
        } catch (err) {
            container.innerHTML = `<div class="page-with-nav"><div class="empty-state"><p>Chapter not found</p></div></div>`;
        }
    }

    renderContent(container) {
        const ch = this.chapter;
        const readSections = new Set(ch.reading_progress.sections_read || []);

        container.innerHTML = `
            <div class="page-with-nav">
                <div class="top-bar">
                    <button class="top-bar-back" id="back-btn">&larr; Library</button>
                    <span class="top-bar-title">Ch. ${ch.chapter_number}</span>
                    <span></span>
                </div>
                <div class="reader-content">
                    <div class="reader-chapter-badge">${ch.category}</div>
                    <h1 class="reader-title">${ch.title}</h1>
                    <p class="reader-subtitle">${ch.subtitle}</p>
                    <div class="reader-meta">
                        <span>${ch.difficulty}</span>
                        <span>~${ch.estimated_minutes || 25} min read</span>
                        <span>${ch.quiz_questions} quiz questions</span>
                    </div>

                    ${ch.intro_hook ? `<div class="reader-hook">${renderMarkdown(ch.intro_hook)}</div>` : ''}

                    ${ch.sections.map(sec => `
                        <div class="reader-section" data-section="${sec.section_number}">
                            <h2 class="reader-section-title">${sec.section_number}. ${sec.title}</h2>
                            <div class="reader-body">${renderMarkdown(sec.content)}</div>
                            <div class="section-check ${readSections.has(sec.section_number) ? 'read' : ''}"
                                 data-section="${sec.section_number}">
                                <div class="section-check-mark">${readSections.has(sec.section_number) ? '&#10003;' : ''}</div>
                                <span class="section-check-text">${readSections.has(sec.section_number) ? 'Section read' : 'Mark as read'}</span>
                            </div>
                        </div>
                    `).join('')}

                    ${ch.key_takeaways && ch.key_takeaways.length > 0 ? `
                        <div class="takeaways-box">
                            <div class="takeaways-title">&#128161; Key Takeaways</div>
                            ${ch.key_takeaways.map(t => `
                                <div class="takeaway-item">
                                    <span class="takeaway-bullet">&bull;</span>
                                    <span>${t}</span>
                                </div>
                            `).join('')}
                        </div>
                    ` : ''}

                    ${ch.vocabulary && ch.vocabulary.length > 0 ? `
                        <div class="vocab-box">
                            <div class="takeaways-title">&#128214; Vocabulary</div>
                            ${ch.vocabulary.map(v => `
                                <div class="vocab-item">
                                    <div class="vocab-term">${v.term}</div>
                                    <div class="vocab-def">${v.definition}</div>
                                </div>
                            `).join('')}
                        </div>
                    ` : ''}

                    <div class="quiz-submit-area">
                        <button class="btn btn-primary btn-lg" id="take-quiz-btn" style="width: 100%">
                            Take End-of-Chapter Quiz
                        </button>
                    </div>
                </div>
            </div>
        `;

        document.getElementById('back-btn').addEventListener('click', () => {
            history.pushState(null, '', '/library');
            window.app.route();
        });

        document.getElementById('take-quiz-btn').addEventListener('click', () => {
            history.pushState(null, '', `/quiz/${this.slug}`);
            window.app.route();
        });

        container.querySelectorAll('.section-check').forEach(el => {
            el.addEventListener('click', () => this.toggleSection(el));
        });
    }

    async toggleSection(el) {
        const sectionNum = parseInt(el.dataset.section);
        const isRead = el.classList.contains('read');

        if (isRead) return;

        try {
            await api('/api/progress/section-read', {
                method: 'POST',
                body: JSON.stringify({
                    chapter_id: this.chapter.id,
                    section_number: sectionNum,
                }),
            });

            el.classList.add('read');
            el.querySelector('.section-check-mark').innerHTML = '&#10003;';
            el.querySelector('.section-check-text').textContent = 'Section read';
        } catch (err) {
            showToast('Failed to save progress', 'error');
        }
    }

    startReadingTimer() {
        this.readingStartTime = Date.now();
        this.timeInterval = setInterval(() => {
            const seconds = Math.floor((Date.now() - this.readingStartTime) / 1000);
            if (seconds > 0 && seconds % 30 === 0) {
                api('/api/progress/reading-time', {
                    method: 'POST',
                    body: JSON.stringify({ seconds: 30 }),
                }).catch(() => {});
                this.readingStartTime = Date.now();
            }
        }, 1000);
    }

    destroy() {
        if (this.timeInterval) {
            clearInterval(this.timeInterval);
            const elapsed = Math.floor((Date.now() - this.readingStartTime) / 1000);
            if (elapsed > 0) {
                api('/api/progress/reading-time', {
                    method: 'POST',
                    body: JSON.stringify({ seconds: elapsed }),
                }).catch(() => {});
            }
        }
    }
}
