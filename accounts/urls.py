from django.urls import path
from accounts import views
from accounts.views import CustomPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', views.StandardLogin.as_view(), name='login'),
    path('logout/', views.StandardLogout.as_view(), name='logout'),
    # path('logout/', logout_then_login, kwargs={'login_url': 'login'}, name='logout'),
    path('subscribe/', views.UserCreateView.as_view(), name='subscribe'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('profile_settings/', views.UserUpdateView.as_view(), name='profile_settings'),
]
