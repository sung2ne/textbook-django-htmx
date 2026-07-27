import pytest
from django.contrib.auth.models import User

from posts.models import Post


@pytest.fixture
def seeded(db):
    """브라우저 테스트용 데이터."""
    author = User.objects.create_user('author', password='pw1234!', first_name='작성자')
    for i in range(15):
        Post.objects.create(
            title=f'게시글 {i:02d}',
            content='내용',
            created_by=author,
            updated_by=author,
        )
    return author


@pytest.fixture
def logged_in_page(page, live_server, seeded):
    """로그인을 마친 브라우저 페이지."""
    page.goto(f'{live_server.url}/auth/login/')
    page.fill('input[name=username]', 'author')
    page.fill('input[name=password]', 'pw1234!')
    page.click('button[type=submit]')
    page.wait_for_url(f'{live_server.url}/**')
    return page
