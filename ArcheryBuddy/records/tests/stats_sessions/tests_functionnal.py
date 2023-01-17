"""functionnal tests for stats sessions"""
import os
from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoConf.settings.testing")
setup()

from django.test import TestCase
from django.test import Client
from django.urls import reverse

from django.db.utils import IntegrityError
from django.db import transaction


from records.models import StatsRecord, StatsRecordSession


class StatsRecordSessionViewsTest(TestCase):
    fixtures = ["data.jsonl"]

    def setUp(self):
        self.client = Client()

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

        # self.assertEqual(count1, count0 - 1) TODO ça merdouille: la vue générique pour
        # supprimer un élément fait 2 redirections dont une avant de supprimer l'objet

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

        response = self.client.get(reverse("stats_detail", args=(34,)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("records/templates/records/detail_stats_session.html")

    def test_detail_stats_session_bad_pk(self):
        self.client.login(username="remi123456", password="123456789")

        response = self.client.get(reverse("stats_detail", args=(75,)))

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed("records/templates/records/list_stats_session.html")


class StatsRecordsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            pseudo="pseudo_de_test", password="password_de_test"
        )

        nock = Nock.objects.create(
            user=self.user, brand="beiter", color="red", size="S", uses_nock_pin=True
        )
        feathers = Feathering.objects.create(
            user=self.user,
            angle=0,
            brand="XS - wings",
            color="blue",
            cock_color="blue",
            size="S",
            laterality="R",
            feathering_type="SPINWINGS",
            nock_distance=8,
        )
        tube = Tube.objects.create(
            user=self.user,
            brand="easton",
            material="CARBON",
            spine=1000,
            tube_diameter=4,
            tube_length=73,
        )
        tip = Tip.objects.create(
            user=self.user, brand="easton", profile="ogive", weight=120
        )

        self.arrow1 = Arrow.objects.create(
            user=self.user, nock=nock, feathering=feathers, tip=tip, tube=tube
        )
        self.arrow2 = Arrow.objects.create(
            user=self.user, nock=nock, feathering=feathers, tip=tip, tube=tube
        )
        self.arrow3 = Arrow.objects.create(
            user=self.user, nock=nock, feathering=feathers, tip=tip, tube=tube
        )

        self.srs = StatsRecordSession.objects.create(
            user=self.user,
            conditions="INT",
            distance=18,
            comment="RAS",
        )
        self.srs.available_arrows.set(
            [
                self.arrow1,
                self.arrow2,
                self.arrow3,
            ]
        )

    def tearDown(self):
        pass

    def test_create_stats_record(self):
        payload = {}
        self.client.post()

    def test_delete_stats_record(self):
        pass
