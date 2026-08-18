import { api, showToast, renderMarkdown } from '/js/app.js';

export class HomePage {
    async render(container) {
        container.innerHTML = `<div class="page-with-nav loading-page"><div class="spinner"></div></div>`;

        try {
            const data = await api('/api/dashboard');
            this.renderContent(container, data);
        } catch (err) {
            container.innerHTML = `<div class="page-with-nav"><div class="empty-state"><p>Failed to load dashboard</p></div></div>`;
        }
    }

    renderContent(container, data) {
        const { progress, current_chapter, recent_chapters, user, total_chapters } = data;
        const pct = progress.percentage;

        container.innerHTML = `
            <div class="page-with-nav">
                <div class="home-hero">
                    <h1>How Cybersecurity Works</h1>
                    <p>Welcome back, ${user.username}</p>
                </div>

                ${current_chapter ? `
                    <div class="continue-card" id="continue-btn" data-slug="${current_chapter.slug}">
                        <div class="continue-label">Continue Reading</div>
                        <div class="continue-title">${current_chapter.title}</div>
                        <div class="continue-meta">Chapter ${current_chapter.chapter_number} &middot; ${current_chapter.category}</div>
                        <div class="continue-progress">
                            <div class="continue-progress-fill" style="width: ${current_chapter.reading_percentage}%"></div>
                        </div>
                    </div>
                ` : `
                    <div class="continue-card" id="continue-btn" data-slug="${recent_chapters[0]?.slug || 'how-data-travels-the-internet'}">
                        <div class="continue-label">Start Reading</div>
                        <div class="continue-title">${recent_chapters[0]?.title || 'How Data Travels the Internet'}</div>
                        <div class="continue-meta">Chapter 1 &middot; Foundations</div>
                    </div>
                `}

                <div class="stats-row">
                    <div class="stat-mini">
                        <div class="stat-mini-value">${progress.completed_chapters}/${total_chapters}</div>
                        <div class="stat-mini-label">Chapters Done</div>
                    </div>
                    <div class="stat-mini">
                        <div class="stat-mini-value">${progress.daily_streak}</div>
                        <div class="stat-mini-label">Day Streak</div>
                    </div>
                    <div class="stat-mini">
                        <div class="stat-mini-value">${Math.round(progress.total_reading_time_seconds / 60)}m</div>
                        <div class="stat-mini-label">Time Read</div>
                    </div>
                </div>

                <div class="section-header">
                    <span class="section-title">Recent Chapters</span>
                </div>
                <div class="chapter-list" id="chapter-list">
                    ${recent_chapters.map(ch => this.chapterCard(ch)).join('')}
                </div>
                <div style="height: 16px"></div>
            </div>
        `;

        document.getElementById('continue-btn')?.addEventListener('click', () => {
            const slug = document.getElementById('continue-btn').dataset.slug;
            history.pushState(null, '', `/read/${slug}`);
            window.app.route();
        });

        container.querySelectorAll('.chapter-card').forEach(card => {
            card.addEventListener('click', () => {
                history.pushState(null, '', `/read/${card.dataset.slug}`);
                window.app.route();
            });
        });
    }

    chapterCard(ch) {
        const numClass = ch.quiz_passed ? 'completed' : ch.sections_read > 0 ? 'in-progress' : '';
        let statusHtml = '';
        if (ch.quiz_passed) {
            statusHtml = `<span class="chapter-status done">Done</span>`;
        } else if (ch.sections_read > 0) {
            statusHtml = `<span class="chapter-status reading">Reading</span>`;
        }

        return `
            <div class="chapter-card" data-slug="${ch.slug}">
                <div class="chapter-num ${numClass}">${ch.chapter_number}</div>
                <div class="chapter-info">
                    <div class="chapter-info-title">${ch.title}</div>
                    <div class="chapter-info-meta">${ch.difficulty} &middot; ~${ch.estimated_minutes || 25} min</div>
                </div>
                ${statusHtml}
            </div>
        `;
    }
}
