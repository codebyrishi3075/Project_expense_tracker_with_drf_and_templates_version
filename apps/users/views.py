from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm
from services.user_service import authenticate_user


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard-home")
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})


from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate_user(username, password)

        if user:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("dashboard-home")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")