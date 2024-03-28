from django.contrib import admin

from cars.models import CarsModel


@admin.register(CarsModel)
class CarsModelAdmin(admin.ModelAdmin):
    """Регистрация модели Cars в админ панели"""

    list_display = ("number", "current_location", "load_capacity")
    list_filter = ("number", "current_location")
    ordering = ("load_capacity",)
