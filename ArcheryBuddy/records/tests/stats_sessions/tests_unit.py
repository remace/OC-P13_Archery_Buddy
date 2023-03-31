"""unit tests for stats sessions"""
import os
from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoConf.settings.testing")
setup()

from django.test import TestCase
from django.db.utils import IntegrityError
from django.db import transaction

from accounts.models import User
from equipment.models.arrows import Arrow, Feathering, Tube, Nock, Tip
from records.models import StatsRecord, StatsRecordSession
from records.utils import (
    calculate_barycentre,
    calculate_convex_hull,
    squared_distance,
    direction,
)


class StatsRecordSessionTests(TestCase):
    """model tests for PracticeRecordSessions"""

    def setUp(self):
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
        # self.srs.available_arrows.set([self.arrow1, self.arrow2, self.arrow3])
        self.datetime = self.srs.session_datetime

    def tearDown(self):
        StatsRecordSession.objects.filter(session_datetime=self.datetime).delete()
        self.srs = None
        self.user = None
        self.datetime = None

    def test_str(self):
        """test string representation for stats sessions"""
        datetime_as_string = self.datetime.strftime("%d/%m/%Y - %H:%M")
        self.assertEqual(
            f"{self.srs}",
            f"statistiques: {datetime_as_string} - {self.srs.conditions} - {self.srs.distance}m",
        )

    def test_stats_record_session_creation(self):
        """test stats record creation in database"""
        self.assertEqual(self.srs.user.pseudo, self.user.pseudo)
        self.assertEqual(self.srs.conditions, "INT")
        self.assertEqual(self.srs.distance, 18)
        self.assertEqual(self.srs.comment, "RAS")

    def test_add_available_arrows(self):

        arrows = self.srs.available_arrows.all()
        self.assertNotEqual(set(arrows), set([self.arrow1, self.arrow2, self.arrow3]))

        self.srs.available_arrows.set([self.arrow1, self.arrow2, self.arrow3])

        arrows = self.srs.available_arrows.all()

        self.assertEqual(set(arrows), set([self.arrow1, self.arrow2, self.arrow3]))

    def test_stats_record_session_save_and_delete(self):
        """
        test that stats record session save on database
        only saves one session and deleting one only deletes one
        """
        count = len(StatsRecordSession.objects.all())
        srs2 = StatsRecordSession.objects.create(
            user=self.user,
            conditions="EXT",
            distance=70,
            comment="RAS",
        )
        count2 = len(StatsRecordSession.objects.all())
        self.assertEqual(count2, count + 1)

        StatsRecordSession.objects.filter(conditions=srs2.conditions).delete()
        count3 = len(StatsRecordSession.objects.all())
        self.assertEqual(count3, count)

    def test_stats_record_session_update_in_database(self):
        """test updating a field in database"""
        srs = StatsRecordSession.objects.get(pk=self.srs.pk)
        self.assertEqual(srs.distance, 18)
        srs.distance = 20
        srs.save()
        srs = StatsRecordSession.objects.get(pk=self.srs.pk)
        self.assertEqual(srs.distance, 20)


class StatsRecordTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            pseudo="pseudo_de_test", password="password_de_test"
        )
        self.srs = StatsRecordSession.objects.create(
            user=self.user,
            conditions="INT",
            distance=18,
            comment="RAS",
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

    def tearDown(self):
        self.arrow1 = None
        self.arrow2 = None
        self.arrow3 = None
        self.srs = None
        self.user = None

    def test_stats_record_creation_update_and_delete(self):
        """test a stat record"""
        count0 = len(StatsRecord.objects.all())
        stats_record = StatsRecord.objects.create(
            arrow=self.arrow1, pos_x=0.0, pos_y=0.0, stats_session=self.srs
        )
        count1 = len(StatsRecord.objects.all())
        self.assertEqual(count1, count0 + 1)

        stats_record.pos_x = 0.5
        stats_record.pos_y = -0.5
        stats_record.save()

        stats_record2 = StatsRecord.objects.get(id=stats_record.id)

        self.assertEqual(stats_record2.pos_x, 0.5)
        self.assertEqual(stats_record2.pos_y, -0.5)

        StatsRecord.objects.filter(id=stats_record.id).delete()
        count2 = len(StatsRecord.objects.all())
        self.assertEqual(count2, count0)

    def test_create_record_session_missing_argument(self):
        count0 = len(StatsRecord.objects.all())
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                stats_record = StatsRecord.objects.create(
                    arrow=self.arrow1, pos_y=0.0, stats_session=self.srs
                )
        count1 = len(StatsRecord.objects.all())
        self.assertEqual(count1, count0)


class UtilsTest(TestCase):
    fixtures = ["records/fixtures/data.jsonl"]

    def test_calculate_barycentre_with_StatsRecords(self):
        point1 = StatsRecord.objects.get(pk=801)
        point2 = StatsRecord.objects.get(pk=802)
        points = [point1, point2]
        self.assertEqual(calculate_barycentre(points), [147.0, 225.0])

    def test_calculate_barycentre_with_points(self):
        p1 = StatsRecord.objects.get(pk=801)
        point1 = {"arrow_id": p1.pk, "pos_x": p1.pos_x, "pos_y": p1.pos_y}
        p2 = StatsRecord.objects.get(pk=802)
        point2 = {"arrow_id": p2.pk, "pos_x": p2.pos_x, "pos_y": p2.pos_y}
        points = [point1, point2]
        self.assertEqual(calculate_barycentre(points), [147.0, 225.0])

    def test_squared_distance(self):
        p1 = StatsRecord.objects.get(pk=801)
        point1 = {"arrow_id": p1.pk, "pos_x": p1.pos_x, "pos_y": p1.pos_y}
        p2 = StatsRecord.objects.get(pk=802)
        point2 = {"arrow_id": p2.pk, "pos_x": p2.pos_x, "pos_y": p2.pos_y}
        self.assertEqual(squared_distance(point1, point2), 400.0)

    def test_direction(self):
        p1 = StatsRecord.objects.get(pk=802)
        point1 = {"arrow_id": p1.pk, "pos_x": p1.pos_x, "pos_y": p1.pos_y}
        p2 = StatsRecord.objects.get(pk=800)
        point2 = {"arrow_id": p2.pk, "pos_x": p2.pos_x, "pos_y": p2.pos_y}
        p3 = StatsRecord.objects.get(pk=801)
        point3 = {"arrow_id": p3.pk, "pos_x": p3.pos_x, "pos_y": p3.pos_y}
        p4 = StatsRecord.objects.get(pk=807)
        point4 = {"arrow_id": p4.pk, "pos_x": p4.pos_x, "pos_y": p4.pos_y}

        self.assertEqual(direction(point1, point2, point3), 0)  # vecteurs parallèles
        self.assertGreater(direction(point2, point1, point4), 0)
        self.assertGreater(0, direction(point1, point2, point4))

    def test_calculate_convex_hull(self):
        points = [
            {"pos_x": record.pos_x, "pos_y": record.pos_y, "arrow_id": record.pk}
            for record in StatsRecord.objects.filter(pk__gte=920)
        ]

        true_convex_hull = [
            points[1],
            points[4],
            points[8],
            points[5],
            points[2],
            points[3],
            points[6],
        ]

        self.assertEqual(
            calculate_convex_hull(points),
            true_convex_hull,
        )
