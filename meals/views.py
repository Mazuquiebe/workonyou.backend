from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import MealSerializer
from .models import Meal


class MealView(ListCreateAPIView, 
               RetrieveUpdateDestroyAPIView):

    serializer_class = MealSerializer
    queryset         = Meal.objects.all()
    lookup_url_kwarg = 'meal_id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)