from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('paciente/<int:pk>/', views.pacienteDetail.as_view()),
    path('pacientecreate/', views.pacientecreate.as_view()),
    ]