from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    # each path here inherits a project slug attribute from the root urls.
    path("", views.projects_list, name="projects-list"),
    path("<slug:project_slug>", views.animals_list, name="animals-list"),
    path("<slug:project_slug>/delete", views.project_delete, name="project-delete"),
    path("<slug:project_slug>/edit", views.project_edit, name="project-edit"),
    path("<slug:project_slug>/<uuid:public_id>/delete", views.animal_delete, name="animal-delete"),
    path("<slug:project_slug>/<uuid:public_id>/edit", views.animal_edit, name="animal-edit"),
]
