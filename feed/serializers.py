from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        
        model  = Food

        fields = [
            "name",
            "total_protein_g",
            "total_carb_g",
            "total_fat_g",
            "total_kcal",
            "quantity_g",
        ]

    def create(self, validated_data):
        return Food.objects.create(**validated_data)

    
    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance