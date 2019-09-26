"""weather_station URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weather_station import views

urlpatterns = [
    path("", views.index, name="index"),
    path("statistics/", views.statistics, name="statistics"),
    path("statistics/temperature/", views.temperature, name="temperature"),
    path("statistics/wind/", views.wind, name="wind"),
    path("statistics/uv/", views.index, name="uv"),
    path("statistics/lux/", views.lux, name="lux"),
    path("statistics/humidity/", views.humidity, name="humidity"),
    path("statistics/pressure/", views.pressure, name="pressure"),
    path("statistics/rain/", views.rain, name="rain"),
    path("admin/", admin.site.urls),
]
