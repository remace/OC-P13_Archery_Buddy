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
)
from equipment.tests.constants import (
    COMPOUND,
    COMPOUND_NOT_VALID,
from django.db import IntegrityError
from django.test import TransactionTestCase
class BowsTestCase(TransactionTestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            pseudo="pseudo_de_test", password="password_de_test"
        )
        self.compound_factory = CompoundFactory()
    def tearDown(self):
        self.user = None
        self.compound_factory = None
    def test_create_compound_success(self):
        initial_bow_count = len(CompoundBow.objects.all())
        user = self.user
        bow_attributes = COMPOUND
        bow = self.compound_factory.create_bow(user=user, bow_attributes=bow_attributes)

        # assert equality of each field in object with constant

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
