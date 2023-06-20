from django.contrib import admin
from .models.arrows import Arrow, Nock, Feathering, Tube, Tip
from .models.bows import (
    Riser,
    Limbs,
    EquipmentString,
    ArrowRest,
    BergerButton,
    Scope,
    Clicker,
    Stabilisation,
    Dampeners,
    Barebow,
    OlympicBow,
    CompoundBow,
    CompoundArrowRest,
    CompoundScope,
)


# Arrows
@admin.register(Arrow)
class ArrowAdmin(admin.ModelAdmin):
    pass


@admin.register(Nock)
class NockAdmin(admin.ModelAdmin):
    pass


@admin.register(Feathering)
class FeatheringAdmin(admin.ModelAdmin):
    pass


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    pass


@admin.register(Tube)
class TubeAdmin(admin.ModelAdmin):
    pass


# Bows
@admin.register(Riser)
class RiserAdmin(admin.ModelAdmin):
    pass


@admin.register(Limbs)
class LimbsAdmin(admin.ModelAdmin):
    pass


@admin.register(EquipmentString)
class StringAdmin(admin.ModelAdmin):
    pass


@admin.register(ArrowRest)
class ArrowRestAdmin(admin.ModelAdmin):
    pass


@admin.register(BergerButton)
class BererButtonAdmin(admin.ModelAdmin):
    pass


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass


@admin.register(Clicker)
class ClickerAdmin(admin.ModelAdmin):
    pass


@admin.register(Stabilisation)
class StabilisationAdmin(admin.ModelAdmin):
    pass


@admin.register(Dampeners)
class DampenersAdmin(admin.ModelAdmin):
    pass


@admin.register(Barebow)
class BarebowAdmin(admin.ModelAdmin):
    pass


@admin.register(OlympicBow)
class OlympicBowAdmin(admin.ModelAdmin):
    pass


@admin.register(CompoundBow)
class CompoundBowAdmin(admin.ModelAdmin):
    pass


@admin.register(CompoundArrowRest)
class CompoundArrowRestAdmin(admin.ModelAdmin):
    pass


@admin.register(CompoundScope)
class CompoundScopeAdmin(admin.ModelAdmin):
    pass
