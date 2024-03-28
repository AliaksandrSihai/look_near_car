from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from cargo.models import CargoModels
from cargo.paginators import ListPaginator
from cargo.serializers import (
    CargoCreateSerializer,
    CargoListSerializer,
    CargoRetrieveSerializer,
    CargoUpdateSerializer,
)


# Create your views here.
class CargoCreateAPIView(generics.CreateAPIView):
    """Класс для создания груза"""

    serializer_class = CargoCreateSerializer


class CargoListAPIView(generics.ListAPIView):
    """Класс для просмотра всех созданных грузов"""

    serializer_class = CargoListSerializer
    queryset = CargoModels.objects.all()
    pagination_class = ListPaginator
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("weight",)


class CargoRetrieveAPIView(generics.RetrieveAPIView):
    """Класс для просмотра одного созданного груза"""

    serializer_class = CargoRetrieveSerializer
    queryset = CargoModels.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        # Получаем параметры фильтрации из запроса и передаем их в контекст сериализатора
        min_distance = self.request.query_params.get("min_distance")
        max_distance = self.request.query_params.get("max_distance")
        if min_distance is not None:
            context["min_distance"] = float(min_distance)
        if max_distance is not None:
            context["max_distance"] = float(max_distance)
        return context


class CargoUpdateAPIView(generics.UpdateAPIView):
    """Класс для полного или частичного обновления созданных грузов"""

    serializer_class = CargoUpdateSerializer
    queryset = CargoModels.objects.all()


class CargoDestroyAPIView(generics.DestroyAPIView):
    """Класс для удаления созданных грузов"""

    queryset = CargoModels.objects.all()
