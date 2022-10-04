from django.db import models
from accounts.models import User


class Bow(models.Model):

    LATERALITY_CHOICES = [("R", "droitier"), ("L", "gaucher")]

    STRING_MATERIAL_CHOICE = [
        ("8125", "8125"),
        ("DACRON", "Dacron"),
        ("FF", "Fast-Flight"),
        ("D75", "D75"),
        ("FS", "Flex Supra"),
    ]

    ARROW_REST_TYPE_CHOICE = [
        ("SM", "short, magnetic"),
        ("LM", "long, magnetic"),
        ("P", "plastic"),
    ]

    power = models.IntegerField("Puissance de l'arc")
    laterality = models.CharField(
        "latéralité",
        max_length=10,
        choices=LATERALITY_CHOICES,
        default=LATERALITY_CHOICES[0],
    )

    class Meta:
        abstract = True


class Riser(models.Model):
    user = models.ForeignKey(
        "accounts.User", related_name="Riser", on_delete=models.CASCADE
    )
    brand = models.CharField("Marque", max_length=30)
    size = models.IntegerField("Taille (in.)")
    color = models.CharField("Couleur", max_length=30)
    grip = models.CharField("grip", max_length=30)

    def __str__(self):
        return f"{self.brand} - {self.color}"

    class Meta:
        verbose_name = "poignée"
        verbose_name_plural = "poignées"


class Limbs(models.Model):
    user = models.ForeignKey(
        "accounts.User", related_name="Limbs", on_delete=models.CASCADE
    )
    brand = models.CharField("Marque", max_length=30)
    power = models.IntegerField("Puissance")
    size = models.IntegerField("taille (in.)")

    def __str__(self):
        return f"{self.brand}"

    class Meta:
        verbose_name = "Branche"
        verbose_name_plural = "Branches"


class EquipmentString(models.Model):
    user = models.ForeignKey(
        "accounts.User", related_name="String", on_delete=models.CASCADE
    )
    brand = models.CharField(max_length=30)
    material = models.CharField(
        max_length=10,
        choices=Bow.STRING_MATERIAL_CHOICE,
        default=Bow.STRING_MATERIAL_CHOICE[0],
    )
    number_of_strands = models.IntegerField("Nombre de brins")

    def __str__(self):
        return f"{self.brand} - {self.number_of_strands} brins"

    class Meta:
        verbose_name = "Corde"
        verbose_name_plural = "Cordes"


class ArrowRest(models.Model):
    user = models.ForeignKey(
        "accounts.User", related_name="ArrowRest", on_delete=models.CASCADE
    )
    brand = models.CharField(max_length=30)
    rest_type = models.CharField(
        max_length=2,
        choices=Bow.ARROW_REST_TYPE_CHOICE,
        default=Bow.ARROW_REST_TYPE_CHOICE[0],
    )

    def __str__(self):
        return f"{self.brand}: {self.rest_type}"

    class Meta:
        verbose_name = "Repose-Flèche"
        verbose_name_plural = "Repose-Flèche"


class BergerButton(models.Model):
    ser = models.ForeignKey(
        "accounts.User",
        related_name="BergerButton",
        on_delete=models.CASCADE,
    )
    brand = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    spring = models.CharField(
        max_length=30
    )  # should be on the bow model? one tuning per bow with a single Berger Button

    def __str__(self):
        return f"{self.brand} - {self.color}"

    class Meta:
        verbose_name = "Berger"
        verbose_name_plural = "Bergers"


class Scope(models.Model):
    user = models.ForeignKey(
        "accounts.User", related_name="Scope", on_delete=models.CASCADE
    )
    brand = models.CharField(max_length=30)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "Viseur"
        verbose_name_plural = "Viseurs"


class Clicker(models.Model):
    user = models.ForeignKey(
        "accounts.User", related_name="Clicker", on_delete=models.CASCADE
    )
    brand = models.CharField(max_length=30)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "Clicker"
        verbose_name_plural = "Clickers"


class Stabilisation(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        related_name="Stabilisation",
        on_delete=models.CASCADE,
    )
    brand = models.CharField(max_length=30)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "Stabilisation"
        verbose_name_plural = "Stabilisations"


