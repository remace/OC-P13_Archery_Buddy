from django.db import models


class Nock(models.Model):

    user = models.ForeignKey(
        "accounts.User", related_name="alternative_nocks", on_delete=models.CASCADE
    )
    brand = models.CharField("encoche", max_length=60)
    color = models.CharField("couleur", max_length=60)
    size = models.CharField("taille", max_length=10)
    uses_nock_pin = models.BooleanField("monté sur nock pin", default=False)

    def __str__(self):
        return f"{self.brand} - {self.size} - {self.color}"

    class Meta:
        verbose_name = "Encoche"
        verbose_name_plural = "Encoches"


class Feathering(models.Model):

    LATERALITY_CHOICES = [("R", "droitier"), ("L", "gaucher")]

    FEATHERING_TYPE_CHOICES = [
        ("VANES", "pennes"),
        ("SPINWINGS", "spin wings"),
        ("FEATHERS", "plumes"),
        ("FLUFLU", "flu-flu"),
    ]

    laterality = models.CharField(
        "latéralité",
        max_length=1,
        choices=LATERALITY_CHOICES,
        default=FEATHERING_TYPE_CHOICES[0],
    )

    feathering_type = models.CharField(
        "type d'empennage",
        max_length=10,
        choices=FEATHERING_TYPE_CHOICES,
        default=FEATHERING_TYPE_CHOICES[0],
    )

    user = models.ForeignKey(
        "accounts.User",
        related_name="alternative_featherings",
        on_delete=models.CASCADE,
    )

    brand = models.CharField("marque de plumes", max_length=60)
    color = models.CharField("couleur d'empennage", max_length=60)
    cock_color = models.CharField("couleur de plume coq", max_length=60)
    size = models.CharField("taille", max_length=60)
    angle = models.IntegerField("angle")  # in degrees
    nock_distance = models.IntegerField("distance à l'encoche")  # in mm

    def __str__(self):
        return f"{self.brand} - {self.cock_color} - {self.color}"

    class Meta:
        verbose_name = "Empennage"
        verbose_name_plural = "Empennages"


class Tip(models.Model):
    user = models.ForeignKey(
        "accounts.User", related_name="alternative_tips", on_delete=models.CASCADE
    )
    brand = models.CharField("marque", max_length=60)
    profile = models.CharField("profil", max_length=60)
    weight = models.CharField("masse (grains)", max_length=60)

    def __str__(self):
        return f"{self.brand} - {self.profile} - {self.weight}"

    class Meta:
        verbose_name = "Pointe"
        verbose_name_plural = "Pointes"


class Tube(models.Model):
    user = models.ForeignKey(
        "accounts.User", related_name="alternative_tubes", on_delete=models.CASCADE
    )
    TUBE_MATERIAL_CHOICES = [
        ("CARBON", "carbone"),
        ("ALU", "aluminium"),
        ("WOOD", "bois"),
    ]

    brand = models.CharField("marque", max_length=60)
    material = models.CharField(
        "matériau",
        max_length=10,
        choices=TUBE_MATERIAL_CHOICES,
        default=TUBE_MATERIAL_CHOICES[0],
    )
    tube_length = models.FloatField("longueur")
    spine = models.FloatField("flèche/spine")
    tube_diameter = models.FloatField("diametre exterieur")

    def __str__(self):
        return f"{self.brand} - {self.material} - {self.spine} - {self.tube_length}"

    class Meta:
        verbose_name = "Tube"
        verbose_name_plural = "Tubes"


class Arrow(models.Model):
    user = models.ForeignKey(
        "accounts.User", related_name="alternative_arrows", on_delete=models.CASCADE
    )
    nock = models.ForeignKey("equipment.Nock", on_delete=models.CASCADE)
    feathering = models.ForeignKey("equipment.Feathering", on_delete=models.CASCADE)
    tip = models.ForeignKey("equipment.Tip", on_delete=models.CASCADE)
    tube = models.ForeignKey("equipment.Tube", on_delete=models.CASCADE)
    not_broken = models.BooleanField("en état d'utilisation", default=True)

    def __str__(self):
        return (
            f"{self.id}: {self.tube.brand} - "
            f"{self.feathering.cock_color}/{self.feathering.color} - {self.tube.tube_length}"
        )

    class Meta:
        verbose_name = "Flèche"
        verbose_name_plural = "Flèches"
