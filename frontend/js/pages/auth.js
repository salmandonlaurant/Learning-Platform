import { api, showToast } from '/js/app.js';

export class AuthPage {
    constructor(mode = 'login') {
        this.mode = mode;
    }

    render(container) {
        const isLogin = this.mode === 'login';
        container.innerHTML = `
            <div class="auth-page">
                <div class="auth-container">
                    <div class="auth-brand">
                        <div class="auth-brand-icon">&#9881;</div>
                        <div class="auth-brand-name">CyberSec Tutor</div>
                    </div>
                    <div class="auth-card">
                        <h1 class="auth-title">${isLogin ? 'Welcome Back' : 'Create Account'}</h1>
                        <p class="auth-subtitle">${isLogin ? 'Continue your cybersecurity learning journey' : 'Start your cybersecurity education'}</p>
                        <div id="auth-error"></div>
                        <form class="auth-form" id="auth-form">
                            ${!isLogin ? '<div class="form-group"><label class="form-label">Username</label><input class="input" name="username" placeholder="Choose a username" required minlength="3"></div>' : ''}
                            <div class="form-group">
                                <label class="form-label">Email</label>
                                <input class="input" name="email" type="email" placeholder="you@example.com" required>
                            </div>
                            <div class="form-group">
                                <label class="form-label">Password</label>
                                <input class="input" name="password" type="password" placeholder="Enter your password" required minlength="6">
                            </div>
                            <button class="btn btn-primary btn-lg" type="submit" id="auth-submit">${isLogin ? 'Sign In' : 'Create Account'}</button>
                        </form>
                        <div class="auth-footer">
                            ${isLogin
                                ? 'Don\'t have an account? <a href="/register" id="switch-auth">Sign up</a>'
                                : 'Already have an account? <a href="/login" id="switch-auth">Sign in</a>'
                            }
                        </div>
                    </div>
                </div>
            </div>
        `;

        document.getElementById('switch-auth')?.addEventListener('click', (e) => {
            e.preventDefault();
            history.pushState(null, '', isLogin ? '/register' : '/login');
            const newMode = isLogin ? 'register' : 'login';
            new AuthPage(newMode).render(container);
        });

        document.getElementById('auth-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const form = e.target;
            const submitBtn = document.getElementById('auth-submit');
            const errorDiv = document.getElementById('auth-error');

            submitBtn.disabled = true;
            submitBtn.textContent = isLogin ? 'Signing in...' : 'Creating account...';
            errorDiv.innerHTML = '';

            const data = Object.fromEntries(new FormData(form));

            try {
                const endpoint = isLogin ? '/api/auth/login' : '/api/auth/register';
                const result = await api(endpoint, {
                    method: 'POST',
                    body: JSON.stringify(data),
                });

                window.app.login(result.access_token, result.user);
                showToast(`Welcome${isLogin ? ' back' : ''}, ${result.user.username}!`, 'success');
            } catch (err) {
                errorDiv.innerHTML = `<div class="auth-error">${err.message}</div>`;
            } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = isLogin ? 'Sign In' : 'Create Account';
            }
        });
    }
}
