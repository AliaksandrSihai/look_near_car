from rest_framework import viewsets

from cargo.paginators import ListPaginator
from location.models import LocationModel
from location.serializers import LocationModelSerializer


class LocationViewset(viewsets.ModelViewSet):
    """Представление для модели LocationModel"""

    serializer_class = LocationModelSerializer
    queryset = LocationModel.objects.all()
    pagination_class = ListPaginator
