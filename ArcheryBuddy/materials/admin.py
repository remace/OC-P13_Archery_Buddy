from django.contrib import admin
from materials.models import Arrow

class ArrowAdmin(admin.ModelAdmin):
    pass

admin.site.register(Arrow, ArrowAdmin)
