from django.contrib import admin

from .models import MilestoneEvent


@admin.register(MilestoneEvent)
class MilestoneEventAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "occurred_at")
    list_filter = ("occurred_at",)
    search_fields = ("title", "description", "project__title")
