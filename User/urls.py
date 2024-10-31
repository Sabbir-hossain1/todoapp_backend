from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from User.Views.UserModelView import UserModelViewSet
from User.Views.PasswordResetRequestView import PasswordResetRequestView
from User.Views.PasswordResetView import PasswordResetView

userRouter = DefaultRouter()
userRouter.register(r"users", UserModelViewSet, basename="users")


urlpatterns = [
    path("", include(userRouter.urls)),
    path(
        "login/", TokenObtainPairView.as_view(), name="token-obtain-pair"
    ),  # JWT login
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token-refresh"
    ),  # Refresh token
    path(
        "password-reset/",
        PasswordResetRequestView.as_view(),
        name="password_reset_request",
    ),
    path(
        "password-reset/confirm/",
        PasswordResetView.as_view(),
        name="password_reset_confirm",
    ),
]
