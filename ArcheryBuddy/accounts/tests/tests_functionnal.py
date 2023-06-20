import os
from http import HTTPStatus

from django import setup
from django.contrib import auth
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from accounts.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoConf.settings.testing")
setup()


class LoginViewTestCase(TestCase):
    fixtures = ["records/fixtures/data.jsonl"]

    def setUp(self):
        self.client = Client()

    def test_get_login_view_nominal_case(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed("accounts/login.html")

    def test_post_login_view_nominal_case(self):
        payload = {
            "pseudo": "remi123456",
            "password": "123456789"
            }
        response = self.client.post(reverse('login'), data=payload)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_post_login_view_bad_credentials(self):
        payload = {
            "pseudo": "",
            "password": ""
            }
        response = self.client.post(reverse('login'), data=payload)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_forbidden_method(self):
        response = self.client.delete(reverse('login'))
        self.assertEqual(response.status_code, HTTPStatus.OK)


class RegisterViewTestCase(TestCase):
    fixtures = ["records/fixtures/data.jsonl"]

    def setUp(self):
        self.client = Client()

    def test_get_login_view_nominal_case(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed("accounts/register.html")

    def test_forbidden_method(self):
        response = self.client.delete(reverse('register'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_register_view_nominal_case(self):
        payload = {
            "first_name": "new",
            "last_name": "user",
            "pseudo": "new_user",
            "password": "1234",
            "password2": "1234"
            }
        response = self.client.post(reverse('register'), data=payload)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_post_register_view_mismatching_passwords(self):
        payload = {
            "first_name": "new",
            "last_name": "user",
            "pseudo": "new_user",
            "password": "1234",
            "password2": "12345"
            }
        response = self.client.post(reverse('register'), data=payload)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)


class LogoutViewTestCase(TestCase):
    fixtures = ["records/fixtures/data.jsonl"]

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get(pseudo="remi123456"))

    def test_get_login_view_nominal_case(self):
        self.assertEqual(auth.get_user(self.client).is_authenticated, True)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(auth.get_user(self.client).is_authenticated, False)


class DetailViewTestCase(TestCase):
    fixtures = ["records/fixtures/data.jsonl"]

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get(pseudo="remi123456"))

    def test_get_login_view_nominal_case(self):
        response = self.client.get(reverse('account_detail'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed("accounts/detail.html")
