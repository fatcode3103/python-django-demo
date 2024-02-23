# Generated by Django 5.0.2 on 2024-02-23 03:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0006_alter_user_role_data"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="role_data",
        ),
        migrations.AlterModelTable(
            name="grouppermission",
            table="Group_Permissions",
        ),
        migrations.AlterModelTable(
            name="permission",
            table="Permissions",
        ),
        migrations.AlterModelTable(
            name="role",
            table="Roles",
        ),
        migrations.AlterModelTable(
            name="user",
            table="Users",
        ),
    ]