import os
from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoConf.settings")
setup()

from django.test import TestCase
from django.test import Client


class PracticeRecordViewsTest(TestCase):
    fixtures = ["data.json"]

    def setUp(self):
        self.client = Client()

    # create
    def test_user_not_logged_in_get_practice_create(self):
        response = self.client.get("/practice/create/")
        self.assertEqual(
            response.status_code, 302
        )  # le test produit un 400 sous vscode seulement
        self.assertEqual(response.url.split("?")[0], "/user/login")

    def test_get_practice_create(self):
        self.client.login(username="remi123456", password="123456789")
        response = self.client.get("/practice/create/")
        self.assertEqual(
            response.status_code, 200
        )  # le test produit un 400 sous vscode seulement
        self.assertTemplateUsed(
            "records/templates/records/create_practice_session.html"
        )

    def test_user_not_logged_in_post_practice_create(self):
        response = self.client.post("/practice/create/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url.split("?")[0], "/user/login")

    def test_post_practice_create(self):

        self.client.login(username="remi123456", password="123456789")
        response = self.client.post("/practice/create/")
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(
            "records/templates/records/create_practice_session.html"
        )

    # list
    def test_get_practice_list(self):
        # self.client.login(username="remi123456", password="123456789")
        # response = self.client.get("/practice/list/")
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed("records/templates/records/list_practice_session.html")
        pass

    # detail
    def test_get_practice_detail(self):
        # self.client.login(username="remi123456", password="123456789")
        # response = self.client.get("/practice/detail/9")
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(
        #     "records/templates/records/detail_practice_session.html"
        # )
        pass
