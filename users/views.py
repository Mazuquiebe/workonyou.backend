from rest_framework.views import Request, Response, status
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializer import UserSerializer,SignUpSerializer
from .models import User
from utils.calculus import NutriCalculus
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView
import ipdb


class SignInUserView(generics.CreateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = self.request.data
    
        nutri_calculus = NutriCalculus(
            user['weight_kg'],
            user['height_cm'],
            user['age_yr'],
            user['sex']
        )

        suggested_diet = nutri_calculus.calculate_macro()
        serializer.save(suggested_diet=suggested_diet)
    

class UserView(generics.RetrieveUpdateDestroyAPIView):

    # authentication_classes = [JWTAuthentication]
    # permission_classes     = [IsAuthenticated]

    serializer_class = UserSerializer
    queryset         = User.objects.all()


    # def get_object(self):
    #     id = self.request.user.id
    #     user = get_object_or_404(User, id=id)
    #     return user


    def perform_update(self, serializer):
        serializer.save()


    # def perform_destroy(self, instance):
    #     instance.is_active = False
    #     instance.save()


class SignupView(TokenViewBase):

    serializer_class = SignUpSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status.HTTP_200_OK)