from accounts.forms import UserForm
from backoffice.views import add_message
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.views.generic import CreateView
from django.utils.translation import ugettext_lazy as _


class StandardLogin(auth_views.LoginView):
    template_name = 'login_form.html'


class StandardLogout(auth_views.LogoutView):
    def render_to_response(self, context, **response_kwargs):
        add_message(self.request, messages.SUCCESS, _('Successfully logged out.'))
        return HttpResponseRedirect(reverse('home'))


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'registration_form.html'

    def get_success_url(self):
        add_message(self.request, messages.SUCCESS, _('Form successfully submitted.'))
        return reverse('accounts:login')
