from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.StandardLogin.as_view(), name='login'),
    path('logout/', views.StandardLogout.as_view(), name='logout'),
    # path('logout/', logout_then_login, kwargs={'login_url': 'login'}, name='logout'),
]
