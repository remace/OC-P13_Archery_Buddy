from django.contrib import admin
from equipment.models.arrows import Arrow
from equipment.models.bows import HuntingBow, Barebow, CompoundBow, OlympicBow

@admin.register(Arrow)
class ArrowAdmin(admin.ModelAdmin):
    search_fields = ['tube brand','feathering_color', 'feathering_color_cock','tip_brand',]
    list_display= [field.name for field in Arrow._meta.get_fields()]
    list_filter = ['tube_brand','feathering_color', 'feathering_cock_color',]
    


    fieldsets = (
        ("proprietaire", 
            {'fields': ('user', 'not_broken')}),
        ('encoche', 
            {'fields':('nock',)}),
        ("empennage",
            {"fields":
                ("feathering_brand",
                'feathering_color',
                'feathering_cock_color',
                'feathering_size',
                'feathering_angle',
                'feathering_nock_distance',    
            )}),
        ("pointe", {
            "fields":("tip_brand",
                "tip_weight",
                "tip_profile",
            )}),
        ("tube", 
            {"fields":(
                "tube_length",
                "tube_spine",
                "tube_diameter",
            )
        }),
    )



@admin.register(OlympicBow)
class BarebowAdmin(admin.ModelAdmin):
    
    pass

@admin.register(CompoundBow)
class CompoundBowAdmin(admin.ModelAdmin):
    pass

@admin.register(Barebow)
class BarebowAdmin(admin.ModelAdmin):
    pass

@admin.register(HuntingBow)
class HuntingBowAdmin(admin.ModelAdmin):
    pass