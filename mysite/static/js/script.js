document.body.addEventListener('htmx:confirm', function (event) {
    if (!event.detail.question) {
        return;
    }

    event.preventDefault();

    let question = event.detail.question;

    // 벌크 액션이면 선택 건수를 문구에 넣는다
    const count = document.querySelectorAll('#post-list .post-check:checked').length;
    if (count > 0 && event.detail.elt.closest('#bulk-bar')) {
        question = `${count}건을 ` + question;
    }

    showConfirm(question, function () {
        event.detail.issueRequest();
    });
});
