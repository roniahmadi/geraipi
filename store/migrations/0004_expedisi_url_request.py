# Generated by Django 4.1.2 on 2024-03-31 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_expedisi_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="expedisi",
            name="url_request",
            field=models.URLField(blank=True, null=True),
        ),
    ]
