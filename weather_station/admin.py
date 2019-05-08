from django.contrib import admin
from .models import BasicMeasurement, WindMeasurement, RainMeasurement


admin.site.register(BasicMeasurement)
admin.site.register(WindMeasurement)
admin.site.register(RainMeasurement)
