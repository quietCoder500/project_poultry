from datetime import timedelta

from django.db.models import Avg, Max, OuterRef, Subquery
from django.utils import timezone

from growth.generators import ALL_GENERATORS, BaseGraphCard, BaseTextCard, register
from growth.models import FeedRecord, WeightRecord
from projects.models import Animal, Project


#
# widgets related to Weight Record Model
@register("growth.WeightRecord")
class AverageWeight(BaseTextCard):
    title = "Average Weight of Flock"
    days_threshold = 3

    @classmethod
    def render(cls, project):
        """
        Generates the average weight of all the chickens. It discards weights older than a week and only uses the last weight from each bird
        """
        project_animals = Animal.objects.filter(project=project)

        latest_weight_records = WeightRecord.objects.filter(
            animal=OuterRef("pk")
        ).order_by("-recorded_at")

        animals_with_latest = project_animals.annotate(
            latest_weight_date=Subquery(
                latest_weight_records.values("recorded_at")[:1]
            ),
            latest_weight=Subquery(latest_weight_records.values("weight")[:1]),
        ).exclude(latest_weight_date__isnull=True)

        global_max_date = animals_with_latest.aggregate(
            global_max=Max("latest_weight_date")
        )["global_max"]

        if not global_max_date:
            return cls.generate("No weights")

        threshold_date = global_max_date - timedelta(days=cls.days_threshold)

        result = animals_with_latest.filter(
            latest_weight_date__gte=threshold_date
        ).aggregate(group_average=Avg("latest_weight"))["group_average"]

        return cls.generate(f"{result} oz.")


@register("growth.WeightRecord")
class AverageDailyGain(BaseTextCard):
    title = "Average Daily Gain of Flock"

    @classmethod
    def render(cls, project):

        return cls.generate("<float> oz/day")
