# Generated by Django 5.0.2 on 2024-02-23 03:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0008_alter_user_role_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="role_id",
            new_name="role",
        ),
    ]
