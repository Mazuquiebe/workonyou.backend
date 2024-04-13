from rest_framework import serializers
from .models import SuggestedDiet
import ipdb


class SuggestedDietSerializer(serializers.ModelSerializer):

    class Meta:

        model  = SuggestedDiet
        fields = [
            "id",
            "suggested_protein",
            "suggested_carb",
            "suggested_sat_fat",
            "suggested_unsat_fat",
            "suggested_water",
            "basal_metabolism",
        ]

        read_only_fields = [
            "id",
            "suggested_protein",
            "suggested_carb",
            "suggested_sat_fat",
            "suggested_unsat_fat",
            "suggested_water",
            "basal_metabolism",
        ]


    def create(self, validated_data:SuggestedDiet) -> SuggestedDiet:
        return SuggestedDiet.objects.create(**validated_data)


    def update(self, instance: SuggestedDiet, validated_data: dict) -> SuggestedDiet:
       
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance