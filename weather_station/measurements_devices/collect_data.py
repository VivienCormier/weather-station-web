import time
import statistics

from .bme280_sensor import get_data as bme280_sensor_get_data
from .ds18b20_therm import get_data as ds18b20_therm_get_data
from .tsl2561 import get_data as tsl2561_get_data
from .veml6075 import get_data as veml6075_get_data
from .rain_fall import reset_rainfall, get_data as rain_fall_get_data
from .wind import reset_wind, calculate_speed
from .wind_direction import get_data as wind_direction_get_data

TIME_MEASUREMENT = 5 * 60  # 5 min
INTERVAL = 5  # 5 sec


def get_data(length=TIME_MEASUREMENT):
    direction_data = []
    speed_data = []
    reset_rainfall()
    start_time = time.time()

    while time.time() - start_time <= length:
        reset_wind()
        time.sleep(INTERVAL)

        # Wind direction
        direction = wind_direction_get_data()
        if direction:
            direction_data.append(direction)

        # Wind speed
        speed = calculate_speed(INTERVAL)
        speed_data.append(speed)

    avg_direction = statistics.mode(direction_data) if direction_data else None
    wind_speed = statistics.mean(speed_data) if speed_data else None
    wind_gust = max(speed_data)

    data = {
        "humidity": None,
        "pressure": None,
        "temperature": None,
        "lux": None,
        "uv_index": None,
        "uv_a": None,
        "uv_b": None,
        "wind_direction": avg_direction,
        "wind_gust": wind_gust,
        "wind_speed": wind_speed,
        "rain_fall": rain_fall_get_data(),
    }

    data.update(bme280_sensor_get_data())
    data.update(ds18b20_therm_get_data())
    data.update(tsl2561_get_data())
    data.update(veml6075_get_data())
    return data
