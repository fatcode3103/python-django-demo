from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.get_users, name="users"),
    path("add-user/", views.add_new_user, name="add-user"),
    path("delete-user/", views.delete_user, name="delete-user"),
    path("update-user/", views.update_user, name="update-user"),
    path("roles/", views.get_all_roles, name="roles"),
    path("add-role/", views.add_new_role, name="add-role"),
    path("delete-role/", views.delete_role, name="delete-role"),
    path("update-role/", views.update_role, name="update-role"),
    path("permissions/", views.get_all_permissions, name="permissions"),
    path("add-permission/", views.add_new_permission, name="add-permission"),
    path("delete-permission/", views.delete_permission, name="delete-permission"),
    path("update-permission/", views.update_permission, name="update-permission"),
]
