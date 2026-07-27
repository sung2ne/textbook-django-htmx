import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from posts.models import Post

TITLES = [
    '공지사항 안내', '시스템 점검 일정', '신규 기능 소개', '이용 약관 변경',
    '자주 묻는 질문', '서비스 개선 사항', '보안 업데이트', '휴무일 안내',
]


class Command(BaseCommand):
    help = '실습용 게시글을 생성한다'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=120)

    def handle(self, *args, **options):
        count = options['count']

        authors = list(User.objects.all()[:5])
        if not authors:
            self.stderr.write('사용자가 없습니다. createsuperuser를 먼저 실행하세요.')
            return

        created = 0
        for i in range(count):
            author = random.choice(authors)
            Post.objects.create(
                title=f'{random.choice(TITLES)} {i + 1:03d}',
                content=f'{i + 1}번째 게시글 내용입니다.\n실습용으로 생성되었습니다.',
                created_by=author,
                updated_by=author,
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(f'게시글 {created}건 생성'))
