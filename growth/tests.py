from django.test import TestCase
from django.utils import timezone
from model_bakery import baker

from growth import generators
from growth.models import FeedRecord, WeightRecord


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


class GeneratorRegistryTests(TestCase):
    def setUp(self):
        self.mock_project = baker.make("projects.Project", is_livestock=True)
        self.mock_animal = baker.make("projects.Animal", project=self.mock_project)

    def test_generator_registration(self):
        generators.ALL_GENERATORS = {}

        @generators.register("growth.WeightRecord")
        class Foo(generators.BaseTextCard):
            title = "Foo card"

            def render(self, *args, **kwargs):
                return self.generate("bar")

        self.assertIsNotNone(
            generators.ALL_GENERATORS["growth.WeightRecord"][0]().render(
                self.mock_project
            )
        )
