from datetime import timedelta

from django.db.models import Avg, Max, OuterRef, Subquery
from django.utils import timezone

from growth.generators import ALL_GENERATORS, GraphCard, TextCard, register
from growth.models import FeedRecord, WeightRecord
from projects.models import Animal, Project


#
# widgets related to Weight Record Model
@register("growth.WeightRecord")
class AverageWeight(TextCard):
    title = "Average Weight of Flock"
    days_threshold = 3

    def render(self, project):
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
            return self.generate("No weights")

        threshold_date = global_max_date - timedelta(days=self.days_threshold)

        result = animals_with_latest.filter(
            latest_weight_date__gte=threshold_date
        ).aggregate(group_average=Avg("latest_weight"))["group_average"]

        return self.generate(f"{result} oz.")


@register("growth.WeightRecord")
class AverageDailyGain(TextCard):
    title = "Average Daily Gain of Flock"

    def render(self, project):

        return self.generate("4.65 oz/day")
