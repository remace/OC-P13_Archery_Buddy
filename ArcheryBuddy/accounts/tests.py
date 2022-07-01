from django.contrib.auth import get_user_model
from django.test import TestCase

class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(pseudo='pseudo_de_test', password='password_de_test')
        self.assertEqual(user.pseudo, 'pseudo_de_test')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEquals(f'{user}',user.pseudo)
        try:
            self.assertIsNone(user.email)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_user(pseudo='')
        with self.assertRaises(ValueError):
            User.objects.create_user(pseudo='', password="foo")
        

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            pseudo='superuser_de_test', 
            password='password_de_test',
            is_superuser=True)
        self.assertEqual(admin_user.pseudo, 'superuser_de_test')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        
        try:
            self.assertIsNone(admin_user.email)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            
            User.objects.create_superuser(
                pseudo='superuser_de_test_2', 
                password='password_de_test_2',
                is_superuser=False)