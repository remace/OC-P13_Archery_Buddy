from django.test import TestCase
from django.urls import reverse


class HoweViewTest(TestCase):
    def test_home_view_test_case(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
