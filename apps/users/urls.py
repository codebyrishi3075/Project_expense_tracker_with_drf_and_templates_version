from django.urls import path
from django.http import HttpResponse
from .views import register_view, login_view, logout_view

def dashboard_home(request):
    return HttpResponse("Dashboard Coming Soon")

urlpatterns = [
    path("", dashboard_home, name="dashboard-home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]