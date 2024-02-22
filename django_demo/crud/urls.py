from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_users, name="users"),
    path("add-user/", views.add_new_user, name="add-user"),
    path("delete-user/", views.delete_user, name="delete-user"),
    path("update-user/", views.update_user, name="update-user"),
]
