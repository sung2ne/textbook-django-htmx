from django.http import HttpResponse


class HtmxRedirectMiddleware:
    """htmx 요청에 대한 302 응답을 HX-Redirect로 바꾼다.

    htmx는 302를 받으면 그 주소의 내용을 가져와 조각 자리에 넣는다.
    로그인 페이지 전체가 표 자리에 들어가는 것을 막는다.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if getattr(request, 'htmx', False) and response.status_code in (301, 302):
            location = response.headers.get('Location')
            if location:
                redirect_response = HttpResponse(status=204)
                redirect_response.headers['HX-Redirect'] = location
                return redirect_response

        return response
