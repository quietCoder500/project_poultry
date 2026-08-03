from django.db import models
from django.utils import timezone

from projects.models import Animal

import uuid


# Create your models here.
class WeightRecord(models.Model):
    record_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    animal = models.ForeignKey(Animal, on_delete=models.RESTRICT)
    weight = models.FloatField()

    # internal use only
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    recorded_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs) -> None:
        if self.recorded_at is None:
            self.recorded_at = (
                self.created_at if self.created_at is not None else timezone.now()
            )
        return super().save(*args, **kwargs)
