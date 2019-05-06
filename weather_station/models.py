from django.db import models


class BasicMeasurement(models.Model):

    humidity = models.IntegerField(blank=True, null=True)
    pressure = models.IntegerField(blank=True, null=True)
    temperature = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True
    )
    lux = models.IntegerField(blank=True, null=True)
    uv_index = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, null=True
    )
    uv_a = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    uv_b = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class WindMeasurement(models.Model):

    WIND_DIRECTION_CHOICES = (
        (1, "n"),
        (2, "n-e"),
        (3, "e"),
        (4, "s-e"),
        (5, "s"),
        (6, "s-w"),
        (7, "w"),
        (8, "n-w"),
    )

    wind_direction = models.PositiveIntegerField(
        choices=WIND_DIRECTION_CHOICES, blank=True, null=True
    )
    wind_gust = models.IntegerField(blank=True, null=True)
    wind_speed = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class RainMeasurement(models.Model):

    rain_fall = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
