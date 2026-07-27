// 모달을 연 요소를 기억했다가 닫을 때 포커스를 되돌린다
let modalOpener = null;

document.body.addEventListener('htmx:beforeRequest', function (event) {
    const elt = event.detail.elt;
    if (elt && elt.getAttribute && elt.getAttribute('hx-target') === '#modal-body') {
        modalOpener = elt;
    }
});
