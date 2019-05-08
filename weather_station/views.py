from datetime import datetime, timedelta
from django.shortcuts import render

from .models import BasicMeasurement, WindMeasurement, RainMeasurement


def index(request):
    basic_measurement = BasicMeasurement.objects.last()
    wind_measurement = WindMeasurement.objects.last()
    time_threshold = datetime.now() - timedelta(hours=1)
    rain_measurements = RainMeasurement.objects.filter(
        created_at__gt=time_threshold
    ).order_by("created_at")
    context = {
        "humidity": basic_measurement.humidity,
        "pressure": basic_measurement.pressure,
        "temperature": basic_measurement.temperature,
        "lux": basic_measurement.lux,
        "uv_index": basic_measurement.uv_index,
        "uv_a": basic_measurement.uv_a,
        "uv_b": basic_measurement.uv_b,
        "wind_direction": wind_measurement.wind_direction,
        "wind_gust": wind_measurement.wind_gust,
        "wind_speed": wind_measurement.wind_speed,
        "rain_measurements": rain_measurements,
    }
    return render(request, "index.html", context=context)


def statistics(request):
    return render(request, "statistics.html", context={})


def temperature(request):
    time_threshold = datetime.now() - timedelta(hours=24)
    temperature_measurement = (
        BasicMeasurement.objects.filter(created_at__gt=time_threshold)
        .order_by("created_at")
        .values("temperature", "created_at")
    )
    return render(
        request, "temperature.html", context={"temperatures": temperature_measurement}
    )


def wind(request):
    from django.db.models import Avg

    time_threshold = datetime.now() - timedelta(hours=24)
    wind_measurement = WindMeasurement.objects.filter(
        created_at__gt=time_threshold
    ).order_by("created_at")
    wind_directions = []
    for wind_direction in WindMeasurement.WIND_DIRECTION_CHOICES:
        avg = wind_measurement.filter(wind_direction=wind_direction[0]).aggregate(
            Avg("wind_speed")
        )
        wind_directions.append(
            {"direction": wind_direction[1], "speed": avg["wind_speed__avg"] or 0}
        )
    return render(
        request,
        "wind.html",
        context={"wind": wind_measurement, "wind_directions": wind_directions},
    )

