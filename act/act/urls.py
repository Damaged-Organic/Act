# act_project/act/act/urls.py
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView

from .admin import admin_site
from .views_api import api_root

from website import views_error

handler400 = views_error.handler400
handler403 = views_error.handler403
handler404 = views_error.handler404
handler500 = views_error.handler500

''' Avoiding React.js routing conflict '''
urlpatterns = [
    url(r'^deus_ex_machina$', RedirectView.as_view(url='/deus_ex_machina/')),
    url(r'^api$', RedirectView.as_view(url='/api/')), ]

''' Admin view '''
urlpatterns += [
    url(r'^deus_ex_machina/', admin_site.urls), ]

''' Root API view '''
urlpatterns += [
    url(r'^api/$', api_root), ]

''' Metadata application API '''
urlpatterns += [
    url(r'^api/', include('metadata.urls_api')), ]

''' Subscription application API '''
urlpatterns += [
    url(r'^api/', include('subscription.urls_api')), ]

''' Website application API '''
urlpatterns += [
    url(r'^api/', include('website.urls_api')), ]

''' Internationalization '''
urlpatterns += i18n_patterns(
    url(r'', include('website.urls')),
    prefix_default_language=False)

if settings.DEBUG:
    from django.conf.urls.static import static
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)), ]
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
