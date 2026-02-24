
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard/users/', permanent=False)),
    path('admin/', admin.site.urls),
    path("dashboard/users/", include("apps.users.urls")),




    # API URLs
    path("api/users/", include("api.users.urls")),
]
    
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
