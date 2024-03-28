from rest_framework import routers

from location.apps import LocationConfig
from location.views import LocationViewset

router = routers.DefaultRouter()
router.register(r"location", LocationViewset, basename="location")

app_name = LocationConfig.name

urlpatterns = [] + router.urls
