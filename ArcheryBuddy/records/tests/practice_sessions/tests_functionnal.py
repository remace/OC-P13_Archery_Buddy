from django import setup
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoConf.settings.testing")
setup()

from django.test import TestCase
from django.test import Client


from records.models import PracticeRecord, PracticeRecordSession


class PracticeRecordViewsTest(TestCase):
    fixtures = ["data.jsonl"]

    def setUp(self):
        self.client = Client()

    # create
    def test_user_not_logged_in_get_practice_create(self):
        response = self.client.get("/practice/create/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url.split("?")[0], "/user/login")

    def test_get_practice_create(self):
        self.client.login(username="remi123456", password="123456789")
        response = self.client.get("/practice/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            "records/templates/records/create_practice_session.html"
        )

    def test_user_not_logged_in_post_practice_create(self):
        response = self.client.post("/practice/create/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url.split("?")[0], "/user/login")

    def test_post_practice_create(self):
        self.client.login(username="remi123456", password="123456789")

        payload = {}
        payload["conditions"] = "INT"
        payload["distance"] = 20
        payload["comment"] = "no comment"
        payload["max_arrows_in_volley"] = 3
        payload["number_of_volleys"] = 10
        response = self.client.post("/practice/create/", payload)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url.split("?")[0], "/practice/list/")

    # list
    def test_get_practice_list(self):
        self.client.login(username="remi123456", password="123456789")
        response = self.client.get("/practice/list/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("records/templates/records/list_practice_session.html")

    # detail
    def test_get_practice_detail(self):
        self.client.login(username="remi123456", password="123456789")
        response = self.client.get("/practice/detail/9")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            "records/templates/records/detail_practice_session.html"
        )

    def test_post_practice_detail(self):

        self.client.login(username="remi123456", password="123456789")
        count1 = len(PracticeRecord.objects.all())

        payload = {}
        payload["input-score-2-2"] = ["5"]
        payload["input-arrow-2-2"] = ["7"]

        response = self.client.post("/practice/detail/9", payload)

        count2 = len(PracticeRecord.objects.all())

        # test échoue: pas de création d'enregistrement en base

        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(
            "records/templates/records/detail_practice_session.html"
        )
        self.assertEqual(count2, count1 + 1)
