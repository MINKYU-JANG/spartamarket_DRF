from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListAPIView.as_view()),
    path('create/', views.ProductCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductPutDeleteAPIView.as_view()),
]
