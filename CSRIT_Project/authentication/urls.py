
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import UserProfileView
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                       TokenRefreshView,)
from . import views



urlpatterns = [
    # user urls
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),#userprofile
]