# Generated by Django 4.1.1 on 2022-10-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exercises", "0002_alter_exercise_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exercise",
            name="duration",
            field=models.DurationField(),
        ),
    ]
