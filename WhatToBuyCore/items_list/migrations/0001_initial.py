# Generated by Django 4.1.6 on 2023-02-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShoppingItem",
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
                (
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="Shopping list item name"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        max_length=30, verbose_name="Shopping list item description"
                    ),
                ),
                ("isCompleted", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ShoppingList",
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
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Shopping list name"),
                ),
            ],
        ),
    ]