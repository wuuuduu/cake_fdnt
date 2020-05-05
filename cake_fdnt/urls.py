import logging

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

logger = logging.getLogger(__name__)

urlpatterns = [
    path('api/v1/', include('api.api_urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                      path('admin/', admin.site.urls),
                  ] + urlpatterns
else:
    urlpatterns = [
                      path('django-admin-prod/', admin.site.urls),
                  ] + urlpatterns
