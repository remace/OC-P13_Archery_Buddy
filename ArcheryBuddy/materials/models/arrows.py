from django.db import models
from accounts.models import User

from django.utils.translation import gettext_lazy as _



class Arrow(models.Model):

    # class FeatheringTypeChoices(models.TextChoices):
    #     VANES = ('VANES', 'pennes')
    #     SPINWINGS = ('SPINWINGS','spin wings')
    #     FEATHERS= ('FEATHERS', 'plumes')
    #     FLUFLU = ('FLUFLU', 'flu-flu')

    FEATHERING_TYPE_CHOICES=[
        ('VANES', 'pennes'),
        ('SPINWINGS','spin wings'),
        ('FEATHERS', 'plumes'),
        ('FLUFLU', 'flu-flu'),
    ]

    TUBE_MATERIAL_CHOICES=[
        ("CARBON", "carbone"),
        ("ALU", "aluminium"),
        ("WOOD", "bois"),
    ]


    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    # encoche
    nock = models.CharField(max_length=60)

    # empennage
    
    feathering_type = models.CharField(
        max_length=10,
        choices=FEATHERING_TYPE_CHOICES,
        default=FEATHERING_TYPE_CHOICES[0]
        )
    feathering_brand = models.CharField(max_length=60)
    feathering_color = models.CharField(max_length=60)
    feathering_cock_color = models.CharField(max_length=60)
    feathering_size = models.CharField(max_length=60)
    feathering_angle = models.IntegerField() # in degrees
    feathering_nock_distance = models.IntegerField() # in mm
    # pointe
    tip_brand = models.CharField(max_length=60)
    tip_profile = models.CharField(max_length=60)
    tip_weight = models.CharField(max_length=60) # in grains
    # tube
    tube_brand = models.CharField(max_length=60)
    tube_material = models.CharField(
        max_length=10,
        choices=TUBE_MATERIAL_CHOICES,
        default=TUBE_MATERIAL_CHOICES[0]
        )
    tube_length = models.FloatField()
    tube_spine = models.FloatField()
    tube_diameter = models.FloatField()
    # general attributes
    not_broken = models.BooleanField(default=True)
