from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    # each path here inherits a project slug attribute from the root urls.
    path("", views.projects_list, name="projects-list"),
    path("<slug:project_slug>", views.animals_list, name="animals-list"),
]
