from django.urls import path

from cargo.apps import CargoConfig
from cargo.views import (
    CargoCreateAPIView,
    CargoDestroyAPIView,
    CargoListAPIView,
    CargoRetrieveAPIView,
    CargoUpdateAPIView,
)

app_name = CargoConfig.name

urlpatterns = [
    path("cargo_create/", CargoCreateAPIView.as_view(), name="cargo_create"),
    path("cargo_update/<int:pk>/", CargoUpdateAPIView.as_view(), name="cargo_update"),
    path(
        "cargo_destroy/<int:pk>/", CargoDestroyAPIView.as_view(), name="cargo_destroy"
    ),
    path("cargo_list/", CargoListAPIView.as_view(), name="cargo_list"),
    path("cargo_view/<int:pk>/", CargoRetrieveAPIView.as_view(), name="cargo_view"),
]
