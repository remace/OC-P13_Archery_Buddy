from django import forms


class ArrowForm(forms.Form):
    # nock
    nock_brand = forms.CharField(label="marque", max_length=32)
    nock_color = forms.CharField(label="couleur", max_length=32)
    nock_size = forms.CharField(label="taille", max_length=32)
    uses_nock_pin = forms.BooleanField(
        label="utilise un pin-nock", initial=False, required=False
    )

    # feathering
    LATERALITY_CHOICES = [("R", "droitier"), ("L", "gaucher")]

    FEATHERING_TYPE_CHOICES = [
        ("VANES", "pennes"),
        ("SPINWINGS", "spin wings"),
        ("FEATHERS", "plumes"),
        ("FLUFLU", "flu-flu"),
    ]

    feathering_laterality = forms.ChoiceField(
        label="latéralité", choices=LATERALITY_CHOICES
    )
    feathering_type = forms.ChoiceField(label="type", choices=FEATHERING_TYPE_CHOICES)
    feathering_brand = forms.CharField(label="marque", max_length=32)
    feathering_color = forms.CharField(label="couleur", max_length=32)
    feathering_cock_color = forms.CharField(label="couleur coq", max_length=32)
    feathering_size = forms.CharField(label="taille", max_length=32)
    feathering_angle = forms.IntegerField(label="angle")
    feathering_to_nock_distance = forms.IntegerField(label="distance plumes-encoche")

    # tip
    tip_brand = forms.CharField(label="marque", max_length=32)
    tip_profile = forms.CharField(label="profil", max_length=32)
    tip_weight = forms.IntegerField(label="masse")

    # tube
    TUBE_MATERIAL_CHOICES = [
        ("CARBON", "carbone"),
        ("ALU", "aluminium"),
        ("WOOD", "bois"),
    ]
    tube_brand = forms.CharField(label="marque", max_length=32)
    tube_material = forms.ChoiceField(label="materiau", choices=TUBE_MATERIAL_CHOICES)
    tube_length = forms.FloatField(label="longueur")
    tube_spine = forms.IntegerField(label="spine")
    tube_diameter = forms.FloatField(label="diamètre exterieur")

    not_broken = forms.BooleanField(
        label="en état de voler", initial=False, required=False
    )

    number_of_arrows = forms.IntegerField(label="nombre de flèches à créer")
