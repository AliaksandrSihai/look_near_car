import csv

from django.core.management import BaseCommand

from location.models import LocationModel


class Command(BaseCommand):
    """Класс для заполнения локаций"""

    def handle(self, *args, **options):
        with open("location/uszips.csv", newline="", encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                zip_code, lat, lng, city, state = row[0], row[1], row[2], row[3], row[5]
                location = LocationModel.objects.create(
                    city=city, state=state, zip=zip_code, latitude=lat, longitude=lng
                )
                location.save()
