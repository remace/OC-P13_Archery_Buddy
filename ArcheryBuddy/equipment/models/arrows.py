from django.db import models
from accounts.models import User

from django.utils.translation import gettext_lazy as _


class Arrow(models.Model):

    # class FeatheringTypeChoices(models.TextChoices):
    #     VANES = ('VANES', 'pennes')
    #     SPINWINGS = ('SPINWINGS','spin wings')
    #     FEATHERS= ('FEATHERS', 'plumes')
    #     FLUFLU = ('FLUFLU', 'flu-flu')

    FEATHERING_TYPE_CHOICES = [
        ("VANES", "pennes"),
        ("SPINWINGS", "spin wings"),
        ("FEATHERS", "plumes"),
        ("FLUFLU", "flu-flu"),
    ]

    TUBE_MATERIAL_CHOICES = [
        ("CARBON", "carbone"),
        ("ALU", "aluminium"),
        ("WOOD", "bois"),
    ]

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    # encoche
    nock = models.CharField("encoche", max_length=60)

    # empennage

    feathering_type = models.CharField(
        "type d'empennage",
        max_length=10,
        choices=FEATHERING_TYPE_CHOICES,
        default=FEATHERING_TYPE_CHOICES[0],
    )
    feathering_brand = models.CharField("marque de plumes", max_length=60)
    feathering_color = models.CharField("couleur d'empennage", max_length=60)
    feathering_cock_color = models.CharField("couleur de plume coq", max_length=60)
    feathering_size = models.CharField("taille", max_length=60)
    feathering_angle = models.IntegerField("angle")  # in degrees
    feathering_nock_distance = models.IntegerField("distance à l'encoche")  # in mm
    # pointe
    tip_brand = models.CharField("marque", max_length=60)
    tip_profile = models.CharField("profil", max_length=60)
    tip_weight = models.CharField("masse (grains)", max_length=60)  # in grains
    # tube
    tube_brand = models.CharField("marque", max_length=60)
    tube_material = models.CharField(
        "matériau",
        max_length=10,
        choices=TUBE_MATERIAL_CHOICES,
        default=TUBE_MATERIAL_CHOICES[0],
    )
    tube_length = models.FloatField("longueur")
    tube_spine = models.FloatField("flèche/spine")
    tube_diameter = models.FloatField("diametre exterieur")
    # general attributes
    not_broken = models.BooleanField("en état d'utilisation", default=True)
