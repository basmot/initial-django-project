from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView

from accounts.forms import UserForm
from backoffice.views import add_message
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
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


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        add_message(self.request, messages.SUCCESS, _('Password successfully updated.'))
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'profile_settings.html'
    success_url = reverse_lazy('accounts:profile_settings')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        add_message(self.request, messages.SUCCESS, _('Profile data successfully updated.'))
        self._warning_if_username_changed(form)
        return super().form_valid(form)

    def _warning_if_username_changed(self, form):
        new_username = form.cleaned_data['username']
        old_username = form.initial['username']
        if new_username != old_username:
            message = _("Warning : your username has been changed. Next time you log in to our site, use <b>'{}'</b> "
                        "(the new one) instead of <s>'{}'</s> (the old one)").format(new_username, old_username)
            add_message(self.request, messages.WARNING, message)
