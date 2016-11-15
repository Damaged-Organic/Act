# diy_project/diy/website/templatetags/website_helpers.py
from datetime import datetime

from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import activate, get_language
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def absolute_url(request):
    return request.build_absolute_uri(reverse('website:index'))[:-1]


@register.filter
def sift_digits(value):
    return ''.join(i for i in value if i.isdigit())


@register.filter
def interpolate_with_timeline(value, start_year):
    current_year = str(datetime.now().year)

    if start_year != current_year:
        timeline = ''.join([start_year, ' - ', current_year])
    else:
        timeline = current_year

    return value % timeline


@register.simple_tag
def get_url_with_kwargs(request):
    url_name = ''.join([
        request.resolver_match.app_name,
        ':',
        request.resolver_match.url_name,
    ])

    url_kwargs = request.resolver_match.kwargs

    return reverse(url_name, None, None, url_kwargs)


@register.simple_tag()
def paragraphize(value, paragraph_open, paragraph_close):
    paragraphs = filter(None, value.split('\n'))
    paragraphized = ''.join(
        "{0}{1}{2}".format(paragraph_open, paragraph, paragraph_close)
        for paragraph in paragraphs
    )

    return mark_safe(paragraphized)
