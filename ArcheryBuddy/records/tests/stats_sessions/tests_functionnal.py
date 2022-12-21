"""functionnal tests for stats sessions"""
import os
from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoConf.settings.testing")
setup()

from django.test import TestCase
from django.test import Client


from records.models import StatsRecord, StatsRecordSession


class PracticeRecordViewsTest(TestCase):
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

    def test_create_stats_session_post(self):
        self.client.login(username="remi123456", password="123456789")
        pass

    def test_create_stats_session_missing_field(self):
        self.client.login(username="remi123456", password="123456789")
        pass
