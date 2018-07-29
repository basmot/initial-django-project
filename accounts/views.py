from accounts.forms import UserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.views.generic import CreateView


class StandardLogin(auth_views.LoginView):
    template_name = 'login_form.html'


class StandardLogout(auth_views.LogoutView):
    def render_to_response(self, context, **response_kwargs):
        return HttpResponseRedirect(reverse('home'))


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'subscribe_form.html'

    def get_success_url(self):
        return reverse('login')
