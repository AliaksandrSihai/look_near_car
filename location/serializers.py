from rest_framework.serializers import ModelSerializer

from location.models import LocationModel


class LocationModelSerializer(ModelSerializer):
    """Сериалайзер для модели пользователя"""

    class Meta:
        model = LocationModel
        fields = "__all__"


class LocationShortSerializer(ModelSerializer):
    class Meta:
        model = LocationModel
        fields = ("zip", "city")
