def _filter_posts(params, user):
    """조건에 맞는 게시글 QuerySet을 돌려준다."""
    posts = Post.objects.select_related('created_by')

    searchType = params['searchType']
    searchKeyword = params['searchKeyword']
    ...
