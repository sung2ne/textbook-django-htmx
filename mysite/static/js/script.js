// 클라이언트에서 발생한 요청 실패를 서버에 알린다
function reportClientError(kind, detail) {
    // 보고 자체가 실패해도 무시한다
    fetch('/client-errors/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({
            kind: kind,
            path: location.pathname,
            detail: detail,
        }),
        keepalive: true,
    }).catch(() => {});
}

document.body.addEventListener('htmx:sendError', function (event) {
    reportClientError('sendError', (event.detail.requestConfig || {}).path);
});

document.body.addEventListener('htmx:timeout', function (event) {
    reportClientError('timeout', (event.detail.requestConfig || {}).path);
});
