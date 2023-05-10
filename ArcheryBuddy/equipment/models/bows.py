from django.db import models
from django.db import IntegrityError
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
    user = models.ForeignKey(
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
        return f"{super().__str__()} - {self.magnitude}X"

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

    scope = models.ForeignKey(
        "equipment.CompoundScope", verbose_name="scope", on_delete=models.CASCADE
    )

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
        return f"{self.bow_brand}"

    class Meta:
        verbose_name = "Arc à poulies"
        verbose_name_plural = "Arcs à poulies"


class CompoundFactory:
    def create_bow(self, user, bow_attributes):
        user = user
        laterality = bow_attributes.get("laterality")
        power = bow_attributes.get("power")

        bow_brand = bow_attributes.get("bow_brand")
        entraxe = bow_attributes.get("entraxe")
        draw_weight = bow_attributes.get("compound_power")
        draw_weight_dropped = bow_attributes.get("reduced_power")
        brace_height = bow_attributes.get("compoundBand")
        draw_length = bow_attributes.get("drawLength")

        # scope
        scope_brand = bow_attributes.get("CompoundScopeBrand")
        magnitude = int(bow_attributes.get("ScopeMagnitude"))

        try:
            compound_scope = CompoundScope(
                magnitude=magnitude, user=user, brand=scope_brand
            )
            compound_scope.save()

        except IntegrityError as integrity:
            raise IntegrityError

        # arrow rest
        arrow_rest_brand = bow_attributes.get("CompoundRestBrand")
        arrow_rest_type = bow_attributes.get("CompoundRestType")
        try:
            arrow_rest = CompoundArrowRest(
                brand=arrow_rest_brand, rest_type=arrow_rest_type, user=user
            )
            arrow_rest.save()
        except IntegrityError as integrity:
            raise IntegrityError

        # stabilisation
        stabilisation_brand = bow_attributes.get("stab_brand")
        try:
            stabilisation = Stabilisation(user=user, brand=stabilisation_brand)
            stabilisation.save()
        except IntegrityError as integrity:
            raise IntegrityError

        # dampeners
        dampeners_front = bow_attributes.get("front_brand")
        dampeners_rears = bow_attributes.get("rears_brand")
        try:
            dampeners = Dampeners(
                user=user,
                front_brand=dampeners_front,
                rears_brand=dampeners_rears,
            )
            dampeners.save()
        except IntegrityError as integrity:
            raise IntegrityError

        try:
            bow = CompoundBow(
                user=user,
                power=power,
                laterality=laterality,
                bow_brand=bow_brand,
                bow_axle_to_axle=entraxe,
                draw_weight=draw_weight,
                draw_weight_dropped=draw_weight_dropped,
                brace_height=brace_height,
                draw_length=draw_length,
                scope=compound_scope,
                arrow_rest=arrow_rest,
                stabilisation=stabilisation,
                dampeners=dampeners,
            )
            bow.save()

        except IntegrityError as integrity:
            arrow_rest.delete()
            compound_scope.delete()
            stabilisation.delete()
            dampeners.delete()
            raise IntegrityError


class BarebowFactory:
    def create_bow(self, user, bow_attributes):
        # general
        bow_power = bow_attributes.get("power")
        laterality = bow_attributes.get("laterality")

        # riser
        riser_brand = bow_attributes.get("riser_brand")
        riser_size = bow_attributes.get("riser_size")
        riser_color = bow_attributes.get("riser_color")
        riser_grip = bow_attributes.get("riser_grip")

        try:
            riser = Riser(
                user=user,
                brand=riser_brand,
                size=riser_size,
                color=riser_color,
                grip=riser_grip,
            )
            riser.save()

        except IntegrityError as integrity:
            raise IntegrityError

        # limbs
        limbs_brand = bow_attributes.get("limbs_brand")
        limbs_power = bow_attributes.get("limbs_power")
        limbs_size = bow_attributes.get("limbs_size")

        try:
            limbs = Limbs(
                user=user,
                brand=limbs_brand,
                power=limbs_power,
                size=limbs_size,
            )
            limbs.save()

        except IntegrityError as integrity:
            raise IntegrityError

        # String
        string_brand = bow_attributes.get("string_brand")
        material = bow_attributes.get("material")
        strands = bow_attributes.get("strands")

        try:
            bow_string = EquipmentString(
                user=user,
                brand=string_brand,
                material=material,
                number_of_strands=strands,
            )
            bow_string.save()

        except IntegrityError as integrity:
            raise IntegrityError

        # Arrow Rest
        rest_type = bow_attributes.get("rest_type")
        rest_brand = bow_attributes.get("rest_brand")

        try:
            rest = ArrowRest(user=user, brand=rest_brand, rest_type=rest_type)
            rest.save()
        except IntegrityError as integrity:
            raise IntegrityError

        # Berger
        berger_brand = bow_attributes.get("berger_brand")
        berger_color = bow_attributes.get("berger_color")
        spring = bow_attributes.get("berger_spring")

        try:
            berger = BergerButton(
                user=user,
                brand=berger_brand,
                color=berger_color,
                spring=spring,
            )
            berger.save()

        except IntegrityError as integrity:
            raise IntegrityError

        string_turns = bow_attributes.get("string_turns")
        nockset_offset = bow_attributes.get("nockset_offset")
        band = bow_attributes.get("band")
        high_tiller = bow_attributes.get("high_tiller")
        low_tiller = bow_attributes.get("low_tiller")

        try:
            bow = Barebow(
                user=user,
                power=bow_power,
                laterality=laterality,
                riser=riser,
                limbs=limbs,
                string=bow_string,
                arrow_rest=rest,
                berger_button=berger,
                band=band,
                number_of_turns=string_turns,
                nockset_offset=nockset_offset,
                high_tiller=high_tiller,
                low_tiller=low_tiller,
            )
            bow.save()

        except IntegrityError as integrity:
            riser.delete()
            limbs.delete()
            bow_string.delete()
            rest.delete()
            berger.delete()
            raise IntegrityError


class OlympicBowFactory:
    def create_bow(self, user, bow_attributes):
        # general
        bow_power = bow_attributes.get("power")
        laterality = bow_attributes.get("laterality")

        # riser
        riser_brand = bow_attributes.get("riser_brand")
        riser_size = bow_attributes.get("riser_size")
        riser_color = bow_attributes.get("riser_color")
        riser_grip = bow_attributes.get("riser_grip")

        try:
            riser = Riser(
                user=user,
                brand=riser_brand,
                size=riser_size,
                color=riser_color,
                grip=riser_grip,
            )
            riser.save()

        except IntegrityError as integrity:
            raise IntegrityError

        # limbs
        limbs_brand = bow_attributes.get("limbs_brand")
        limbs_power = bow_attributes.get("limbs_power")
        limbs_size = bow_attributes.get("limbs_size")

        try:
            limbs = Limbs(
                user=user,
                brand=limbs_brand,
                power=limbs_power,
                size=limbs_size,
            )
            limbs.save()

        except IntegrityError as integrity:
            raise IntegrityError

        # String
        string_brand = bow_attributes.get("string_brand")
        material = bow_attributes.get("material")
        strands = bow_attributes.get("strands")

        try:
            bow_string = EquipmentString(
                user=user,
                brand=string_brand,
                material=material,
                number_of_strands=strands,
            )
            bow_string.save()

        except IntegrityError as integrity:
            raise IntegrityError

        # Arrow Rest
        rest_type = bow_attributes.get("rest_type")
        rest_brand = bow_attributes.get("rest_brand")

        try:
            rest = ArrowRest(user=user, brand=rest_brand, rest_type=rest_type)
            rest.save()
        except IntegrityError as integrity:
            raise IntegrityError

        # Berger
        berger_brand = bow_attributes.get("berger_brand")
        berger_color = bow_attributes.get("berger_color")
        spring = bow_attributes.get("berger_spring")

        try:
            berger = BergerButton(
                user=user,
                brand=berger_brand,
                color=berger_color,
                spring=spring,
            )
            berger.save()

        except IntegrityError as integrity:
            raise IntegrityError

        # scope
        scope_brand = bow_attributes.get("scope_brand")
        try:
            scope = Scope(user=user, brand=scope_brand)
            scope.save()
        except IntegrityError as integrity:
            raise IntegrityError

        # clicker
        clicker_brand = bow_attributes.get("scope_brand")
        try:
            clicker = Clicker(user=user, brand=clicker_brand)
            clicker.save()
        except IntegrityError as integrity:
            raise IntegrityError

        # stab
        stabilisation_brand = bow_attributes.get("stab_brand")
        try:
            stab = Stabilisation(user=user, brand=stabilisation_brand)
            stab.save()
        except IntegrityError as integrity:
            raise IntegrityError

        # dampeners
        dampeners_rears = bow_attributes.get("rears_brand")
        dampeners_front = bow_attributes.get("front_brand")
        try:
            dampeners = Dampeners(
                user=user,
                rears_brand=dampeners_rears,
                front_brand=dampeners_front,
            )
            dampeners.save()

        except IntegrityError as integrity:
            raise IntegrityError

        string_turns = bow_attributes.get("string_turns")
        nockset_offset = bow_attributes.get("nockset_offset")
        band = bow_attributes.get("band")
        high_tiller = bow_attributes.get("high_tiller")
        low_tiller = bow_attributes.get("low_tiller")

        try:
            barebow = Barebow(
                user=user,
                power=bow_power,
                laterality=laterality,
                riser=riser,
                limbs=limbs,
                string=bow_string,
                arrow_rest=rest,
                berger_button=berger,
                band=band,
                number_of_turns=string_turns,
                nockset_offset=nockset_offset,
                high_tiller=high_tiller,
                low_tiller=low_tiller,
            )
            barebow.save()

            bow = OlympicBow(
                user=user,
                barebow=barebow,
                power=bow_power,
                laterality=laterality,
                scope=scope,
                clicker=clicker,
                stabilisation=stab,
                dampeners=dampeners,
            )
            bow.save()

        except IntegrityError as integrity:
            riser.delete()
            limbs.delete()
            bow_string.delete()
            rest.delete()
            berger.delete()
            barebow.delete()
            scope.delete()
            stab.delete()
            clicker.delete()
            dampeners.delete()
            raise IntegrityError
