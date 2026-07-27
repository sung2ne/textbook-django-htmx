let lastToastKey = '';
let lastToastAt = 0;

function showToastOnce(message, level) {
    const now = Date.now();
    const key = level + '|' + message;
    if (key === lastToastKey && now - lastToastAt < 5000) {
        return;
    }
    lastToastKey = key;
    lastToastAt = now;
    showToast(message, level);
}
