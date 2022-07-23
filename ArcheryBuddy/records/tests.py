from django.test import TestCase
from django.core.exceptions import ValidationError


from records.models import (
    PracticeRecord,
    PracticeRecordSession,
    StatsRecord,
    StatsRecordSession,
)

from accounts.models import User
from equipment.models.arrows import Arrow, Feathering, Tube, Nock, Tip


class PracticeRecordSessionTests(TestCase):
    """model tests for PracticeRecordSessions"""

    def setUp(self):
        self.user = User.objects.create_user(
            pseudo="pseudo_de_test", password="password_de_test"
        )
        self.prs = PracticeRecordSession.objects.create(
            user=self.user,
            conditions="INT",
            distance=18,
            comment="RAS",
            number_of_volleys=2,
        )
        self.datetime = self.prs.session_datetime

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
        PracticeRecordSession.objects.filter(session_datetime=self.datetime).delete()
        self.prs = None
        self.user = None
        self.datetime = None

    def test_str(self):
        """returns str representation of the object"""
        datetime_as_string = self.datetime.strftime("%d/%m/%Y - %H:%M")
        self.assertEqual(
            f"{self.prs}",
            f"Entrainement: {datetime_as_string} - {self.prs.conditions} - {self.prs.distance}m",
        )

    def test_practice_record_session_creation(self):
        """test PracticeRecordSession creation, attributes should be OK"""
        self.assertEqual(self.prs.user.pseudo, self.user.pseudo)
        self.assertEqual(self.prs.conditions, "INT")
        self.assertEqual(self.prs.distance, 18)
        self.assertEqual(self.prs.comment, "RAS")
        self.assertEqual(self.prs.number_of_volleys, 2)
        self.assertEqual(self.prs.session_datetime, self.datetime)

    def test_save_and_delete(self):
        """
        test that practice record session save on database
        only saves one session and deleting one only deletes one
        """
        count = len(PracticeRecordSession.objects.all())
        prs2 = PracticeRecordSession.objects.create(
            user=self.user,
            conditions="EXT",
            distance=70,
            comment="RAS",
            number_of_volleys=2,
        )
        count2 = len(PracticeRecordSession.objects.all())
        self.assertEqual(count2, count + 1)

        PracticeRecordSession.objects.filter(conditions=prs2.conditions).delete()
        count3 = len(PracticeRecordSession.objects.all())
        self.assertEqual(count3, count)

    def test_update_in_database(self):
        """test updating a field in database"""
        prs = PracticeRecordSession.objects.get(conditions="INT")
        self.assertEqual(prs.distance, 18)
        prs.distance = 20
        prs.save()
        prs = PracticeRecordSession.objects.get(conditions="INT")
        self.assertEqual(prs.distance, 20)

    def test_total_score(self):
        PracticeRecord.objects.create(
            arrow=self.arrow1, score=10, practice_session=self.prs, volley=1
        )
        PracticeRecord.objects.create(
            arrow=self.arrow2, score=10, practice_session=self.prs, volley=1
        )
        PracticeRecord.objects.create(
            arrow=self.arrow3, score=10, practice_session=self.prs, volley=1
        )
        PracticeRecord.objects.create(
            arrow=self.arrow1, score=10, practice_session=self.prs, volley=2
        )
        PracticeRecord.objects.create(
            arrow=self.arrow2, score=10, practice_session=self.prs, volley=2
        )
        PracticeRecord.objects.create(
            arrow=self.arrow3, score=8, practice_session=self.prs, volley=2
        )

        total = self.prs.get_total_score()

        self.assertEqual(total, 58)


class PracticeRecordTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            pseudo="pseudo_de_test", password="password_de_test"
        )
        self.prs = PracticeRecordSession.objects.create(
            user=self.user,
            conditions="INT",
            distance=18,
            comment="RAS",
            number_of_volleys=2,
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
        self.prs = None
        self.user = None

    def test_create_practice_record_nominal_case(self):
        """test recording an arrow, nominal case"""
        length = len(PracticeRecord.objects.all())
        self.assertEqual(length, 0)
        practice_record = PracticeRecord.objects.create(
            arrow=self.arrow1, score=10, practice_session=self.prs, volley=1
        )
        self.assertEqual(practice_record.arrow, self.arrow1)
        self.assertEqual(practice_record.score, 10)
        self.assertEqual(practice_record.practice_session, self.prs)
        self.assertEqual(practice_record.volley, 1)
        length = len(PracticeRecord.objects.all())
        self.assertEqual(length, 1)

    def test_create_practice_record_score_out_of_bounds(self):
        """test creating a practice record with score out of bounds (0,10)"""
        with self.assertRaises(
            ValidationError, msg="score may be an integer value between 0 and 10"
        ):
            PracticeRecord.objects.create(
                arrow=self.arrow1, score=-1, practice_session=self.prs, volley=1
            )

        with self.assertRaisesMessage(
            ValidationError, "score may be an integer value between 0 and 10"
        ):
            PracticeRecord.objects.create(
                arrow=self.arrow1, score=11, practice_session=self.prs, volley=1
            )

    def test_create_practice_record_volley_out_of_bounds(self):
        """test creates a practice record with the volley identifier out if bounds"""
        with self.assertRaises(
            ValidationError,
            msg="volley may be an integer value between 1 and session's volley number",
        ):
            PracticeRecord.objects.create(
                arrow=self.arrow1, score=10, practice_session=self.prs, volley=-1
            )
            print("volée -1 faite")

        with self.assertRaises(
            ValidationError,
            msg="volley may be an integer value between 1 and session's volley number",
        ):
            PracticeRecord.objects.create(
                arrow=self.arrow1, score=10, practice_session=self.prs, volley=3
            )


class StatsRecordSessionTests(TestCase):
    """model tests for PracticeRecordSessions"""

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
        self.datetime = self.srs.session_datetime

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
        StatsRecordSession.objects.filter(session_datetime=self.datetime).delete()
        self.srs = None
        self.user = None
        self.datetime = None

    def test_str(self):
        datetime_as_string = self.datetime.strftime("%d/%m/%Y - %H:%M")
        self.assertEqual(
            f"{self.srs}",
            f"statistiques: {datetime_as_string} - {self.srs.conditions} - {self.srs.distance}m",
        )

    def test_stats_record_session_creation(self):
        self.assertEqual(self.srs.user.pseudo, self.user.pseudo)
        self.assertEqual(self.srs.conditions, "INT")
        self.assertEqual(self.srs.distance, 18)
        self.assertEqual(self.srs.comment, "RAS")
        self.assertEqual(self.srs.session_datetime, self.datetime)

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
        srs = StatsRecordSession.objects.get(conditions="INT")
        self.assertEqual(srs.distance, 18)
        srs.distance = 20
        srs.save()
        srs = StatsRecordSession.objects.get(conditions="INT")
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
        count0 = len(StatsRecord.objects.all())
        stats_record = StatsRecord.objects.create(
            arrow=self.arrow1, pos_x=0.0, pos_y=0.0, stats_session=self.srs
        )
        count1 = len(StatsRecord.objects.all())
        self.assertEqual(count1, count0 + 1)

        stats_record.pos_x = 0.5
        stats_record.pos_y = -0.5
        stats_record.save()

        stats_record2 = StatsRecord.objects.all()[0]

        self.assertEqual(stats_record2.pos_x, 0.5)
        self.assertEqual(stats_record2.pos_y, -0.5)

        PracticeRecordSession.objects.filter(id=stats_record.id).delete()
        count2 = len(PracticeRecordSession.objects.all())
        self.assertEqual(count2, count0)
