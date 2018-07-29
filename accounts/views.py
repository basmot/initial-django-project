from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.urls import reverse


class StandardLogin(auth_views.LoginView):
    template_name = 'login_form.html'


class StandardLogout(auth_views.LogoutView):
    def render_to_response(self, context, **response_kwargs):
        return HttpResponseRedirect(reverse('home'))
