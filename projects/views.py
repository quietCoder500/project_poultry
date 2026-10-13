from dataclasses import dataclass

from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from projects.forms import ProjectForm
from projects.models import Animal, Project


@dataclass
class ProjectWithForms:
    project: Project
    edit_form: ProjectForm

    @classmethod
    def from_project(cls, project):
        return cls(project=project, edit_form=ProjectForm(instance=project))


# Create your views here.
def projects_list(request):
    projects = get_list_or_404(Project, user=request.user)
    context = {
        "projects": [ProjectWithForms.from_project(project) for project in projects]
    }

    return render(request, "projects/projects_list.html", context=context)


@require_POST
def project_delete(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug, user=request.user)

    project.delete()

    return redirect("projects:projects-list")


def animals_list(request, project_slug):
    project = get_object_or_404(
        Project, slug=project_slug, user=request.user, is_livestock=True
    )
    animals = get_list_or_404(Animal, project=project)

    context = {"animals": animals, "project": project}

    return render(request, "projects/animals_list.html", context=context)
