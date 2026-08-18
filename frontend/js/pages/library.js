import { api, showToast } from '/js/app.js';

export class LibraryPage {
    async render(container) {
        container.innerHTML = `<div class="page-with-nav loading-page"><div class="spinner"></div></div>`;

        try {
            const parts = await api('/api/chapters/parts');
            this.renderContent(container, parts);
        } catch (err) {
            container.innerHTML = `<div class="page-with-nav"><div class="empty-state"><p>Failed to load chapters</p></div></div>`;
        }
    }

    renderContent(container, parts) {
        container.innerHTML = `
            <div class="page-with-nav">
                <div class="library-header">
                    <h1>Library</h1>
                    <p>23 chapters across 6 parts</p>
                </div>
                ${parts.map(part => this.partGroup(part)).join('')}
                <div style="height: 16px"></div>
            </div>
        `;

        container.querySelectorAll('.chapter-card').forEach(card => {
            card.addEventListener('click', () => {
                history.pushState(null, '', `/read/${card.dataset.slug}`);
                window.app.route();
            });
        });
    }

    partGroup(part) {
        return `
            <div class="part-group">
                <div class="part-title">Part ${part.part_number}: ${part.title}</div>
                <div class="chapter-list">
                    ${part.chapters.map(ch => `
                        <div class="chapter-card" data-slug="${ch.slug}">
                            <div class="chapter-num">${ch.chapter_number}</div>
                            <div class="chapter-info">
                                <div class="chapter-info-title">${ch.title}</div>
                                <div class="chapter-info-meta">${ch.difficulty} &middot; ~${ch.estimated_minutes || 25} min</div>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }
}
