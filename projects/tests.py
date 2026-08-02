from django.test import TestCase
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from projects.models import Project


# Create your tests here.
class ProjectModelTests(TestCase):
    def setUp(self):
        self.test_user = get_user_model().objects.create_user(
            email="email@email.com", password="pass"
        )  # type: ignore

    def test_create_project(self):
        PROJECT_NAME = "My Livestock project"
        project_one = Project.objects.create(
            title=PROJECT_NAME, user=self.test_user, is_livestock=True
        )
        self.assertEqual(project_one.title, PROJECT_NAME)
        self.assertEqual(project_one.slug, slugify(PROJECT_NAME))
        self.assertTrue(project_one.is_livestock)
        self.assertIsNotNone(project_one.created_at)
        self.assertFalse(project_one.is_completed)

        project_two = Project.objects.create(
            title="A Still Project", user=self.test_user
        )
        self.assertFalse(project_two.is_livestock)

        project_three = Project.objects.create(
            title=PROJECT_NAME, user=self.test_user, is_livestock=True
        )
        self.assertEqual(project_three.title, PROJECT_NAME + " (1)")
        self.assertEqual(project_three.slug, slugify(PROJECT_NAME) + "_1")
