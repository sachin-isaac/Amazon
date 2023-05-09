# Generated by Django 4.1 on 2023-05-08 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0014_alter_profile_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Myaddress",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("address_head", models.CharField(max_length=20)),
                ("fname", models.CharField(max_length=20)),
                ("lname", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.BigIntegerField()),
                ("address", models.TextField()),
                ("landmark", models.CharField(max_length=40)),
                ("country", models.CharField(max_length=20)),
                ("state", models.CharField(max_length=20)),
                ("city", models.CharField(max_length=20)),
                ("pincode", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
