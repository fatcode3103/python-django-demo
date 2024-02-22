from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    role_id = models.IntegerField(null=True)


class Role(models.Model):
    name = models.CharField(max_length=255)


class Permission(models.Model):
    name = models.CharField(max_length=255)


class GroupPermission(models.Model):
    role_id = models.IntegerField()
    permission_id = models.IntegerField()
