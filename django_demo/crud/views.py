from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework import status


@api_view(["GET"])
def get_users(request):
    obj = User.objects.all()
    data = {"result": list(obj.values("name", "role_id"))}
    return JsonResponse(data)


@api_view(["POST"])
def add_new_user(request):
    data_request = JSONParser().parse(request)
    new_user_serializer = UserSerializer(data=data_request)
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
