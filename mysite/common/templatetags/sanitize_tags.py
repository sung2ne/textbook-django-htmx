from django import template
from django.utils.safestring import mark_safe

from common.sanitize import clean_html

register = template.Library()


@register.filter(name='clean_html')
def clean_html_filter(value):
    return mark_safe(clean_html(value))
