from django.test import TestCase
from django.utils import timezone
from model_bakery import baker

from growth.models import WeightRecord, FeedRecord


# Create your tests here.
class WeightRecordModelTests(TestCase):
    def setUp(self):
        self.mock_animal = baker.make("projects.Animal", project__is_livestock=True)

    def test_custom_date_weight_record_model(self):
        time = timezone.now()
        record_one = WeightRecord.objects.create(
            animal=self.mock_animal,
            weight=45,  # oz
            recorded_at=time,
        )
        self.assertEqual(record_one.recorded_at, time)

    def test_automatic_date_weight_record_model(self):
        record_one = WeightRecord.objects.create(
            animal=self.mock_animal,
            weight=45,  # oz
        )
        self.assertIsNotNone(record_one.recorded_at)


class FeedRecordModelTests(TestCase):
    def setUp(self):
        self.mock_animal = baker.make("projects.Animal", project__is_livestock=True)

    def test_custom_date_weight_record_model(self):
        time = timezone.now()
        record_one = FeedRecord.objects.create(
            animal=self.mock_animal,
            feed_consumed=200,  # oz
            recorded_at=time,
        )
        self.assertEqual(record_one.recorded_at, time)

    def test_automatic_date_weight_record_model(self):
        record_one = FeedRecord.objects.create(
            animal=self.mock_animal,
            feed_consumed=200,  # oz
        )
        self.assertIsNotNone(record_one.recorded_at)
