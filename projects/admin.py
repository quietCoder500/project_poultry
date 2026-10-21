from django.contrib import admin

from projects.models import Animal, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "user",
        "created_at",
        "updated_at",
        "is_livestock",
        "is_completed",
        "started_at",
        "completed_at",
    )
    list_display_links = ("title", "user")
    list_filter = (
        "is_livestock",
        "is_completed",
        "started_at",
        ("user", admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ("title", "slug", "user__email")
    date_hierarchy = "created_at"
    ordering = ("-updated_at",)
    list_select_related = ("user",)
    list_per_page = 50
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Project",
            {
                "fields": ("title", "slug", "user"),
            },
        ),
        (
            "Status and dates",
            {
                "fields": (
                    ("is_livestock", "is_completed"),
                    ("started_at", "completed_at"),
                ),
            },
        ),
        (
            "Record keeping",
            {
                "classes": ("collapse",),
                "fields": ("created_at", "updated_at"),
            },
        ),
    )


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        "public_id",
        "project",
        "created_at",
        "updated_at",
        "common_name",
        "breed",
        "is_market",
        "name",
        "name_override",
    )
    list_display_links = ("public_id", "name")
    list_filter = (
        "common_name",
        "is_market",
        ("project", admin.RelatedOnlyFieldListFilter),
    )
    search_fields = (
        "=public_id",
        "name",
        "name_override",
        "breed",
        "project__title",
        "project__slug",
        "project__user__email",
    )
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    list_select_related = ("project", "project__user")
    autocomplete_fields = ("project",)
    list_per_page = 50
    readonly_fields = ("public_id", "name", "created_at", "updated_at")
    fieldsets = (
        (
            "Animal",
            {
                "fields": ("public_id", "project", "name", "name_override"),
            },
        ),
        (
            "Classification",
            {
                "fields": (("common_name", "breed"), "is_market"),
            },
        ),
        (
            "Record keeping",
            {
                "classes": ("collapse",),
                "fields": ("created_at", "updated_at"),
            },
        ),
    )
