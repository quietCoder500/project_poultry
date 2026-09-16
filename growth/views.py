from dataclasses import dataclass

from django.shortcuts import get_object_or_404, render

from growth.generators import ALL_GENERATORS
from projects.models import Project


@dataclass(frozen=True)
class ReportCard:
    html: str
    title: str


@dataclass(frozen=True)
class ReportSection:
    title: str
    model: str
    children: list[ReportCard]


def progress_report_view(request, project_slug: str):
    project = get_object_or_404(Project, user=request.user, slug=project_slug)

    report_sections = []
    for model_name, cards in ALL_GENERATORS.items():
        current_section = ReportSection(
            title=model_name.split(".")[1], model=model_name, children=[]
        )
        for unrendered in cards:
            current_section.children.append(
                ReportCard(
                    html=unrendered.render(project=project), title=unrendered.title
                )
            )
        report_sections.append(current_section)

    context = {"report_sections": report_sections}

    return render(request, "growth/progress_report.html", context=context)
