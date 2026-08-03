from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Project(models.Model):
    """Model definition for Project."""

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    # for internal use only
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Project attributes
    is_livestock = models.BooleanField(default=False)  # can it have animals
    is_completed = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Project."""

        verbose_name = "project"
        verbose_name_plural = "projects"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = base_slug = slugify(self.title)
            unique_slug = self.slug
            i = 0
            while (
                    self.__class__.objects.filter(slug=unique_slug, user=self.user)
                            .exclude(pk=self.pk)
                            .exists()
            ):
                i += 1
                unique_slug = f"{base_slug}_{i}"
            self.slug = unique_slug
            if i > 0:
                self.title += f" ({i})"

        return super().save(*args, **kwargs)

    def __str__(self):
        pass


class Animal(models.Model):
    ANIMAL_COMMON_NAME_CHOICES = [
        ["CHK", "Chicken"],
        ["TKY", "Turkey"],
        ["DCK", "Duck"],
    ]

    project = models.ForeignKey(Project, on_delete=models.RESTRICT)

    # internal use only
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Animal genetics
    common_name = models.CharField(choices=ANIMAL_COMMON_NAME_CHOICES, max_length=3, blank=True, null=True)
    breed = models.CharField(max_length=255, null=True, blank=True)

    is_market = models.BooleanField(default=False)

    name = models.CharField(max_length=255)
    # is an override for animal display name
    name_override = models.CharField(null=True, blank=True)

    def generate_name(self):
        if self.name_override:
            return self.name_override
        show_type = "Market" if self.is_market else "Exhibition"

        return f"{show_type} {self.common_name} - {self.breed}"

    def save(self, *args, **kwargs):
        self.name = self.generate_name()
        if not self.project.is_livestock:
            raise ValueError(f"Project {self.project.title} is not a livestock project")
        return super().save(*args, **kwargs)
