# Generated by Django 5.0.2 on 2024-02-23 02:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0002_alter_user_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role_with_user",
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.PROTECT, to="crud.role"
            ),
        ),
    ]
