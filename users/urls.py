from django.urls import path
from .views import UserView, SignInUserView, SignupView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path("signin/", SignInUserView.as_view()),
    path("users/", UserView.as_view()),
    path("users/<str:pk>/", UserView.as_view()),
    path("signup/", SignupView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
