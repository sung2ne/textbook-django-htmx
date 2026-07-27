from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404


def get_own_object_or_403(model, pk, user, owner_field='created_by'):
    """객체를 가져오되 소유자가 아니면 403을 일으킨다."""
    obj = get_object_or_404(model, id=pk)
    if getattr(obj, f'{owner_field}_id') != user.id:
        raise PermissionDenied('권한이 없습니다.')
    return obj
