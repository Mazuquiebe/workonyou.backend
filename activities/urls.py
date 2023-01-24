from django.urls import path
from .views import ActivityView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = (
    path("activities/", ActivityView.as_view()),

)
