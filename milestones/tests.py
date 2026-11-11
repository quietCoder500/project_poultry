from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from milestones.models import MilestoneEvent
from projects.models import Project


class MilestoneEventModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="member@example.com", password="test-password"
        )
        self.project = Project.objects.create(title="Poultry project", user=self.user)

    def test_create_milestone_event(self):
        milestone = MilestoneEvent.objects.create(
            project=self.project,
            title="First eggs",
            description="The hens laid their first eggs.",
            occurred_at=date(2026, 3, 12),
        )

        self.assertEqual(milestone.project, self.project)
        self.assertEqual(str(milestone), "First eggs")

    def test_project_lifecycle_events_are_not_saved_as_milestones(self):
        self.project.is_completed = True
        self.project.save()
        self.project.title = "Updated poultry project"
        self.project.save()

        self.assertFalse(
            MilestoneEvent.objects.filter(
                project=self.project,
                title__in=("Project started", "Project completed"),
            ).exists()
        )


class MilestoneIndexTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="member@example.com", password="test-password"
        )
        self.project = Project.objects.create(title="Poultry project", user=self.user)
        self.client.force_login(self.user)

    def test_index_lists_project_milestones_in_date_order(self):
        MilestoneEvent.objects.create(
            project=self.project, title="Second event", occurred_at=date(2026, 4, 1)
        )
        MilestoneEvent.objects.create(
            project=self.project, title="First event", occurred_at=date(2026, 3, 12)
        )
        other_user = get_user_model().objects.create_user(
            email="other@example.com", password="test-password"
        )
        other_project = Project.objects.create(title="Other project", user=other_user)
        MilestoneEvent.objects.create(
            project=other_project, title="Private event", occurred_at=date(2026, 3, 1)
        )

        response = self.client.get(
            reverse("milestones:index", kwargs={"project_slug": self.project.slug})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First event")
        self.assertContains(response, "Second event")
        self.assertNotContains(response, "Private event")
        self.assertLess(
            response.content.index(b"First event"),
            response.content.index(b"Second event"),
        )
        self.assertEqual(
            response.content.count(b"timeline-start mb-10 md:text-end"), 2
        )
        self.assertEqual(response.content.count(b"timeline-end mb-10"), 1)

    def test_index_rejects_projects_owned_by_another_user(self):
        other_user = get_user_model().objects.create_user(
            email="other@example.com", password="test-password"
        )
        other_project = Project.objects.create(title="Other project", user=other_user)

        response = self.client.get(
            reverse("milestones:index", kwargs={"project_slug": other_project.slug})
        )

        self.assertEqual(response.status_code, 404)

    def test_index_generates_lifecycle_events_from_current_project_dates(self):
        self.project.started_at = date(2026, 3, 12)
        self.project.is_completed = True
        self.project.completed_at = date(2026, 4, 1)
        self.project.save()

        response = self.client.get(
            reverse("milestones:index", kwargs={"project_slug": self.project.slug})
        )

        self.assertContains(response, "Project started")
        self.assertContains(response, "March 12, 2026")
        self.assertContains(response, "Project completed")
        self.assertContains(response, "April 1, 2026")
        self.assertFalse(
            MilestoneEvent.objects.filter(
                project=self.project,
                title__in=("Project started", "Project completed"),
            ).exists()
        )

    def test_index_uses_updated_project_start_date(self):
        self.project.started_at = date(2026, 5, 5)
        self.project.save()

        response = self.client.get(
            reverse("milestones:index", kwargs={"project_slug": self.project.slug})
        )

        self.assertContains(response, "May 5, 2026")
