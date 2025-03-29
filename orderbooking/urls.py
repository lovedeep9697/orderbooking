"""
URL configuration for orderbooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
import orderbooking.views


router = routers.DefaultRouter()
router.register(r"users", orderbooking.views.UserViewSet)
router.register(r"groups", orderbooking.views.GroupViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    # Using the default TokenObtainPairView and TokenRefreshView for tokens.
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # End point to create new user.
    path(
        "api/users/register/",
        orderbooking.views.CreateUserView.as_view(),
        name="register_user",
    ),
    # All endpoint from OrderBook app.
    path("api/orderbook/", include("orderbook.urls")),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
