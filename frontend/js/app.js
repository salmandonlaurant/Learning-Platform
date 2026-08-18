import { AuthPage } from '/js/pages/auth.js';
import { HomePage } from '/js/pages/home.js';
import { LibraryPage } from '/js/pages/library.js';
import { ReaderPage } from '/js/pages/reader.js';
import { QuizPage } from '/js/pages/quiz.js';
import { ProgressPage } from '/js/pages/progress.js';

const API = '';

class App {
    constructor() {
        this.token = localStorage.getItem('token');
        this.user = JSON.parse(localStorage.getItem('user') || 'null');
        this.currentPage = null;

        this.init();
    }

    init() {
        window.addEventListener('popstate', () => this.route());

        document.querySelectorAll('#bottom-nav .nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const href = link.getAttribute('href');
                history.pushState(null, '', href);
                this.route();
            });
        });

        this.route();
    }

    route() {
        const path = window.location.pathname;

        if (!this.token && path !== '/login' && path !== '/register') {
            history.replaceState(null, '', '/login');
            this.renderAuth();
            return;
        }

        if (this.token && (path === '/login' || path === '/register' || path === '/')) {
            history.replaceState(null, '', '/home');
        }

        const nav = document.getElementById('bottom-nav');
        if (this.token) {
            nav.classList.remove('hidden');
        } else {
            nav.classList.add('hidden');
        }

        if (this.token) {
            const basePage = path === '/home' || path === '/library' || path === '/progress'
                ? path.slice(1)
                : 'home';
            document.querySelectorAll('#bottom-nav .nav-link').forEach(l => {
                l.classList.toggle('active', l.getAttribute('data-page') === basePage);
            });
        }

        if (this.currentPage && typeof this.currentPage.destroy === 'function') {
            this.currentPage.destroy();
        }

        if (path === '/login' || path === '/register') {
            nav.classList.add('hidden');
            const mode = path === '/register' ? 'register' : 'login';
            this.currentPage = new AuthPage(mode);
        } else if (path === '/home') {
            this.currentPage = new HomePage();
        } else if (path === '/library') {
            this.currentPage = new LibraryPage();
        } else if (path === '/progress') {
            this.currentPage = new ProgressPage();
        } else if (path.startsWith('/read/')) {
            const slug = path.replace('/read/', '');
            this.currentPage = new ReaderPage(slug);
        } else if (path.startsWith('/quiz/')) {
            const slug = path.replace('/quiz/', '');
            this.currentPage = new QuizPage(slug);
        } else {
            this.currentPage = new HomePage();
        }

        this.currentPage.render(document.getElementById('main-content'));
        window.scrollTo(0, 0);
    }

    renderAuth() {
        document.getElementById('bottom-nav').classList.add('hidden');
        const path = window.location.pathname;
        const mode = path === '/register' ? 'register' : 'login';
        this.currentPage = new AuthPage(mode);
        this.currentPage.render(document.getElementById('main-content'));
    }

    login(token, user) {
        this.token = token;
        this.user = user;
        localStorage.setItem('token', token);
        localStorage.setItem('user', JSON.stringify(user));
        history.pushState(null, '', '/home');
        this.route();
    }

    logout() {
        this.token = null;
        this.user = null;
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        history.pushState(null, '', '/login');
        this.route();
    }
}

export async function api(path, options = {}) {
    const token = localStorage.getItem('token');
    const headers = { 'Content-Type': 'application/json', ...options.headers };
    if (token) headers['Authorization'] = `Bearer ${token}`;

    const res = await fetch(`${API}${path}`, { ...options, headers });

    if (res.status === 401) {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        window.location.href = '/login';
        throw new Error('Unauthorized');
    }

    if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: 'Request failed' }));
        throw new Error(err.detail || 'Request failed');
    }

    return res.json();
}

export function showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    container.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

export function renderMarkdown(text) {
    if (!text) return '';
    let html = text
        .replace(/```(\w*)\n([\s\S]*?)```/g, '<pre><code>$2</code></pre>')
        .replace(/`([^`]+)`/g, '<code>$1</code>')
        .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
        .replace(/\*([^*]+)\*/g, '<em>$1</em>')
        .replace(/^> (.+)$/gm, '<blockquote>$1</blockquote>')
        .replace(/^- (.+)$/gm, '<li>$1</li>')
        .replace(/^(\d+)\. (.+)$/gm, '<li>$2</li>')
        .replace(/\n\n/g, '<br><br>')
        .replace(/\n/g, '<br>');

    html = html.replace(/(<li>.*<\/li>)/gs, '<ul>$1</ul>');
    html = html.replace(/<\/ul><ul>/g, '');

    return html;
}

window.app = new App();
