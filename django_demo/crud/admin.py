from django.contrib import admin
from .models import User, Role, Permission, GroupPermission

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(GroupPermission)
