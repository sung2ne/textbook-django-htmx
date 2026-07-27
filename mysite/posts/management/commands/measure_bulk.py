import time

from django.core.management.base import BaseCommand

from posts.models import Post


class Command(BaseCommand):
    help = '벌크 삭제 소요 시간을 측정한다'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=100)

    def handle(self, *args, **options):
        count = options['count']
        ids = list(Post.objects.values_list('id', flat=True)[:count])

        start = time.perf_counter()
        Post.objects.filter(id__in=ids).delete()
        elapsed = time.perf_counter() - start

        self.stdout.write(f'{len(ids)}건 삭제: {elapsed:.2f}초')
        self.stdout.write(f'건당 평균: {elapsed / max(len(ids), 1) * 1000:.1f}ms')
