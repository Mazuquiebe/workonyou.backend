from django.urls import path
from .views import MealView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path("meals/", MealView.as_view()),
    path("meals/<meal_id>/", MealView.as_view()),
]
