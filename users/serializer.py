from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from suggested_diets.serializer import SuggestedDiet, SuggestedDietSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken

import ipdb


class UserSerializer(serializers.ModelSerializer):

    suggested_diet = SuggestedDietSerializer(read_only=True)

    class Meta:
        model  = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "is_active",
            "updated_at",
            "created_at",
            "weight_kg",
            "height_cm",
            "age_yr",
            "sex",
            "suggested_diet"
        ]

        read_only_fields = [
            "id", 
            "is_active",
            "updated_at", 
            "created_at",
            "suggested_diet",
        ]


        extra_kwargs = {
            "password":{
                "write_only": True
            },
            "email":{
                "validators": [
                    UniqueValidator(
                        queryset = User.objects.all(), 
                        message="Email already being used."
                    )
                ]
            },    
        }

        depth = 1


    def create(self, validated_data:dict) -> User:
        suggeted_diet = validated_data.pop('suggested_diet')
        user = User.objects.create_user(**validated_data)
        suggeted_diet = SuggestedDiet(user=user, **suggeted_diet)
        return user


    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            
            if  key == "password":
                instance.set_password(value)
                
            setattr(instance, key, value)

        instance.save()

        return instance



class SignUpSerializer(serializers.Serializer):

    email    = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    token_class = RefreshToken
    
    @classmethod
    def get_token(cls,user):
        token = cls.token_class.for_user(user)
        token['user_id'] = str(user.id)
        return token


    def validate(self, attrs):
        
        self.user = authenticate(
            email = attrs["email"],
            password = attrs["password"]
        )

        if not self.user:
            raise InvalidToken(detail="invalid credentials",code=401)

        refresh = self.get_token(self.user)
       
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return data