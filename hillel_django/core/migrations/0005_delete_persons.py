# Generated by Django 5.1.5 on 2025-02-06 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_persons"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Persons",
        ),
    ]
