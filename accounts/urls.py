from django.urls import path, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignupAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('<str:username>/', views.UserProfileAPIView.as_view()),
]
