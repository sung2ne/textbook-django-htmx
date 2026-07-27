// hx-confirm을 모달로 대체한다
document.body.addEventListener('htmx:confirm', function (event) {
    if (!event.detail.question) {
        return;
    }

    event.preventDefault();

    showConfirm(event.detail.question, function () {
        event.detail.issueRequest();
    });
});

function showConfirm(question, onConfirm) {
    const body = document.getElementById('modal-body');
    body.innerHTML = `
        <div class="p-3 border-bottom">
            <h5 class="mb-0">확인</h5>
        </div>
        <div class="p-3">
            <p class="mb-0"></p>
        </div>
        <div class="p-3 border-top text-end">
            <button type="button" class="btn btn-sm btn-danger" data-role="ok">확인</button>
            <button type="button" class="btn btn-sm btn-secondary" data-role="cancel">취소</button>
        </div>
    `;

    // 질문 문구는 textContent로 넣는다 (HTML로 해석되지 않게)
    body.querySelector('p').textContent = question;

    body.querySelector('[data-role="ok"]').addEventListener('click', function () {
        closeModal();
        onConfirm();
    });
    body.querySelector('[data-role="cancel"]').addEventListener('click', closeModal);

    openModal();
}
