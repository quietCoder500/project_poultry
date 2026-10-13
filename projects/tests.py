from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from projects.models import Animal, Project


# Create your tests here.
class ProjectsListViewTests(TestCase):
    def test_post_creates_project_for_authenticated_user(self):
        user = get_user_model().objects.create_user(
            email="projects@example.com", password="test-password"
        )  # type: ignore
        self.client.force_login(user)

        response = self.client.post(
            reverse("projects:projects-list"),
            {
                "title": "My Project",
                "started_at": "2026-10-13",
                "is_livestock": "on",
            },
        )

        self.assertEqual(response.status_code, 200)
        project = Project.objects.get(title="My Project")
        self.assertEqual(project.user, user)


class ProjectModelTests(TestCase):
    def setUp(self):
        self.test_user = get_user_model().objects.create_user(
            email="email@email.com", password="pass"
        )  # type: ignore

    def test_create_project(self):
        project_name = "My Livestock project"
        project_one = Project.objects.create(
            title=project_name, user=self.test_user, is_livestock=True
        )
        self.assertEqual(project_one.title, project_name)
        self.assertEqual(project_one.slug, slugify(project_name))
        self.assertTrue(project_one.is_livestock)
        self.assertIsNotNone(project_one.created_at)
        self.assertFalse(project_one.is_completed)

        project_two = Project.objects.create(
            title="A Still Project", user=self.test_user
        )
        self.assertFalse(project_two.is_livestock)

        project_three = Project.objects.create(
            title=project_name, user=self.test_user, is_livestock=True
        )
        self.assertEqual(project_three.title, project_name + " (1)")
        self.assertEqual(project_three.slug, slugify(project_name) + "_1")


class AnimalModelTests(TestCase):
    def setUp(self):
        self.test_user = get_user_model().objects.create_user(
            email="email@email.com", password="pass"
        )  # type: ignore
        self.test_livestock_project = Project.objects.create(
            title="My Project", user=self.test_user, is_livestock=True
        )
        self.test_still_project = Project.objects.create(
            title="My still project", user=self.test_user, is_livestock=False
        )

    def test_create_animal(self):
        animal_one = Animal.objects.create(
            project=self.test_livestock_project,
            common_name="CHK",
            breed="Brahma",
        )
        self.assertEqual(animal_one.name, "Exhibition Chicken - Brahma")
        self.assertIsNone(animal_one.name_override)
        self.assertFalse(animal_one.is_market)

        animal_two = Animal.objects.create(
            project=self.test_livestock_project,
            common_name="CHK",
            breed="Cornish Cross",
            is_market=True,
        )
        self.assertTrue(animal_two.is_market)

        with self.assertRaises(ValueError):
            animal_three = Animal.objects.create(
                project=self.test_still_project,
                common_name="CHK",
                breed="Cornish Cross",
                is_market=True,
            )
