from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/v1/user/", include("crud.urls")),
    path("admin/", admin.site.urls),
]
