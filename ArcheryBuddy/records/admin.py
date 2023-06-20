from django.contrib import admin
from .models import (
    PracticeRecordSession,
    PracticeRecord,
    StatsRecordSession,
    StatsRecord,
)


@admin.register(PracticeRecordSession)
class PracticeRecordSessionAdmin(admin.ModelAdmin):
    pass


@admin.register(PracticeRecord)
class PracticeRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(StatsRecordSession)
class StatsRecordSessionAdmin(admin.ModelAdmin):
    pass


@admin.register(StatsRecord)
class StatsRecordAdmin(admin.ModelAdmin):
    pass
