from datetime import timedelta

from django.db.models.aggregates import Avg
from django.utils import timezone

from growth.generators import ALL_GENERATORS, GraphCard, TextCard, register
from growth.models import FeedRecord, WeightRecord


#
# widgets related to Weight Record Model
@register("growth.WeightRecord")
class AverageWeight(TextCard):
    title = "Average Weight of Flock"

    def render(self):
        since = timezone.now() - timedelta(days=7)
        result = WeightRecord.objects.filter(
            recorded_at__gte=since,
        ).aggregate(avg=Avg("weight"))
        return self.generate(f"{result} oz.")


@register("growth.WeightRecord")
class AverageDailyGain(TextCard):
    title = "Average Daily Gain of Flock"

    def render(self):

        return self.generate("4.65 oz/day")
