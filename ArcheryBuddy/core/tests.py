from django.test import TestCase


class HoweViewTest(TestCase):
    def home_view_test_case(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
