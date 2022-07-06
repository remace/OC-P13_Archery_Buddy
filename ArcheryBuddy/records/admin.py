from django.contrib import admin
from .models import *

@admin.register(PracticeRecordSession)
class PracticeRecordSessionAdmin(admin.ModelAdmin):
    pass

@admin.register(PracticeRecord)
class PracticeRecordAdmin(admin.ModelAdmin):
    pass
