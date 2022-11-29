import os
from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoConf.settings.testing")
setup()

from http import HTTPStatus

from accounts.models import User
from equipment.models.arrows import Arrow
from equipment.tests.constants import (
    COMPOUND,
    COMPOUND_NOT_VALID,
)


from django.test import TestCase


class AddBowsTest(TestCase):
    def setUp(self):
        user = User.objects.get_or_create(pseudo="remi123456")[0]
        self.client.force_login(user=user)

    def test_get(self):
        response = self.client.get("/bows/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("equipment/create_bows.html")

    def test_post_success(self):

        payload = {}
        response = self.client.post("/bows/create/", data=payload)
        self.assertEqual(response.status_code, 302)
        # test that the redirection is done to the detail page of the bow

    def test_post_compound_success(self):
        payload = COMPOUND
        response = self.client.post("/bows/create/", data=payload)
        self.assertEqual(response.status_code, 302)
        # TODO test that the redirection is done to the detail page of the bow

    def test_post_compound_fail(self):
        payload = COMPOUND_NOT_VALID
        response = self.client.post("/bows/create/", data=payload)
        self.assertEqual(response.status_code, 200)
        # test that context.messages has errors
        messages = list(response.context["messages"])
        self.assertGreaterEqual(len(messages), 1)
