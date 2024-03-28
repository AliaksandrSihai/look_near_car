from rest_framework import generics

from cargo.paginators import ListPaginator
from cars.models import CarsModel
from cars.serializers import CarsSerializer, CarsUpdateSerializer


class CarsListAPIView(generics.ListAPIView):
    """Класс для просмотра всех созданных автомобилей"""

    serializer_class = CarsSerializer
    queryset = CarsModel.objects.all()
    pagination_class = ListPaginator


class CarsUpdateAPIView(generics.UpdateAPIView):
    """Класс для полного или частичного обновления созданных автомобилей"""

    serializer_class = CarsUpdateSerializer
    queryset = CarsModel.objects.all()
