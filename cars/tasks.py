from celery import shared_task

from cars.models import CarsModel


@shared_task
def change_car_locations():
    all_cars = CarsModel.objects.all()
    for car in all_cars:
        car.change_location()
