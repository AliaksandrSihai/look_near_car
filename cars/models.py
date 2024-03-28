# Create your models here.
import random
import string

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from location.models import LocationModel


class CarsModel(models.Model):
    """Модель для машин"""

    number = models.CharField(
        max_length=5, unique=True, editable=False, verbose_name="уникальный номер"
    )
    current_location = models.ForeignKey(
        to=LocationModel,
        verbose_name="текущая локация",
        on_delete=models.SET_NULL,
        null=True,
    )
    load_capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        verbose_name="грузоподъемность",
    )

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "машина"
        verbose_name_plural = "машины"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.generate_unique_number()
        if not self.current_location:
            random_location = LocationModel.objects.order_by("?").first()
            self.current_location = random_location
        if not self.load_capacity:
            self.generate_load_capacity()
        super().save(*args, **kwargs)

    def generate_unique_number(self):
        number = random.randint(1000, 9999)
        letter = random.choice(string.ascii_uppercase)
        self.number = f"{number}{letter}"

    def generate_load_capacity(self):
        number = random.randint(1, 1000)
        self.load_capacity = number

    def change_location(self):
        random_location = LocationModel.objects.order_by("?").first()
        self.current_location = random_location
        self.save()
