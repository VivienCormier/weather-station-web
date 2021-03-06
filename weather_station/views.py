from datetime import datetime, timedelta
from django.shortcuts import render
from django.db.models.functions import ExtractWeek, ExtractYear
from django.db.models import Sum

from .models import Measurement
from .utils import group_measurements


def index(request):
    measurement = Measurement.objects.last()
    time_threshold = datetime.now() - timedelta(hours=1)
    measurements = Measurement.objects.filter(created_at__gt=time_threshold).order_by(
        "created_at"
    )
    context = {
        "humidity": measurement.humidity,
        "pressure": measurement.pressure,
        "temperature": measurement.temperature,
        "lux": measurement.lux,
        "uv_index": measurement.uv_index,
        "uv_a": measurement.uv_a,
        "uv_b": measurement.uv_b,
        "wind_direction": measurement.wind_direction,
        "wind_gust": measurement.wind_gust,
        "wind_speed": measurement.wind_speed,
        "measurements": measurements,
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
    from django.db.models import Max

    time_threshold = datetime.now() - timedelta(hours=24)
    wind_measurement = Measurement.objects.filter(
        created_at__gt=time_threshold
    ).order_by("created_at")
    wind_directions = []
    for wind_direction in Measurement.WIND_DIRECTION_CHOICES:
        avg = wind_measurement.filter(
            wind_direction=wind_direction[0], wind_speed__gt=0
        ).aggregate(Max("wind_speed"), Max("wind_gust"))
        wind_directions.append(
            {
                "direction": wind_direction[1],
                "gust": avg["wind_gust__max"] or 0,
                "speed": avg["wind_speed__max"] or 0,
            }
        )
    return render(
        request,
        "wind.html",
        context={
            "wind_directions": wind_directions,
            "wind_measurement": wind_measurement,
        },
    )


def humidity(request):
    time_threshold = datetime.now() - timedelta(hours=24)
    measurements = (
        Measurement.objects.filter(created_at__gt=time_threshold)
        .order_by("created_at")
        .values("humidity", "created_at")
    )
    return render(request, "humidity.html", context={"measurements": measurements})


def pressure(request):
    time_threshold = datetime.now() - timedelta(hours=24)
    measurements = (
        Measurement.objects.filter(created_at__gt=time_threshold)
        .order_by("created_at")
        .values("pressure", "created_at")
    )
    return render(request, "pressure.html", context={"measurements": measurements})


def lux(request):
    time_threshold = datetime.now() - timedelta(hours=24)
    measurements = (
        Measurement.objects.filter(created_at__gt=time_threshold)
        .order_by("created_at")
        .values("lux", "created_at")
    )
    return render(request, "lux.html", context={"measurements": measurements})


def rain(request, slice="hour"):
    time_threshold = datetime.now() - timedelta(days=365)
    if slice == "hour":
        time_threshold = datetime.now() - timedelta(hours=24)

    measurements_rain = (
        Measurement.objects.filter(created_at__gt=time_threshold)
        .order_by("created_at")
        .values("rain_fall", "created_at")
    )
    measurements = group_measurements(
        Measurement.objects.filter(created_at__gt=time_threshold),
        "rain_fall",
        slice,
        "sum",
    )
    return render(
        request,
        "rain.html",
        context={
            "measurements": measurements,
            "sum": measurements_rain.aggregate(Sum("rain_fall")),
        },
    )
