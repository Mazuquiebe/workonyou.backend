from django.urls import path
from .views import SuggestedDietView


urlpatterns = [
    path('suggested_diet/', SuggestedDietView.as_view()),

]