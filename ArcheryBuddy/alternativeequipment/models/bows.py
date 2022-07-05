from django.db import models

class Bow(models.Model):
    
    LATERALITY_CHOICES = [
        ('R', 'droitier'),
        ('L', 'gaucher')
    ]

    STRING_MATERIAL_CHOICE=[
        ("8125", "8125"),
        ("DACRON", "Dacron"),
        ('FF', "Fast-Flight"),
        ('D75', "D75"),
        ("FS", "Flex Supra"),
    ]

    ARROW_REST_TYPE_CHOICE=[
        ("SM","short, magnetic"),
        ("LM","long, magnetic"),
        ("P", "plastic"),
    ]

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    power = models.IntegerField()
    laterality = models.CharField(max_length=10,
        choices = LATERALITY_CHOICES,
        default = LATERALITY_CHOICES[0]
        )
    
    class Meta:
        abstract = True


class Riser(models.Model):
    brand = models.CharField("Marque", max_length=30)
    size = models.IntegerField("Taille")
    color = models.CharField("Couleur", max_length=30)
    grip = models.CharField("grip", max_length=30)

    def __str__(self):
        return f'{self.brand} - {self.color}'
    


class Limbs(models.Model):
    brand = models.CharField("Marque", max_length=30)
    power = models.Integer_Field("Puissance")
    size = models.IntegerField('taille (")')

    def __str__(self):
        return f'{brand}'


class EquipmentString(models.Model):
    brand = models.CharField(max_length=30)
    material = models.CharField(max_length=10,
        choices = Bow.STRING_MATERIAL_CHOICE,
        default = Bow.STRING_MATERIAL_CHOICE[0]
        )
    number_of_strands = models.IntegerField("Nombre de brins")

    def __str__(self):
        return f'{self.id}: {self.brand} - {self.number_of_strands}'


class Barebow(Bow):
    riser = models.ForeignKey("alternativeequipment.Riser", on_delete=models.CASCADE)
    limbs = models.ForeignKey("alternativeequipment.Limbs", on_delete=models.CASCADE)
    string = models.ForeignKey("alternativeequipment.EquipmentString", on_delete=models.CASCADE)
    
    # settings done on the bow or the string...
    number_of_turns = models.IntegerField()
    nockset_offset = models.FloatField()
    band = models.FloatField()
    high_tiller = models.FloatField()
    low_tiller = models.FloatField()


class OlympicBow(Bow):
    
    barebow = ForeignKey("alternativeequipment.Barebow", on_delete=models.CASCADE)

    # viseur
        # plus tard: réglages du viseur selon distance
    scope_brand = models.CharField(max_length=30)

    # clicker
    clicker_brand = models.CharField(max_length=30)

    # repose_flèches
    arrow_rest_brand = models.CharField(max_length=30)
    arrow_rest_type = models.CharField(
        max_length=2,
        choices = Bow.ARROW_REST_TYPE_CHOICE,
        default = Bow.ARROW_REST_TYPE_CHOICE[0])
    # berger_button
    berger_button_brand = models.CharField(max_length=30)
    berger_button_spring = models.CharField(max_length=30)
    # stabilisation
    stabilisation_brand = models.CharField(max_length=30)
    # amortisseurs de stabilisation
    dampeners = models.CharField(max_length=30)