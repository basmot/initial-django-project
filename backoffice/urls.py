from backoffice.settings.base import INSTALLED_APPS
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from backoffice import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]

import debug_toolbar

if 'debug_toolbar' in settings.INSTALLED_APPS:
    urlpatterns += (re_path(r'^__debug__/', include(debug_toolbar.urls)),)
