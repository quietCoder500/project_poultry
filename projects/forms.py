from django import forms

from projects.models import Animal, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("title", "is_livestock", "started_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ("name_override", "is_market", "common_name", "breed", "project")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
