from django.utils.cache import patch_vary_headers


class HtmxVaryMiddleware:
    """htmx 요청과 일반 요청의 응답이 캐시에서 섞이지 않게 한다.

    같은 URL이 조각과 전체 페이지를 모두 응답하므로,
    캐시가 둘을 구분할 수 있도록 Vary 헤더를 붙인다.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        patch_vary_headers(response, ['HX-Request', 'HX-History-Restore-Request'])
        return response
