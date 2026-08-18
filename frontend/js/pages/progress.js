import { api, showToast } from '/js/app.js';

export class ProgressPage {
    async render(container) {
        container.innerHTML = `<div class="page-with-nav loading-page"><div class="spinner"></div></div>`;

        try {
            const data = await api('/api/progress/book');
            this.renderContent(container, data);
        } catch (err) {
            container.innerHTML = `<div class="page-with-nav"><div class="empty-state"><p>Failed to load progress</p></div></div>`;
        }
    }

    renderContent(container, data) {
        const { chapters_completed, daily_streak, total_reading_time_seconds, chapter_progress } = data;
        const total = chapter_progress.length;
        const pct = total > 0 ? Math.round((chapters_completed / total) * 100) : 0;

        const minutes = Math.round(total_reading_time_seconds / 60);
        const hours = Math.floor(minutes / 60);
        const remainingMin = minutes % 60;
        const timeStr = hours > 0 ? `${hours}h ${remainingMin}m` : `${minutes}m`;

        let parts = {};
        chapter_progress.forEach(ch => {
            const pn = ch.part_number;
            if (!parts[pn]) parts[pn] = { chapters: [] };
            parts[pn].chapters.push(ch);
        });

        container.innerHTML = `
            <div class="page-with-nav">
                <div class="progress-header">
                    <h1>Your Progress</h1>
                    <p>How Cybersecurity Works</p>
                </div>

                <div class="progress-overall">
                    <div class="progress-big-pct">${pct}%</div>
                    <div class="progress-big-label">Book Completed</div>
                    <div class="progress-bar-large">
                        <div class="progress-fill" style="width: ${pct}%"></div>
                    </div>
                    <div class="progress-stats-row">
                        <div class="progress-stat">
                            <div class="progress-stat-value">${chapters_completed}/${total}</div>
                            <div class="progress-stat-label">Chapters Done</div>
                        </div>
                        <div class="progress-stat">
                            <div class="progress-stat-value">${daily_streak}</div>
                            <div class="progress-stat-label">Day Streak</div>
                        </div>
                        <div class="progress-stat">
                            <div class="progress-stat-value">${timeStr}</div>
                            <div class="progress-stat-label">Time Read</div>
                        </div>
                    </div>
                </div>

                ${Object.keys(parts).sort().map(pn => `
                    <div class="part-group">
                        <div class="part-title">Part ${pn}</div>
                        <div class="progress-chapter-list">
                            ${parts[pn].chapters.map(ch => this.chapterItem(ch)).join('')}
                        </div>
                    </div>
                `).join('')}

                <div style="height: 16px"></div>
            </div>
        `;

        container.querySelectorAll('.progress-chapter-item').forEach(el => {
            el.addEventListener('click', () => {
                const slug = el.dataset.slug;
                if (slug) {
                    history.pushState(null, '', `/read/${slug}`);
                    window.app.route();
                }
            });
        });
    }

    chapterItem(ch) {
        let numClass = 'not-started';
        if (ch.quiz_passed) numClass = 'done';
        else if (ch.sections_read > 0) numClass = 'wip';

        let scoreHtml = '';
        if (ch.quiz_passed) {
            scoreHtml = `<span class="progress-chapter-score pass">${ch.quiz_score}/${ch.quiz_total}</span>`;
        } else if (ch.quiz_score !== null) {
            scoreHtml = `<span class="progress-chapter-score fail">${ch.quiz_score}/${ch.quiz_total}</span>`;
        }

        return `
            <div class="progress-chapter-item" data-slug="${ch.slug}">
                <div class="progress-chapter-num ${numClass}">${ch.chapter_number}</div>
                <div class="progress-chapter-info">
                    <div class="progress-chapter-title">${ch.title}</div>
                    <div class="progress-chapter-meta">
                        ${ch.sections_read}/${ch.total_sections} sections
                    </div>
                </div>
                ${scoreHtml}
            </div>
        `;
    }
}
