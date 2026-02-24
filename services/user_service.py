from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


def register_user(data):
    user = User.objects.create_user(
        username=data.get("username"),
        email=data.get("email"),
        password=data.get("password"),
    )
    return user


def authenticate_user(username, password):
    return authenticate(username=username, password=password)