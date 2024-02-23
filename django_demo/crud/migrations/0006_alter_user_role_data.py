# Generated by Django 5.0.2 on 2024-02-23 02:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0005_user_role_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role_data",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                to="crud.role",
            ),
        ),
    ]
