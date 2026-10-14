from dataclasses import dataclass

from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from projects.forms import AnimalForm, ProjectForm
from projects.models import Animal, Project


@dataclass
class ProjectWithForms:
    project: Project
    edit_form: ProjectForm

    @classmethod
    def from_project(cls, project):
        return cls(project=project, edit_form=ProjectForm(instance=project))

@dataclass
class AnimalWithForms:
    animal: Animal
    edit_form: AnimalForm

    @classmethod
    def from_animal(cls, animal):
        return cls(animal=animal, edit_form=AnimalForm(instance=animal))


# Create your views here.
def projects_list(request):
    project_form = ProjectForm()
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = request.user
            project.save()
            project_form = ProjectForm()

    projects = Project.objects.filter(user=request.user)
    context = {
        "projects": [ProjectWithForms.from_project(project) for project in projects],
        "project_form": project_form,
    }
    return render(request, "projects/projects_list.html", context=context)


@require_POST
def project_delete(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug, user=request.user)

    project.delete()

    return redirect("projects:projects-list")


@require_POST
def project_edit(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug, user=request.user)

    form = ProjectForm(request.POST, instance=project)

    if form.is_valid():
        try:
            form.save()
            messages.success(
                request,
                f"{form.cleaned_data.get('title', 'Project')} updated successfully",
            )
        except ValueError:
            messages.error(request, "Unable to save changes.")

    return redirect("projects:projects-list")


def animals_list(request, project_slug):
    project = get_object_or_404(
        Project, slug=project_slug, user=request.user, is_livestock=True
    )
    animals = get_list_or_404(Animal, project=project)

    context = {"animals": [AnimalWithForms.from_animal(animal) for animal in animals]}

    return render(request, "projects/animals_list.html", context=context)

@require_POST
def animal_delete(request, project_slug, public_id):
    animal = get_object_or_404(Animal, project__slug=project_slug, project__user=request.user, public_id=public_id)

    animal.delete()

    return redirect("projects:animals-list", project_slug=project_slug)


@require_POST
def animal_edit(request, project_slug, public_id):
    animal = get_object_or_404(Animal, project__slug=project_slug, project__user=request.user, public_id=public_id)

    form = AnimalForm(request.POST, instance=animal)

    if form.is_valid():
        try:
            form.save()
            messages.success(
                request,
                f"{form.cleaned_data.get('name', 'Animal')} updated successfully",
            )
        except ValueError:
            messages.error(request, "Unable to save changes.")

    return redirect("projects:animals-list", project_slug=project_slug)
