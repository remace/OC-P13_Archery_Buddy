import os
from django import setup
from django.test import TestCase
from accounts.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoConf.settings.testing")
setup()


class UsersManagersTests(TestCase):
    """test class on User creation"""

    def test_create_user(self):
        """test on create_user function"""
        user = User.objects.create_user(
            pseudo="pseudo_de_test", password="password_de_test"
        )
        self.assertEqual(user.pseudo, "pseudo_de_test")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(f"{user}", user.pseudo)
        with self.assertRaises(ValueError):
            User.objects.create_user(pseudo="")
        with self.assertRaises(ValueError):
            User.objects.create_user(pseudo="", password="foo")

    def test_create_superuser(self):
        """test on createsuperuser ./manage.py command"""
        admin_user = User.objects.create_superuser(
            pseudo="superuser_de_test",
            password="password_de_test",
            is_superuser=True
        )
        self.assertEqual(admin_user.pseudo, "superuser_de_test")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        with self.assertRaises(ValueError):

            User.objects.create_superuser(
                pseudo="superuser_de_test_2",
                password="password_de_test_2",
                is_superuser=False,
            )
