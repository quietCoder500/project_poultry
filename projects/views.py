from django.shortcuts import get_list_or_404, get_object_or_404, render

from projects.models import Animal, Project


# Create your views here.
def projects_list(request):
    projects = get_list_or_404(Project, user=request.user)

    context = {"projects": projects}

    return render(request, "projects/projects_list.html", context=context)


def animals_list(request, project_slug):
    project = get_object_or_404(
        Project, slug=project_slug, user=request.user, is_livestock=True
    )
    animals = get_list_or_404(Animal, project=project)

    context = {"animals": animals, "project": project}

    return render(request, "projects/animals_list.html", context=context)


def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug, user=request.user)
    context = {"project"}
