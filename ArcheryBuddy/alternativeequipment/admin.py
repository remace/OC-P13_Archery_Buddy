from django.contrib import admin
from .models.arrows import Arrow,Nock,Feathering,Tip,Tube

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

