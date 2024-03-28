from django.urls import path

from cars.apps import CarsConfig
from cars.views import CarsListAPIView, CarsUpdateAPIView

app_name = CarsConfig.name

urlpatterns = [
    path("cars_update/<int:pk>/", CarsUpdateAPIView.as_view(), name="cars_update"),
    path("cars_list/", CarsListAPIView.as_view(), name="cars_list"),
]
