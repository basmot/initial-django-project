from django.urls import path, reverse_lazy
from accounts import views
from django.contrib.auth import views as auth_views

from accounts.views import CustomPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', views.StandardLogin.as_view(), name='login'),
    path('logout/', views.StandardLogout.as_view(), name='logout'),
    # path('logout/', logout_then_login, kwargs={'login_url': 'login'}, name='logout'),
    path('subscribe/', views.UserCreateView.as_view(), name='subscribe'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
]
