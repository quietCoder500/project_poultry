from django.contrib import admin

from growth.models import DashboardCard, DataPoint, MetricDefinition


# Register your models here.
@admin.register(DataPoint)
class DataPointAdmin(admin.ModelAdmin):
    pass


@admin.register(DashboardCard)
class DashboardCardAdmin(admin.ModelAdmin):
    pass


@admin.register(MetricDefinition)
class MetricDefinitionAdmin(admin.ModelAdmin):
    pass
