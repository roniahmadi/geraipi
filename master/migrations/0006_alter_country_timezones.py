# Generated by Django 4.1.2 on 2024-03-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("master", "0005_alter_country_region_id_alter_country_subregion_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="country",
            name="timezones",
            field=models.TextField(default=[]),
        ),
    ]