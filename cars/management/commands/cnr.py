from django.core.management.base import BaseCommand

from cars.models import CarsModel


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for _ in range(20):
            car = CarsModel.objects.create()
            car.save()
