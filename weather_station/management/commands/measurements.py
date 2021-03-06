from django.core.management.base import BaseCommand

from weather_station.models import Measurement
from weather_station.measurements_devices import collect_data


class Command(BaseCommand):
    help = "Collect data from devices"

    def handle(self, *args, **kwargs):
        while True:
            data = collect_data.get_data()
            measurement = Measurement(**data)
            measurement.full_clean()
            measurement.save()
