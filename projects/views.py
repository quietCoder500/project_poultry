from django.shortcuts import get_list_or_404, get_object_or_404, render

from projects.forms import ProjectForm
from projects.models import Animal, Project


class ProjectWithForms:
    def __init__(self, project: Project) -> None:
        self.title = project.title
        self.slug = project.slug

        self.created_at = project.created_at
        self.updated_at = project.updated_at

        self.is_livestock = project.is_livestock
        self.is_completed = project.is_completed

    edit_form: ProjectForm


# Create your views here.
def projects_list(request):
    projects = get_list_or_404(Project, user=request.user)

    projects_with_forms = []
    for project in projects:
        new_project = ProjectWithForms(project)
        new_project.edit_form = ProjectForm(instance=project)

        projects_with_forms.append(new_project)

    context = {"projects": projects_with_forms}

    return render(request, "projects/projects_list.html", context=context)


def animals_list(request, project_slug):
    project = get_object_or_404(
        Project, slug=project_slug, user=request.user, is_livestock=True
    )
    animals = get_list_or_404(Animal, project=project)

    context = {"animals": animals, "project": project}

    return render(request, "projects/animals_list.html", context=context)
