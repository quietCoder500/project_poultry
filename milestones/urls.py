from django.urls import path

from . import views

app_name = "milestones"

urlpatterns = [path("", views.index, name="index")]
