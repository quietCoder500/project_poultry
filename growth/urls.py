from django.urls import path

from . import views


app_name = "growth"

urlpatterns = [
    path("progress-report", views.progress_report_view, name="progress-report")
]
