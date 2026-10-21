from django import forms

from projects.models import Animal, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("title", "is_livestock", "started_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("title", "is_livestock", "started_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AnimalEditForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ("name_override", "is_market", "common_name", "breed", "project")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class AnimalCreateForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, required=True, initial=1)
    class Meta:
        model = Animal
        fields = ("name_override", "is_market", "common_name", "breed", "quantity")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
