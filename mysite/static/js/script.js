// htmx 요청에 CSRF 토큰을 붙인다.
// base.html의 hx-headers 대신 쿠키에서 읽어 항상 최신 값을 쓴다.
function getCsrfToken() {
    const match = document.cookie.match(/(^|;)\s*csrftoken=([^;]*)/);
    return match ? decodeURIComponent(match[2]) : '';
}

document.body.addEventListener('htmx:configRequest', function (event) {
    const method = (event.detail.verb || '').toUpperCase();
    if (method && method !== 'GET') {
        event.detail.headers['X-CSRFToken'] = getCsrfToken();
    }
});
