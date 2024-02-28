# Generated by Django 4.1.2 on 2024-02-18 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContentTranslate",
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
                ("tag_data", models.CharField(blank=True, max_length=255, null=True)),
                ("tag_value", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Content Translate",
                "verbose_name_plural": "Content Translate",
            },
        ),
    ]
