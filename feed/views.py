from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import FoodSerializer
from .models import Food 


class FoodView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):

    serializer_class = FoodSerializer
    queryset         = Food.objects.all()

    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated]

