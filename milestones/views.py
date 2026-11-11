from dataclasses import dataclass
from datetime import date, datetime, timedelta

from django.shortcuts import get_object_or_404, render

from milestones.models import MilestoneEvent
from projects.models import Project


@dataclass(frozen=True)
class TimelineEvent:
    title: str
    description: str
    days_since: int
    occurred_at: date


def _as_date(value):
    return value.date() if isinstance(value, datetime) else value

def _days_since(ref_date, event_date):
    return (event_date - ref_date).days

def index(request, project_slug):
    project = get_object_or_404(
        Project, slug=project_slug, user=request.user
    )
    events = [
        TimelineEvent(
            title=milestone.title,
            description=milestone.description,
            days_since=_days_since(_as_date(project.started_at), milestone.occurred_at),
            occurred_at=milestone.occurred_at,
        )
        for milestone in MilestoneEvent.objects.filter(project=project)
    ]
    events.append(
        TimelineEvent(
            title="Project started",
            description="",
            days_since=timedelta(0).days,
            occurred_at=_as_date(project.started_at),
        )
    )
    if project.is_completed and project.completed_at:
        events.append(
            TimelineEvent(
                title="Project completed",
                description="",
                days_since=_days_since(_as_date(project.started_at), _as_date(project.completed_at)),
                occurred_at=_as_date(project.completed_at),
            )
        )
    events.sort(key=lambda event: event.occurred_at)

    return render(
        request,
        "milestones/index.html",
        {"project": project, "milestones": events},
    )
