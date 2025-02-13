# Generated by Django 5.1.5 on 2025-02-06 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_delete_persons"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="person",
            table="users",
        ),
        migrations.CreateModel(
            name="Order",
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
                ("product_name", models.CharField(max_length=50)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.person"
                    ),
                ),
            ],
            options={
                "db_table": "orders",
            },
        ),
    ]
