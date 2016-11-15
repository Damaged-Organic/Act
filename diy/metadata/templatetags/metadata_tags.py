# diy_project/diy/metadata/templatetags/metadata_tags.py
from django import template

from metadata.models import Metadata

register = template.Library()


@register.simple_tag(takes_context=True)
def provide_metadata(context):
    request = context['request']

    if request.resolver_match:
        url_name = request.resolver_match.url_name

        # Returns first matching object or None.
        return Metadata.objects.filter(url_name=url_name).first()
    else:
        return None
