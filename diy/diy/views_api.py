# diy_project/diy/diy/views_api.py
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # Metadata
        'metadata': reverse('metadata_list', request=request, format=format),
        # Subscription
        'subscribers': reverse(
            'subscribers_list', request=request, format=format
        ),
        # Website
        'intro_content': reverse(
            'intro_content_singular', request=request, format=format
        ),
        'sponsors': reverse('sponsors_list', request=request, format=format),
        'socials': reverse('socials_list', request=request, format=format),
        'activities': reverse(
            'activities_list', request=request, format=format
        ),
        'projects_areas': reverse(
            'projects_areas_list', request=request, format=format
        ),
        'projects': reverse('projects_list', request=request, format=format),
        'events_categories': reverse(
            'events_categories_list', request=request, format=format
        ),
        'events': reverse('events_list', request=request, format=format),
        'cities': reverse('cities_list', request=request, format=format),
        'participants': reverse(
            'participants_list', request=request, format=format
        ),
        'contacts': reverse('contacts_list', request=request, format=format),
        'centres': reverse('centres_list', request=request, format=format),
        'worksheets': reverse(
            'worksheets_list', request=request, format=format
        ),
    })
