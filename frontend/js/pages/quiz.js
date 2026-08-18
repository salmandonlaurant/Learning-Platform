import { api, showToast, renderMarkdown } from '/js/app.js';

export class QuizPage {
    constructor(slug) {
        this.slug = slug;
        this.questions = [];
        this.answers = {};
        this.submitted = false;
        this.results = null;
    }

    async render(container) {
        container.innerHTML = `<div class="page-with-nav loading-page"><div class="spinner"></div></div>`;

        try {
            const data = await api(`/api/chapters/${this.slug}/quiz`);
            if (data.error) {
                container.innerHTML = `<div class="page-with-nav"><div class="empty-state"><p>${data.error}</p></div></div>`;
                return;
            }
            this.chapterId = data.chapter_id;
            this.chapterTitle = data.chapter_title;
            this.questions = data.questions;
            this.renderContent(container);
        } catch (err) {
            container.innerHTML = `<div class="page-with-nav"><div class="empty-state"><p>Quiz not found</p></div></div>`;
        }
    }

    renderContent(container) {
        if (this.submitted && this.results) {
            this.renderResults(container);
            return;
        }

        const answered = Object.keys(this.answers).length;
        const total = this.questions.length;
        const pct = total > 0 ? (answered / total) * 100 : 0;

        container.innerHTML = `
            <div class="page-with-nav">
                <div class="top-bar">
                    <button class="top-bar-back" id="quiz-back">&larr; Back</button>
                    <span class="top-bar-title">${this.chapterTitle}</span>
                    <span></span>
                </div>
                <div class="quiz-container">
                    <div class="quiz-header">
                        <h1>Chapter Quiz</h1>
                        <p>Answer all questions &middot; 60% to pass</p>
                        <div class="quiz-progress-bar">
                            <div class="quiz-progress-fill" style="width: ${pct}%"></div>
                        </div>
                    </div>

                    ${this.questions.map((q, i) => `
                        <div class="quiz-question-card">
                            <div class="quiz-question-num">Question ${q.question_number} of ${total}</div>
                            <div class="quiz-question-text">${q.question_text}</div>
                            ${q.options.map((opt, oi) => `
                                <div class="quiz-option ${this.answers[i] === oi ? 'selected' : ''}"
                                     data-question="${i}" data-option="${oi}">
                                    <div class="quiz-option-marker">${String.fromCharCode(65 + oi)}</div>
                                    <span>${opt}</span>
                                </div>
                            `).join('')}
                        </div>
                    `).join('')}

                    <div class="quiz-submit-area">
                        <button class="btn btn-primary btn-lg" id="quiz-submit-btn"
                            ${answered < total ? 'disabled' : ''}
                            style="width: 100%">
                            ${answered < total ? `Answer all questions (${answered}/${total})` : 'Submit Quiz'}
                        </button>
                    </div>
                </div>
            </div>
        `;

        document.getElementById('quiz-back').addEventListener('click', () => {
            history.pushState(null, '', `/read/${this.slug}`);
            window.app.route();
        });

        container.querySelectorAll('.quiz-option').forEach(el => {
            el.addEventListener('click', () => {
                if (this.submitted) return;
                const qi = parseInt(el.dataset.question);
                const oi = parseInt(el.dataset.option);
                this.answers[qi] = oi;

                container.querySelectorAll(`[data-question="${qi}"]`).forEach(o => {
                    o.classList.toggle('selected', parseInt(o.dataset.option) === oi);
                });

                const answeredCount = Object.keys(this.answers).length;
                const btn = document.getElementById('quiz-submit-btn');
                if (answeredCount >= this.questions.length) {
                    btn.disabled = false;
                    btn.textContent = 'Submit Quiz';
                } else {
                    btn.textContent = `Answer all questions (${answeredCount}/${this.questions.length})`;
                }
            });
        });

        document.getElementById('quiz-submit-btn').addEventListener('click', () => this.submitQuiz(container));
    }

    async submitQuiz(container) {
        const btn = document.getElementById('quiz-submit-btn');
        btn.disabled = true;
        btn.textContent = 'Submitting...';

        try {
            const answerList = this.questions.map((_, i) => this.answers[i] ?? -1);
            this.results = await api('/api/progress/quiz-submit', {
                method: 'POST',
                body: JSON.stringify({
                    chapter_id: this.chapterId,
                    answers: answerList,
                }),
            });
            this.submitted = true;
            this.renderResults(container);
        } catch (err) {
            showToast('Failed to submit quiz', 'error');
            btn.disabled = false;
            btn.textContent = 'Submit Quiz';
        }
    }

    renderResults(container) {
        const r = this.results;
        const scorePct = r.score_percentage;

        container.innerHTML = `
            <div class="page-with-nav">
                <div class="top-bar">
                    <button class="top-bar-back" id="result-back">&larr; Back</button>
                    <span class="top-bar-title">${this.chapterTitle}</span>
                    <span></span>
                </div>
                <div class="quiz-container">
                    <div class="quiz-result-card">
                        <div class="quiz-result-icon">${r.passed ? '&#127881;' : '&#128170;'}</div>
                        <div class="quiz-result-score ${r.passed ? 'quiz-result-pass' : 'quiz-result-fail'}">
                            ${r.score}/${r.total}
                        </div>
                        <div class="quiz-result-label">
                            ${r.passed ? 'Congratulations! You passed!' : 'Keep studying — you need 60% to pass'}
                        </div>
                        <button class="btn btn-primary btn-lg" id="retry-btn" style="margin-right: 10px">
                            Retry Quiz
                        </button>
                        <button class="btn btn-outline btn-lg" id="back-to-chapter-btn">
                            Back to Chapter
                        </button>
                    </div>

                    <div style="margin-top: 28px">
                        <h3 style="margin-bottom: 16px; font-size: 18px;">Review Answers</h3>
                        ${r.results.map((res, i) => `
                            <div class="quiz-question-card" style="margin-bottom: 12px">
                                <div class="quiz-question-num" style="color: ${res.is_correct ? 'var(--success)' : 'var(--danger)'}">
                                    ${res.is_correct ? '&#10003; Correct' : '&#10007; Incorrect'}
                                </div>
                                <div class="quiz-question-text" style="font-size: 16px">${res.question_text}</div>
                                <div class="quiz-explanation">${res.explanation}</div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        `;

        document.getElementById('result-back').addEventListener('click', () => {
            history.pushState(null, '', `/read/${this.slug}`);
            window.app.route();
        });

        document.getElementById('retry-btn').addEventListener('click', () => {
            this.answers = {};
            this.submitted = false;
            this.results = null;
            this.renderContent(container);
        });

        document.getElementById('back-to-chapter-btn').addEventListener('click', () => {
            history.pushState(null, '', `/read/${this.slug}`);
            window.app.route();
        });
    }
}
