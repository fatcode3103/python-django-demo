from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Permission, User, Role
from rest_framework.decorators import api_view
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer
from rest_framework import status


# user
@api_view(["GET"])
def get_users(request):
    try:
        users = User.objects.select_related("role").all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    except:
        return JsonResponse(
            {"message": "Error from the server"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def add_new_user(request):
    try:
        data_request = JSONParser().parse(request)
    except Exception as ex:
        return JsonResponse(
            {"message": f"Invalid JSON data: {ex}"}, status=status.HTTP_400_BAD_REQUEST
        )
    role = Role.objects.filter(id=data_request["role_id"]).first()
    user_data = {
        "name": data_request["name"],
        "role": role.id,
    }
    new_user_serializer = UserSerializer(data=user_data)
    if new_user_serializer.is_valid():
        new_user_serializer.save()
        return JsonResponse(new_user_serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(new_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_user(request):
    pk = request.query_params.get("pk", None)
    if pk is not None:
        try:
            user = User.objects.get(id=pk)
            user.delete()
            return JsonResponse(
                {"message": "Delete user successfully"}, status=status.HTTP_200_OK
            )
        except Exception as ex:
            return JsonResponse(
                {"message": f"User not found: {ex}"}, status=status.HTTP_404_NOT_FOUND
            )
    return JsonResponse(
        {"message": "Missing user id"}, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["PUT"])
def update_user(request):
    data_send = JSONParser().parse(request)
    pk = data_send["user_id"]
    data_new_user = {"name": data_send["name"], "role_id": data_send["role_id"]}
    if pk is not None:
        try:
            user = User.objects.get(id=pk)
            new_user_serializer = UserSerializer(user, data=data_new_user)
            if new_user_serializer.is_valid():
                new_user_serializer.save()
                return JsonResponse(
                    {"message": "Update user successfully"}, status=status.HTTP_200_OK
                )
            return JsonResponse(
                {"message": "Invalid user data"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as ex:
            return JsonResponse(
                {"message": f"User not found: {ex}"}, status=status.HTTP_404_NOT_FOUND
            )
    return JsonResponse(
        {"message": "Missing user id"}, status=status.HTTP_400_BAD_REQUEST
    )


# role
@api_view(["GET"])
def get_all_roles(request):
    try:
        obj = Role.objects.all()
        data = {"result": list(obj.values("name"))}
        return JsonResponse(data)
    except:
        return JsonResponse(
            {"message": "Error from the server"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def add_new_role(request):
    try:
        data_request = JSONParser().parse(request)
    except Exception as ex:
        return JsonResponse(
            {"message": f"Invalid JSON data: {ex}"}, status=status.HTTP_400_BAD_REQUEST
        )

    new_role_serializer = RoleSerializer(data=data_request)
    if new_role_serializer.is_valid():
        new_role_serializer.save()
        return JsonResponse(new_role_serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(new_role_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_role(request):
    pk = request.query_params.get("pk", None)
    if pk is not None:
        try:
            role = Role.objects.get(id=pk)
            role.delete()
            return JsonResponse(
                {"message": "Delete role successfully"}, status=status.HTTP_200_OK
            )
        except Exception as ex:
            return JsonResponse(
                {"message": f"Role not found: {ex}"}, status=status.HTTP_404_NOT_FOUND
            )
    return JsonResponse(
        {"message": "Missing role id"}, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["PUT"])
def update_role(request):
    data_send = JSONParser().parse(request)
    pk = data_send["role_id"]
    data_new_role = {"name": data_send["name"]}
    if pk is not None:
        try:
            role = Role.objects.get(id=pk)
            new_role_serializer = RoleSerializer(role, data=data_new_role)
            if new_role_serializer.is_valid():
                new_role_serializer.save()
                return JsonResponse(
                    {"message": "Update role successfully"}, status=status.HTTP_200_OK
                )
            return JsonResponse(
                {"message": "Invalid role data"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as ex:
            return JsonResponse(
                {"message": f"Role not found: {ex}"}, status=status.HTTP_404_NOT_FOUND
            )
    return JsonResponse(
        {"message": "Missing role id"}, status=status.HTTP_400_BAD_REQUEST
    )


# permission
@api_view(["GET"])
def get_all_permissions(request):
    try:
        obj = Permission.objects.all()
        data = {"result": list(obj.values("name"))}
        return JsonResponse(data)
    except:
        return JsonResponse(
            {"message": "Error from the server"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def add_new_permission(request):
    try:
        data_request = JSONParser().parse(request)
    except Exception as ex:
        return JsonResponse(
            {"message": f"Invalid JSON data: {ex}"}, status=status.HTTP_400_BAD_REQUEST
        )

    new_permission_serializer = PermissionSerializer(data=data_request)
    if new_permission_serializer.is_valid():
        new_permission_serializer.save()
        return JsonResponse(new_permission_serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(
        new_permission_serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["DELETE"])
def delete_permission(request):
    pk = request.query_params.get("pk", None)
    if pk is not None:
        try:
            permission = Permission.objects.get(id=pk)
            permission.delete()
            return JsonResponse(
                {"message": "Delete permission successfully"}, status=status.HTTP_200_OK
            )
        except Exception as ex:
            return JsonResponse(
                {"message": f"Permission not found: {ex}"},
                status=status.HTTP_404_NOT_FOUND,
            )
    return JsonResponse(
        {"message": "Missing permission id"}, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["PUT"])
def update_permission(request):
    data_send = JSONParser().parse(request)
    pk = data_send["permission_id"]
    data_new_permission = {"name": data_send["name"]}
    if pk is not None:
        try:
            permission = Permission.objects.get(id=pk)
            new_permission_serializer = PermissionSerializer(
                permission, data=data_new_permission
            )
            if new_permission_serializer.is_valid():
                new_permission_serializer.save()
                return JsonResponse(
                    {"message": "Update permission successfully"},
                    status=status.HTTP_200_OK,
                )
            return JsonResponse(
                {"message": "Invalid permission data"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as ex:
            return JsonResponse(
                {"message": f"Permission not found: {ex}"},
                status=status.HTTP_404_NOT_FOUND,
            )
    return JsonResponse(
        {"message": "Missing permission id"}, status=status.HTTP_400_BAD_REQUEST
    )
