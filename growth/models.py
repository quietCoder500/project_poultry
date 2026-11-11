from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from projects.models import Animal, Project


class MetricDefinition(models.Model):
    class DataType(models.TextChoices):
        FLOAT = "float", "Numeric (Decimal)"
        INT = "int", "Numeric (Integer)"
        TEXT = "text", "Text / Notes"
        CHOICE = "choice", "Categorical Choice"

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    unit_of_measurement = models.CharField(max_length=20, blank=True)
    data_type = models.CharField(
        max_length=10, choices=DataType.choices, default=DataType.FLOAT
    )

    livestock_only = models.BooleanField(default=True)
    is_global = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Null if global, user-created if specific to a member or club",
    )

    description = models.TextField(blank=True)


class DataPoint(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="datapoints"
    )
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name="datapoints",
        null=True,
        blank=True,
    )
    metric = models.ForeignKey(
        MetricDefinition, on_delete=models.CASCADE, related_name="datapoints"
    )

    numeric_value = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        null=True,
        blank=True,
    )
    text_value = models.TextField(null=True, blank=True)

    timestamp = models.DateTimeField(default=timezone.now)
    notes = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional context (e.g. 'Weighed before morning feeding')",
    )

    class Meta:
        indexes = (
            models.Index(
                fields=(
                    "project",
                    "animal",
                    "metric",
                    "timestamp",
                )
            ),
        )
        ordering = ("timestamp",)

    def __str__(self):
        val = self.numeric_value if self.numeric_value is not None else self.text_value
        return f"{self.timestamp.strftime('%b %d')} - {self.metric.name}: {val} {self.metric.unit_of_measurement}"


class DashboardCard(models.Model):
    class CardType(models.TextChoices):
        LINE_CHART = "line_chart", "Line Chart"
        STAT_BADGE = "stat_badge", "Statistic Badge (Latest value)"
        MARKDOWN = "markdown", "Text Card"

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    card_type = models.CharField(
        max_length=20, choices=CardType, default=CardType.LINE_CHART
    )
    title = models.CharField("Card Name", max_length=100)
    order = models.DecimalField(max_digits=10, decimal_places=5, default=Decimal("1.0"))

    class Meta:
        ordering = ("order",)
