from django.db import models


# Create your models here.
class LocationModel(models.Model):
    """Модель локации"""

    city = models.CharField(max_length=255, verbose_name="город")
    state = models.CharField(max_length=255, verbose_name="штат")
    zip = models.CharField(max_length=255, verbose_name="почтовый индекс")
    latitude = models.CharField(max_length=255, verbose_name="широта")
    longitude = models.CharField(max_length=255, verbose_name="долгота")

    def __str__(self):
        return self.zip

    class Meta:
        verbose_name = "локация"
        verbose_name_plural = "локации"
