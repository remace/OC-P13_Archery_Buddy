from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = [
        "email",
        "first_name",
        "last_name",
    ]
    list_display = [
        "pseudo",
        "email",
        "first_name",
        "last_name",
    ]
    list_filter = ["is_admin", "is_active"]

    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    ("first_name", "last_name"),
                )
            },
        ),
        ("Permissions", {"fields": ("is_admin", "is_active")}),
        ("Time", {"fields": ("created_at", "updated_at")}),
    )

    add_fieldsets = (
        (
            None,
            {"fields": ("first_name", "last_name", "email", "password1", "password2")},
        ),
    )
    ordering = ("email",)
    filter_horizontal = ()
