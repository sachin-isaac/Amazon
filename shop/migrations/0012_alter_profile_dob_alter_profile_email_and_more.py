# Generated by Django 4.1 on 2023-05-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0011_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile", name="dob", field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="fname",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="lname",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="profile", name="phone", field=models.BigIntegerField(null=True),
        ),
    ]
