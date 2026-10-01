from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    # each path here inherits a project slug attribute from the root urls.
    path("list", views.projects_list, name="projects-list")
]
