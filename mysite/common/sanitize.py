import nh3

# 게시글 본문에서 허용할 태그
ALLOWED_TAGS = {
    'p', 'br', 'strong', 'em', 'u', 's',
    'ul', 'ol', 'li', 'blockquote', 'pre', 'code',
    'h2', 'h3', 'h4', 'a', 'img', 'table', 'thead', 'tbody', 'tr', 'th', 'td',
}

ALLOWED_ATTRIBUTES = {
    'a': {'href', 'title'},
    'img': {'src', 'alt', 'width', 'height'},
    'td': {'colspan', 'rowspan'},
    'th': {'colspan', 'rowspan'},
}

ALLOWED_SCHEMES = {'http', 'https', 'mailto'}


def clean_html(value):
    """사용자가 입력한 HTML에서 허용 목록에 없는 것을 제거한다."""
    if not value:
        return value
    return nh3.clean(
        value,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        url_schemes=ALLOWED_SCHEMES,
    )
