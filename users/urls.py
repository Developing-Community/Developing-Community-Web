from django.urls import path

from .views import (
    UserCreateAPIView,
    ProfileUpdateAPIView,
    ProfileRetrieveAPIView,
    reset_password_change)
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
app_name = "user"
urlpatterns = [
    path('auth/refresh_token/', refresh_jwt_token),
    path('auth/verify_token/', verify_jwt_token),
    path('auth/obtain_token/', obtain_jwt_token),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('profile/', ProfileRetrieveAPIView.as_view(), name='view-profile'),
    path('profile/<int:id>/update/', ProfileUpdateAPIView.as_view(), name='edit-profile'),
    path('reset-password/<key>/',reset_password_change,name="reset_password"),
]
