# Generated by Django 5.0.4 on 2024-04-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Clients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("joining_data", models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name="payments",
            old_name="Integer",
            new_name="status",
        ),
    ]