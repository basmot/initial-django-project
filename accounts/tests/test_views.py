from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse
from accounts.tests.factories.user import UserFactory
from django.utils.translation import ugettext as _


class StandardLoginViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.url = reverse('login')

    def test_get_view_not_authenticated(self):
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertTemplateUsed(response, 'login_form.html')


class StandardLogoutViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.url = reverse('logout')

    def test_get_template_used(self):
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertTemplateUsed(response, 'home.html')

    def test_success_message(self):
        response = self.client.get(self.url, follow=True)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertIn(_('Successfully logged out.'), messages[0].message)


class UserCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.url = reverse('subscribe')
        new_user = UserFactory.build()
        cls.post_data = {
            'username': new_user.username,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email,
            'password1': new_user.password,
            'password2': new_user.password,
        }

    def test_get_template_used(self):
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertTemplateUsed(response, 'registration_form.html')

    def test_post_success_message(self):
        response = self.client.post(self.url, data=self.post_data, follow=True)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertIn(_('Form successfully submitted.'), messages[0].message)

    def test_post_template_used(self):
        response = self.client.post(self.url, data=self.post_data, follow=True)
        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertTemplateUsed(response, 'login_form.html')

    def test_post_new_object_created(self):
        response = self.client.post(self.url, data=self.post_data, follow=True)
        created_user = User.objects.get(username=self.post_data['username'])
        self.assertEqual(created_user.username, self.post_data['username'])
        self.assertEqual(created_user.first_name, self.post_data['first_name'])
        self.assertEqual(created_user.last_name, self.post_data['last_name'])
        self.assertEqual(created_user.email, self.post_data['email'])