# Generated by Django 5.0.2 on 2024-02-23 02:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0004_remove_user_role_with_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role_data",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="role_data",
                to="crud.role",
            ),
        ),
    ]
