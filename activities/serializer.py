from .models import Activity
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:

        model  = Activity
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
        ]

    
    def create(self, validated_data):
        return Activity.objects.create(**validated_data)


    def update(self, instance: Activity, validated_data: dict) -> Activity:
       
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance