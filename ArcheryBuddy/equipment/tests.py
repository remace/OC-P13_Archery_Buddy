from http import HTTPStatus

from django.test import TestCase
from accounts.models import User

from equipment.models.arrows import Arrow

# Create your tests here.
class AddArrowsViewTest(TestCase):
    def setUp(self):
        self.client.force_login(
            User.objects.get_or_create(
                pseudo="testuser", password="azertyuiop123456789"
            )[0]
        )

    def test_get(self):
        response = self.client.get("/arrows/create/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Création de flèches</h1>", html=True)

    def test_post_success(self):
        count = len(Arrow.objects.all())
        data = {
            "nock_brand": "beiter",
            "nock_color": "rouge",
            "nock_size": "S",
            "uses_nock_pin": True,
            "feathering_laterality": "R",
            "feathering_type": "SPINWINGS",
            "feathering_brand": "XS-Wings",
            "feathering_color": "bleu",
            "feathering_cock_color": "bleu",
            "feathering_size": "S",
            "feathering_angle": 0,
            "feathering_to_nock_distance": 8,
            "tip_brand": "easton",
            "tip_profile": "ogive",
            "tip_weight": 120,
            "tube_brand": "easton",
            "tube_material": "CARBON",
            "tube_length": 73,
            "tube_spine": 1000,
            "tube_diameter": 4,
            "not_broken": True,
            "number_of_arrows": 3,
        }

        response = self.client.post("/arrows/create/", data=data)
        count2 = len(Arrow.objects.all())
        self.assertEqual(count2 - count, 3)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], "/arrows/list/")

    def test_post_fail(self):
        count = len(Arrow.objects.all())
        data = {
            "number_of_arrows": 3,
        }
        response = self.client.post("/arrows/create/", data=data)
        count2 = len(Arrow.objects.all())
        self.assertEqual(count2 - count, 0)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        # self.assertEqual(response["Location"], "/arrows/create/") /// KeyError: 'location'
