from django.db import migrations
from django.db.models import F, Q


def remove_project_lifecycle_milestones(apps, schema_editor):
    MilestoneEvent = apps.get_model("milestones", "MilestoneEvent")
    database = schema_editor.connection.alias

    MilestoneEvent.objects.using(database).filter(description="").filter(
        Q(title="Project started", occurred_at=F("project__started_at"))
        | Q(title="Project completed", occurred_at=F("project__completed_at"))
    ).delete()


class Migration(migrations.Migration):
    dependencies = [  # noqa: RUF012
        ("milestones", "0001_initial"),
    ]

    operations = [  # noqa: RUF012
        migrations.RunPython(
            remove_project_lifecycle_milestones,
            migrations.RunPython.noop,
        ),
    ]