class Dampeners(models.Model):
    user = models.ForeignKey(
        "accounts.User", related_name="Dampeners", on_delete=models.CASCADE
    )
    front_brand = models.CharField(max_length=30)
    rears_brand = models.CharField(max_length=30)

    def __str__(self):
        return f"avant: {self.front_brand} arrières: {self.rears_brand}"

    class Meta:
        verbose_name = "Amortisseur"
        verbose_name_plural = "Amortisseurs"


class Barebow(Bow):
    user = models.ForeignKey(
        "accounts.User", related_name="Barebow", on_delete=models.CASCADE
    )
    riser = models.ForeignKey("equipment.Riser", on_delete=models.CASCADE)
    limbs = models.ForeignKey("equipment.Limbs", on_delete=models.CASCADE)
    string = models.ForeignKey(
        "equipment.EquipmentString", verbose_name="corde", on_delete=models.CASCADE
    )
    arrow_rest = models.ForeignKey(
        "equipment.ArrowRest", verbose_name="repose_flèche", on_delete=models.CASCADE
    )
    berger_button = models.ForeignKey(
        "equipment.BergerButton", verbose_name="Berger", on_delete=models.CASCADE
    )
    # tuning parameters... maybe should be in an association table
    number_of_turns = models.IntegerField()
    nockset_offset = models.FloatField()
    band = models.FloatField()
    high_tiller = models.FloatField()
    low_tiller = models.FloatField()

    class Meta:
        verbose_name = "Barebow"
        verbose_name_plural = "Barebows"

    def __str__(self):
        return f"{self.riser.brand} - {self.limbs.brand} {self.power}"


class OlympicBow(Bow):
    user = models.ForeignKey(
        "accounts.User", related_name="OlympicBow", on_delete=models.CASCADE
    )
    barebow = models.ForeignKey("equipment.Barebow", on_delete=models.CASCADE)
    scope = models.ForeignKey("equipment.Scope", on_delete=models.CASCADE)
    clicker = models.ForeignKey("equipment.Clicker", on_delete=models.CASCADE)
    stabilisation = models.ForeignKey(
        "equipment.stabilisation", on_delete=models.CASCADE
    )
    dampeners = models.ForeignKey("equipment.Dampeners", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.barebow.riser} - {self.barebow.limbs} - {self.power}"

    class Meta:
        verbose_name = "Arc Olympique"
        verbose_name_plural = "Arcs Olympiques"


class CompoundArrowRest(ArrowRest):
    ARROW_REST_TYPE_CHOICE = [
        ("B", "blade"),
        ("MB", "mobile blade"),
        ("A", "aiguille"),
        ("D", "Donuts"),
    ]

    def __str__(self):
        return f"{self.brand}: {self.rest_type}"

    class Meta:
        verbose_name = "Repose-Flèche (Compound)"
        verbose_name_plural = "Repose-Flèche (Compound)"


class CompoundScope(Scope):
    magnitude = models.FloatField(verbose_name="grossissement")

    def __str__(self):
        return f"{super.__str__()} - {self.magnitude}X"

    class Meta:
        verbose_name = "Viseur (Compound)"
        verbose_name_plural = "Viseurs (Compound)"


class CompoundBow(Bow):
    user = models.ForeignKey(
        "accounts.User", related_name="CompoundBow", on_delete=models.CASCADE
    )
    # general stuff
    bow_brand = models.CharField(max_length=30)
    bow_axle_to_axle = models.IntegerField()
    draw_weight = models.IntegerField()
    draw_weight_dropped = models.IntegerField()
    brace_height = models.FloatField()  # simili-band
    draw_length = models.FloatField()  # allonge

    arrow_rest = models.ForeignKey(
        "equipment.CompoundArrowRest",
        verbose_name="repose_flèche",
        on_delete=models.CASCADE,
    )
    stabilisation = models.ForeignKey(
        "equipment.Stabilisation",
        verbose_name="stabilisation",
        on_delete=models.CASCADE,
    )
    dampeners = models.ForeignKey("equipment.Dampeners", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand}"

    class Meta:
        verbose_name = "Arc à poulies"
        verbose_name_plural = "Arcs à poulies"
