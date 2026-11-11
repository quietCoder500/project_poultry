from django.contrib import admin

from growth.models import DashboardCard, DataPoint, MetricDefinition


# Register your models here.
@admin.register(DataPoint)
class DataPointAdmin(admin.ModelAdmin):
    list_display = ("__str__", "metric", "project", "animal", "timestamp")
    list_display_links = ("project", "animal")
    list_filter = ("timestamp",)
    search_fields = ("project__user__email", "project__title", "animal__name")


@admin.register(DashboardCard)
class DashboardCardAdmin(admin.ModelAdmin):
    pass


@admin.register(MetricDefinition)
class MetricDefinitionAdmin(admin.ModelAdmin):
    list_display = (
        "is_global",
        "created_by",
    )
