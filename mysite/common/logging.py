import logging
import time

logger = logging.getLogger('request.timing')


class RequestTimingMiddleware:
    """요청 종류와 소요 시간을 로그로 남긴다.

    htmx 조각 요청과 전체 페이지 요청을 구분해 기록한다.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()
        response = self.get_response(request)
        elapsed_ms = (time.perf_counter() - start) * 1000

        kind = 'partial' if getattr(request, 'htmx', False) else 'page'

        logger.info(
            'kind=%s method=%s path=%s status=%s ms=%.1f',
            kind,
            request.method,
            request.path,
            response.status_code,
            elapsed_ms,
        )
        return response
