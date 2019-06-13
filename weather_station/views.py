from datetime import datetime, timedelta
from django.shortcuts import render

from .models import Measurement


def index(request):
    measurements = Measurement.objects.last()
    time_threshold = datetime.now() - timedelta(hours=1)
    rain_measurements = (
        Measurement.objects.filter(created_at__gt=time_threshold)
        .order_by("created_at")
        .values("rain_fall", "created_at")
    )
    context = {
        "humidity": measurements.humidity,
        "pressure": measurements.pressure,
        "temperature": measurements.temperature,
        "lux": measurements.lux,
        "uv_index": measurements.uv_index,
        "uv_a": measurements.uv_a,
        "uv_b": measurements.uv_b,
        "wind_direction": measurements.wind_direction,
        "wind_gust": measurements.wind_gust,
        "wind_speed": measurements.wind_speed,
        "rain_measurements": rain_measurements,
    }
    return render(request, "index.html", context=context)


def statistics(request):
    return render(request, "statistics.html", context={})


def temperature(request):
    time_threshold = datetime.now() - timedelta(hours=24)
    temperature_measurement = (
        Measurement.objects.filter(created_at__gt=time_threshold)
        .order_by("created_at")
        .values("temperature", "created_at")
    )
    return render(
        request, "temperature.html", context={"temperatures": temperature_measurement}
    )


def wind(request):
    from django.db.models import Avg

    time_threshold = datetime.now() - timedelta(hours=24)
    wind_measurement = Measurement.objects.filter(
        created_at__gt=time_threshold
    ).order_by("created_at")
    wind_directions = []
    for wind_direction in Measurement.WIND_DIRECTION_CHOICES:
        avg = wind_measurement.filter(
            wind_direction=wind_direction[0], wind_speed__gt=0
        ).aggregate(Avg("wind_speed"), Avg("wind_gust"))
        wind_directions.append(
            {
                "direction": wind_direction[1],
                "gust": avg["wind_gust__avg"] or 0,
                "speed": avg["wind_speed__avg"] or 0,
            }
        )
    return render(request, "wind.html", context={"wind_directions": wind_directions})

