// 응답 상태 코드를 읽는다.
// htmx 4.0에서 detail 구조가 바뀌므로 여기 한 곳만 고치면 된다.
function responseStatus(event) {
    const d = event.detail || {};
    if (d.xhr && typeof d.xhr.status === 'number') return d.xhr.status;      // htmx 2.x
    if (d.response && typeof d.response.status === 'number') return d.response.status;  // htmx 4.x
    return 0;
}
