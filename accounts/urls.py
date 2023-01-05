from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

from .views import CustomTokenObtainPairView, LogoutView, LogoutAllView, UserRegistration, ForgatePasswordView, SavePasswordView, ResetPassword, SaveResetPassword

urlpatterns = [
    path('token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutView.as_view(), name='auth_logout'),
    path('logout-all-device', LogoutAllView.as_view(), name='auth_logout_all'),
    path('register-user', UserRegistration.as_view()),
    path('forgot-password', ForgatePasswordView.as_view()),
    path('save-password', SavePasswordView.as_view()),
    path('reset-password', ResetPassword.as_view()),
    path('save-reset-password', SaveResetPassword.as_view())
]