from django.db import models
from django.utils import timezone

from projects.models import Project


class MilestoneEvent(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="milestones"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    occurred_at = models.DateField(default=timezone.now)

    class Meta:
        ordering = ("occurred_at", "pk")
        verbose_name = "milestone"
        verbose_name_plural = "milestones"

    def __str__(self):
        return self.title
