from rest_framework import serializers

from cars.models import CarsModel
from location.serializers import LocationShortSerializer


class CarsSerializer(serializers.ModelSerializer):
    current_location = LocationShortSerializer(read_only=True)

    class Meta:
        model = CarsModel
        fields = ("number", "current_location", "load_capacity")


class CarsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ("current_location",)
