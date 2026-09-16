from django.urls import path

from . import views

app_name = "growth"

urlpatterns = [
    # each path here inherits a project slug attribute from the root urls.
    path("progress-report", views.progress_report_view, name="progress-report")
]
