import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from posts.models import Post


@pytest.fixture
def author(db):
    return User.objects.create_user('author', password='pw', first_name='작성자')


@pytest.fixture
def other(db):
    return User.objects.create_user('other', password='pw', first_name='다른사람')


@pytest.fixture
def post(author):
    return Post.objects.create(title='남의 글', content='내용',
                               created_by=author, updated_by=author)


HX = {'HTTP_HX_REQUEST': 'true'}


# (URL 이름, HTTP 메서드, 데이터)
OWNER_ONLY_ENDPOINTS = [
    ('posts:edit-row', 'get', {}),
    ('posts:save-row', 'post', {'title': '변조'}),
    ('posts:modal-edit', 'get', {}),
    ('posts:modal-save', 'post', {'title': '변조', 'content': '변조'}),
    ('posts:delete-row', 'delete', {}),
]


@pytest.mark.parametrize('url_name,method,data', OWNER_ONLY_ENDPOINTS)
def test_other_user_cannot_touch(client, other, post, url_name, method, data):
    """작성자가 아니면 403이어야 한다."""
    client.force_login(other)
    url = reverse(url_name, args=[post.id])

    response = getattr(client, method)(url, data, **HX)

    assert response.status_code == 403


@pytest.mark.parametrize('url_name,method,data', OWNER_ONLY_ENDPOINTS)
def test_anonymous_is_redirected(client, post, url_name, method, data):
    """로그인하지 않으면 접근할 수 없어야 한다."""
    url = reverse(url_name, args=[post.id])

    response = getattr(client, method)(url, data, **HX)

    assert response.status_code in (204, 302)


@pytest.mark.parametrize('url_name,method,data', OWNER_ONLY_ENDPOINTS)
def test_data_unchanged_after_forbidden(client, other, post, url_name, method, data):
    """거부된 요청이 데이터를 바꾸지 않아야 한다."""
    client.force_login(other)
    original_title = post.title

    getattr(client, method)(reverse(url_name, args=[post.id]), data, **HX)

    post.refresh_from_db()
    assert post.title == original_title
