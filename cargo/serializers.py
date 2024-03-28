from rest_framework import serializers

from cargo.models import CargoModels
from cars.models import CarsModel
from cars.serializers import CarsSerializer
from location.serializers import LocationShortSerializer
from location.service import calculate_distance


class CargoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoModels
        fields = "__all__"


class CargoListSerializer(serializers.ModelSerializer):
    pick_up_location = LocationShortSerializer()
    delivery_location = LocationShortSerializer()
    near_car_count = serializers.SerializerMethodField(read_only=True)

    def get_near_car_count(self, cargo):
        nearby_cars_count = 0
        max_distance = 450
        pick_up_location = (
            cargo.pick_up_location.latitude,
            cargo.pick_up_location.longitude,
        )

        all_cars = CarsModel.objects.all()
        for car in all_cars:
            car_location = (
                car.current_location.latitude,
                car.current_location.longitude,
            )
            distance_to_cargo_pick_up = calculate_distance(
                pick_up_location, car_location
            )
            if distance_to_cargo_pick_up < max_distance:
                nearby_cars_count += 1
        return nearby_cars_count

    class Meta:
        model = CargoModels
        fields = (
            "id",
            "weight",
            "description",
            "pick_up_location",
            "delivery_location",
            "near_car_count",
        )


class CargoRetrieveSerializer(serializers.ModelSerializer):
    pick_up_location = LocationShortSerializer()
    delivery_location = LocationShortSerializer()
    near_cars = serializers.SerializerMethodField(read_only=True)

    def get_near_cars(self, cargo):
        pick_up_location = (
            cargo.pick_up_location.latitude,
            cargo.pick_up_location.longitude,
        )
        min_distance = self.context.get("min_distance")
        max_distance = self.context.get("max_distance")

        nearby_cars = []

        all_cars = CarsModel.objects.all()
        for car in all_cars:
            car_location = (
                car.current_location.latitude,
                car.current_location.longitude,
            )
            distance_to_cargo_pick_up = calculate_distance(
                pick_up_location, car_location
            )
            if (min_distance is None or distance_to_cargo_pick_up >= min_distance) and (
                max_distance is None or distance_to_cargo_pick_up <= max_distance
            ):
                car_data = CarsSerializer(car).data
                car_data["distance_to_cargo_pick_up"] = distance_to_cargo_pick_up
                nearby_cars.append(car_data)

        return nearby_cars

    class Meta:
        model = CargoModels
        fields = (
            "id",
            "weight",
            "description",
            "pick_up_location",
            "delivery_location",
            "near_cars",
        )


class CargoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoModels
        fields = ("weight", "description")
