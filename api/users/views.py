from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.user_service import register_user


class RegisterAPIView(APIView):

    def post(self, request):
        user = register_user(request.data)
        return Response(
            {"message": "User created successfully"},
            status=status.HTTP_201_CREATED
        )