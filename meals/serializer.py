from rest_framework import serializers
from .models import Meal


class MealSerializer(serializers.Serializer):

    class Meta:

        model  = Meal
        fields = [
            "user",
            "ingredients",
            "protein_grams",
            "carb_grams",
            "sat_fat_grams",
            "unsat_fat_grams",
            "total_kcal",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):

        ingredients = validated_data.pop('ingredients')

        meal = Meal.objects.create(**validated_data)

        meal.ingredients.set(ingredients)

        return meal


    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance