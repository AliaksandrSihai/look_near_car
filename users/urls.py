from rest_framework import routers

from users.apps import UsersConfig
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet, basename="users")

app_name = UsersConfig.name

urlpatterns = [] + router.urls
