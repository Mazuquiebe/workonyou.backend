from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import SuggestedDiet
from .serializer import SuggestedDietSerializer


class SuggestedDietView(ListCreateAPIView):

    serializer_class = SuggestedDietSerializer
    queryset         = SuggestedDiet.objects.all()


    # def perform_create(self, serializer):

    #     serializer.save(user_id=self.request.user.id)