from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "Roles"


class User(models.Model):
    name = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "Users"


class Permission(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "Permissions"


class GroupPermission(models.Model):
    role_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        db_table = "Group_Permissions"
