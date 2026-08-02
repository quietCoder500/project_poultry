from django.db import models
from django.contrib.auth import get_user_model
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
