from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import ActivitySerializer
from .models import Activity


class ActivityView(ListCreateAPIView, 
                   RetrieveUpdateDestroyAPIView):

    serializer_class = ActivitySerializer
    queryset         = Activity

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)