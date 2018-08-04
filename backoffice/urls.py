import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include

from backoffice import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]

if 'debug_toolbar' in settings.INSTALLED_APPS:
    urlpatterns += (re_path(r'^__debug__/', include(debug_toolbar.urls)),)
