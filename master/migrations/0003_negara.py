# Generated by Django 4.1.2 on 2024-03-21 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("master", "0002_configurationwebsite_konfigurasi_firebase"),
    ]

    operations = [
        migrations.CreateModel(
            name="Negara",
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
                ("kode", models.CharField(max_length=50)),
                ("nama", models.CharField(max_length=100)),
            ],
        ),
    ]
