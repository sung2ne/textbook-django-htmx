import pytest
from playwright.sync_api import expect


@pytest.mark.django_db
def test_live_search_updates_list(logged_in_page, live_server):
    """검색어를 입력하면 목록이 좁혀진다."""
    page = logged_in_page
    page.goto(f'{live_server.url}/posts/')

    expect(page.locator('#post-list tbody tr')).to_have_count(11)   # 10건 + 더 보기

    page.fill('input[name=searchKeyword]', '게시글 03')

    expect(page.locator('#post-list tbody tr')).to_have_count(1)
    expect(page.locator('#post-list')).to_contain_text('게시글 03')
