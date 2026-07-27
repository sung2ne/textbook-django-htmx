from functools import wraps

from django.shortcuts import redirect


def wants_partial(request):
    """조각으로 응답해야 하는 요청인지 판단한다.

    htmx 요청이더라도 히스토리 복원 요청이면 전체 페이지가 필요하다.
    """
    return bool(request.htmx) and not request.htmx.history_restore_request


def htmx_only(redirect_to):
    """htmx 요청이 아니면 지정한 곳으로 돌려보내는 데코레이터.

    조각 전용 URL에 사용한다. 사용자가 주소를 직접 열거나
    북마크로 들어왔을 때 깨진 화면 대신 정상 페이지를 보여 준다.
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.htmx:
                return redirect(redirect_to)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
