from django.urls import path
from .views import FoodView


urlpatterns = (
   path("foods/", FoodView.as_view()),
   path("foods/<pk>/", FoodView.as_view()),
   path("foods/<str:name>/", FoodView.as_view()),
)