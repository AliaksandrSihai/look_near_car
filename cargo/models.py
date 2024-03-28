from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

import location.models


# # Create your models here.
class CargoModels(models.Model):
    """Модель груза"""

    pick_up_location = models.ForeignKey(
        to=location.models.LocationModel,
        verbose_name="локация pick-up",
        on_delete=models.CASCADE,
        related_name="pick_up_location",
    )
    delivery_location = models.ForeignKey(
        to=location.models.LocationModel,
        verbose_name="локация delivery",
        on_delete=models.CASCADE,
        related_name="delivery_location",
    )
    weight = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)], verbose_name="вес"
    )
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.pick_up_location} -> {self.delivery_location}"

    class Meta:
        verbose_name = "груз"
        verbose_name_plural = "груз"
