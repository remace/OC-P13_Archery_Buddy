"""functionnal tests for stats sessions"""
import os
from django import setup

import pdb

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoConf.settings.testing")
setup()

from django.test import TestCase
from django.test import Client
from django.urls import reverse

from django.db.utils import IntegrityError
from django.db import transaction


from records.models import StatsRecord, StatsRecordSession
from equipment.models.arrows import Arrow
from accounts.models import User


class StatsRecordSessionViewsTest(TestCase):
    fixtures = ["data.jsonl"]

    def setUp(self):
        self.client = Client()
        self.user = User.objects.get(pseudo="remi123456")

    # list
    def test_user_not_logged_in_get_stats_sessions_list(self):
        response = self.client.get("/stats/list/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url.split("?")[0], "/user/login")

    def test_get_stats_sessions_list_create(self):
        self.client.login(username="remi123456", password="123456789")
        response = self.client.get("/practice/list/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("records/templates/records/list_stats_session.html")

    # create

    def test_user_not_logged_in_create_stats_session_get(self):
        response = self.client.get("/stats/create/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url.split("?")[0], "/user/login")

    def test_create_stats_session_get(self):
        self.client.login(username="remi123456", password="123456789")
        response = self.client.get("/stats/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("records/templates/records/create_stats_session.html")

    def test_create_stats_session_post(self):
        self.client.login(username="remi123456", password="123456789")
        payload = {
            "conditions": ["INT"],
            "distance": ["65"],
            "comment": ["commentaire de test"],
            "available_arrows": ["6", "8", "9"],
        }
        count = len(StatsRecordSession.objects.all())
        response = self.client.post("/stats/create/", payload)
        after_count = len(StatsRecordSession.objects.all())
        self.assertEqual(after_count, count + 1)

    def test_create_stats_session_missing_field(self):
        self.client.login(username="remi123456", password="123456789")
        payload = {
            "distance": ["65"],
            "commentaires": ["commentaire de test"],
            "available_arrows": ["6", "8", "9"],
        }
        count = len(StatsRecordSession.objects.all())

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                response = self.client.post("/stats/create/", payload)
                after_count = len(StatsRecordSession.objects.all())
                self.assertEqual(after_count, count)
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(
                    "records/templates/records/create_stats_session.html"
                )

        # TODO IntegrityError remains in test trace

    # delete
    def test_delete_stats_session(self):
        self.client.login(username="remi123456", password="123456789")
        count0 = len(StatsRecordSession.objects.all())
        response = self.client.get("/stats/delete/34/")
        count1 = len(StatsRecordSession.objects.all())

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("records/templates/records/list_stats_session.html")

    def test_delete_stats_session_bad_pk(self):
        self.client.login(username="remi123456", password="123456789")

        count0 = len(StatsRecordSession.objects.all())

        response = self.client.get("/stats/delete/75/")

        count1 = len(StatsRecordSession.objects.all())

        self.assertEqual(count1, count0)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed("records/templates/records/list_stats_session.html")

    # detail
    def test_detail_stats_session(self):
        self.client.login(username="remi123456", password="123456789")

        response = self.client.get(reverse("stats_session_detail", args=(34,)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("records/templates/records/detail_stats_session.html")

    def test_detail_stats_session_bad_pk(self):
        self.client.login(username="remi123456", password="123456789")
        client = self.client.force_login(user=self.user)
        response = self.client.get(reverse("stats_session_detail", args=(75,)))

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed("records/templates/records/list_stats_session.html")


class StatsRecordsViewsTest(TestCase):

    fixtures = ["data.jsonl"]

    def setUp(self):
        self.client = Client()
        self.user = User.objects.get(pseudo="remi123456")

        self.srs = StatsRecordSession.objects.create(
            user=self.user, conditions="INT", distance=20, comment="RAS"
        )

        self.arrow = Arrow.objects.filter(user=self.user).first()

        self.srs.available_arrows.add(self.arrow)

    def tearDown(self):
        pass

    def test_create_stats_record(self):

        client = self.client.force_login(user=self.user)

        payload = {
            "srs_id": self.srs.id,
            "arrow_id": self.arrow.pk,
            "pos_x": 50,
            "pos_y": 50,
        }

        response = self.client.post("/stats/record/create/", payload)
        self.assertEqual(response.status_code, 200)

    def test_delete_stats_record(self):

        self.client.login(username="remi123456", password="123456789")
        record_id = 84  # arbitraire
        session_id = self.srs.pk

        response = self.client.get(f"/stats/{session_id}/record/{record_id}/delete/")
        self.assertEqual(response.status_code, 200)
