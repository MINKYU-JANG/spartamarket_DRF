from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignupAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('<str:username>/', views.UserProfileAPIView.as_view()),
    # path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
    