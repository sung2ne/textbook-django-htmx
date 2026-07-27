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
    return Post.objects.create(
        title='테스트 게시글',
        content='내용',
        created_by=author,
        updated_by=author,
    )


HX = {'HTTP_HX_REQUEST': 'true'}


def test_list_returns_full_page_for_browser(client, author, post):
    """주소창으로 들어오면 전체 페이지를 준다."""
    client.force_login(author)
    response = client.get(reverse('posts:list'))

    assert response.status_code == 200
    assert b'<!DOCTYPE html' in response.content
    assert 'posts/list.html' in [t.name for t in response.templates]


def test_list_returns_partial_for_htmx(client, author, post):
    """htmx 요청이면 조각만 준다."""
    client.force_login(author)
    response = client.get(reverse('posts:list'), **HX)

    assert response.status_code == 200
    assert b'<!DOCTYPE html' not in response.content
    assert 'posts/partials/post_list.html' in [t.name for t in response.templates]
