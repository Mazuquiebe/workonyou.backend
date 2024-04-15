from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from suggested_diets.serializer import SuggestedDiet, SuggestedDietSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from .exceptions import RequiredFields, InvalidCredentials
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
        SuggestedDiet.objects.create(user=user, **suggeted_diet)
        return user


    def update(self, instance: User, validated_data: dict) -> User:
        
        for key, value in validated_data.items():
            
            if  key == "password":
                instance.set_password(value)
                
            setattr(instance, key, value)

        instance.save()

        return instance


class SignUpSerializer(serializers.Serializer):

    token_class = RefreshToken

    email    = serializers.EmailField(write_only=True,default=None)
    username = serializers.CharField(write_only=True,default=None)
    password = serializers.CharField(write_only=True)
    
    @classmethod
    def get_token(cls,user):
        token = cls.token_class.for_user(user)
        token['user_id'] = str(user.id)
        return token


    def validate(self, attrs):
        
        email = attrs["email"]
        username = attrs["username"]
        password = attrs["password"]
        
        if not username and not email:
            raise RequiredFields
        
        self.user = authenticate(
            email    = email,
            username = username,
            password = password
        )

        if not self.user:
            raise InvalidCredentials

        refresh = self.get_token(self.user)
       
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return data