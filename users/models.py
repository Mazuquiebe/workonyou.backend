from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class SexChoices(models.TextChoices):

    M = "MALE"
    F = "FEMALE"


class User(AbstractUser):

    id         = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username   = models.CharField(max_length=80, unique=True)
    first_name = models.CharField(max_length=80, null=True)
    last_name  = models.CharField(max_length=80, null=True)
    password   = models.CharField(max_length=150)
    email      = models.EmailField(max_length=80, unique=True)
    is_active  = models.BooleanField(default=True) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    weight_kg  = models.DecimalField(max_digits=8,decimal_places=2)
    height_cm  = models.IntegerField()
    
    age_yr = models.IntegerField()
    sex    = models.CharField(max_length=10, choices=SexChoices.choices)

    # suggested_diet = models.OneToOneField('suggested_diets.SuggestedDiet',
    #                             related_name='user', 
    #                             )
    
    # meals      = models.OneToOneField('meals.Meal', on_delete=models.CASCADE)
    # activities = models.OneToOneField('activities.Activity', on_delete=models.CASCADE)
   
