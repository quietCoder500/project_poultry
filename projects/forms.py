from django import forms

from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("title", "is_livestock", "started_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
