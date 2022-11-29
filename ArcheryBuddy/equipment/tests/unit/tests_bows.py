import os
from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoConf.settings.testing")
setup()

from accounts.models import User
from equipment.models.bows import (
    CompoundScope,
    Dampeners,
    Stabilisation,
    CompoundArrowRest,
    CompoundBow,
    CompoundFactory,
    BarebowFactory,
    Barebow,
    Riser,
    Limbs,
    EquipmentString,
    ArrowRest,
    BergerButton,
)
from equipment.tests.constants import (
    COMPOUND,
    COMPOUND_NOT_VALID,
    BAREBOW,
    BAREBOW_NOT_VALID,
)

from django.db import IntegrityError
from django.test import TransactionTestCase


class BowsTestCase(TransactionTestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            pseudo="pseudo_de_test", password="password_de_test"
        )
        self.compound_factory = CompoundFactory()
        self.barebow_factory = BarebowFactory()

    def tearDown(self):
        self.user = None
        self.compound_factory = None
        self.barebow_factory = None

    def test_create_compound_success(self):
        initial_bow_count = len(CompoundBow.objects.all())
        user = self.user
        bow_attributes = COMPOUND
        bow = self.compound_factory.create_bow(user=user, bow_attributes=bow_attributes)

        bow_count = len(CompoundBow.objects.all())
        self.assertEqual(bow_count, initial_bow_count + 1)

    def test_create_compound_fail(self):
        initial_bow_count = len(CompoundBow.objects.all())
        initial_scope_count = len(CompoundScope.objects.all())
        initial_arrow_rest_count = len(CompoundArrowRest.objects.all())
        initial_stabilisation_count = len(Stabilisation.objects.all())
        initial_dampeners_count = len(Dampeners.objects.all())

        user = self.user
        bow_attributes = COMPOUND_NOT_VALID

        with self.assertRaises(IntegrityError):
            bow = self.compound_factory.create_bow(
                user=user, bow_attributes=bow_attributes
            )

        bow_count = len(CompoundBow.objects.all())
        scope_count = len(CompoundScope.objects.all())
        arrow_rest_count = len(CompoundArrowRest.objects.all())
        stabilisation_count = len(Stabilisation.objects.all())
        dampeners_count = len(Dampeners.objects.all())

        self.assertEqual(arrow_rest_count, initial_arrow_rest_count)
        self.assertEqual(scope_count, initial_scope_count)
        self.assertEqual(stabilisation_count, initial_stabilisation_count)
        self.assertEqual(dampeners_count, initial_dampeners_count)
        self.assertEqual(bow_count, initial_bow_count)

    def test_create_barebow_success(self):
        initial_bow_count = len(Barebow.objects.all())
        initial_riser_count = len(Riser.objects.all())
        initial_limbs_count = len(Limbs.objects.all())
        initial_string_count = len(EquipmentString.objects.all())
        initial_arrow_rest_count = len(ArrowRest.objects.all())
        initial_berger_count = len(BergerButton.objects.all())

        user = self.user

        bow_attributes = BAREBOW
        bow = self.barebow_factory.create_bow(user=user, bow_attributes=bow_attributes)

        bow_count = len(Barebow.objects.all())
        riser_count = len(Riser.objects.all())
        limbs_count = len(Limbs.objects.all())
        string_count = len(EquipmentString.objects.all())
        arrow_rest_count = len(ArrowRest.objects.all())
        berger_count = len(BergerButton.objects.all())

        self.assertEqual(riser_count, initial_riser_count + 1)
        self.assertEqual(limbs_count, initial_limbs_count + 1)
        self.assertEqual(string_count, initial_string_count + 1)
        self.assertEqual(arrow_rest_count, initial_arrow_rest_count + 1)
        self.assertEqual(berger_count, initial_berger_count + 1)
        self.assertEqual(bow_count, initial_bow_count + 1)

    def test_create_barebow_fail(self):
        initial_bow_count = len(Barebow.objects.all())
        initial_riser_count = len(Riser.objects.all())
        initial_limbs_count = len(Limbs.objects.all())
        initial_string_count = len(EquipmentString.objects.all())
        initial_arrow_rest_count = len(ArrowRest.objects.all())
        initial_berger_count = len(BergerButton.objects.all())

        user = self.user

        bow_attributes = BAREBOW_NOT_VALID

        with self.assertRaises(IntegrityError):
            bow = self.barebow_factory.create_bow(
                user=user, bow_attributes=bow_attributes
            )

        bow_count = len(Barebow.objects.all())
        riser_count = len(Riser.objects.all())
        limbs_count = len(Limbs.objects.all())
        string_count = len(EquipmentString.objects.all())
        arrow_rest_count = len(ArrowRest.objects.all())
        berger_count = len(BergerButton.objects.all())

        self.assertEqual(riser_count, initial_riser_count)
        self.assertEqual(limbs_count, initial_limbs_count)
        self.assertEqual(string_count, initial_string_count)
        self.assertEqual(arrow_rest_count, initial_arrow_rest_count)
        self.assertEqual(berger_count, initial_berger_count)
        self.assertEqual(bow_count, initial_bow_count)
