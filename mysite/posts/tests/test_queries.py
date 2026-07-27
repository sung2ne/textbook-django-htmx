from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from posts.models import Post


class PostListQueryCountTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.viewer = User.objects.create_user('viewer', password='pw')
        authors = [
            User.objects.create_user(f'author{i}', password='pw', first_name=f'작성자{i}')
            for i in range(10)
        ]
        for i in range(30):
            Post.objects.create(
                title=f'게시글 {i}',
                content='내용',
                created_by=authors[i % 10],
                updated_by=authors[i % 10],
            )

    def setUp(self):
        self.client.force_login(self.viewer)

    def test_list_query_count_does_not_grow_with_rows(self):
        """행 수가 늘어도 쿼리 수가 늘지 않아야 한다."""
        url = reverse('posts:list')

        with self.assertNumQueries(4):
            self.client.get(url, {'per_page': 10})

        with self.assertNumQueries(4):
            self.client.get(url, {'per_page': 30})
