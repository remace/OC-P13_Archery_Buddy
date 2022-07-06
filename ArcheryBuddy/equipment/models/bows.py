from django.db import models


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

    power = models.IntegerField()
    laterality = models.CharField(
        max_length=10, choices=LATERALITY_CHOICES, default=LATERALITY_CHOICES[0]
    )

    class Meta:
        abstract = True


class Barebow(Bow):
    user = models.ForeignKey(
        "accounts.User", related_name="Barebow", on_delete=models.CASCADE
    )
    # Poignée
    riser_brand = models.CharField(max_length=30)
    riser_size = models.IntegerField()

    # branches
    limbs_brand = models.CharField(max_length=30)
    limbs_size = models.IntegerField()
    # corde
    string_brand = models.CharField(max_length=30)
    string_material = models.CharField(
        max_length=10,
        choices=Bow.STRING_MATERIAL_CHOICE,
        default=Bow.STRING_MATERIAL_CHOICE[0],
    )
    string_number_of_strands = models.IntegerField()
    string_number_of_turns = models.IntegerField()
    nockset_offset = models.FloatField()
    band = models.FloatField()
    high_tiller = models.FloatField()
    low_tiller = models.FloatField()


class OlympicBow(Bow):
    user = models.ForeignKey(
        "accounts.User", related_name="Olympicbow", on_delete=models.CASCADE
    )
    # Poignée
    riser_brand = models.CharField(max_length=30)
    riser_size = models.IntegerField()

    # branches
    limbs_brand = models.CharField(max_length=30)
    limbs_size = models.IntegerField()
    # corde
    string_brand = models.CharField(max_length=30)
    string_material = models.CharField(
        max_length=10,
        choices=Bow.STRING_MATERIAL_CHOICE,
        default=Bow.STRING_MATERIAL_CHOICE[0],
    )
    string_number_of_strands = models.IntegerField()
    string_number_of_turns = models.IntegerField()
    nockset_offset = models.FloatField()
    band = models.FloatField()
    high_tiller = models.FloatField()
    low_tiller = models.FloatField()

    # viseur
    # plus tard: réglages du viseur selon distance
    scope_brand = models.CharField(max_length=30)

    # clicker
    clicker_brand = models.CharField(max_length=30)

    # repose_flèches
    arrow_rest_brand = models.CharField(max_length=30)
    arrow_rest_type = models.CharField(
        max_length=2,
        choices=Bow.ARROW_REST_TYPE_CHOICE,
        default=Bow.ARROW_REST_TYPE_CHOICE[0],
    )
    # berger_button
    berger_button_brand = models.CharField(max_length=30)
    berger_button_spring = models.CharField(max_length=30)
    # stabilisation
    stabilisation_brand = models.CharField(max_length=30)
    # amortisseurs de stabilisation
    dampeners = models.CharField(max_length=30)


class CompoundBow(Bow):

    ARROW_REST_TYPE_CHOICE = [
        ("B", "blade"),
        ("MB", "mobile blade"),
        ("A", "aiguille"),
        ("D", "Donuts"),
    ]

    # general stuff
    bow_brand = models.CharField(max_length=30)
    bow_axle_to_axle = models.IntegerField()
    draw_weight = models.IntegerField()
    draw_weight_dropped = models.IntegerField()
    brace_height = models.FloatField()  # simili-band
    draw_length = models.FloatField()  # allonge

    # Arrow Rest
    arrow_rest_brand = models.CharField(max_length=30)
    arrow_rest_type = models.CharField(
        max_length=2, choices=ARROW_REST_TYPE_CHOICE, default=ARROW_REST_TYPE_CHOICE[0]
    )
    # plus tard: entrer les réglage du repose flèche

    # scope
    scope_brand = models.CharField(max_length=30)
    scope_mag = models.FloatField()
    # plus tard: entrer les réglages du repose-flèches

    # stabilisation
    stabilisation_brand = models.CharField(max_length=30)
    # amortisseurs de stabilisation
    dampeners = models.CharField(max_length=30)
