import time
import statistics

import bme280_sensor
import ds18b20_therm
import rain_fall
import tsl2561
import veml6075
import wind
import wind_direction

TIME_MEASUREMENT = 5 * 60  # 5 min
INTERVAL = 5  # 5 sec


def get_data(length=TIME_MEASUREMENT):
    direction_data = []
    speed_data = []
    rain_fall.reset_rainfall()
    start_time = time.time()

    while time.time() - start_time <= length:
        wind.reset_wind()
        time.sleep(INTERVAL)

        # Wind direction
        direction = wind_direction.get_data()
        if direction:
            direction_data.append(direction)

        # Wind speed
        speed = wind.calculate_speed(INTERVAL)
        speed_data.append(speed)

    avg_direction = statistics.mode(direction_data) if direction_data else None
    wind_speed = statistics.mean(speed_data) if speed_data else None
    wind_gust = max(speed_data)

    data = {
        'humidity': None,
        'pressure': None,
        'temperature': None,
        'lux': None,
        'uv_index': None,
        'uv_a': None,
        'uv_b': None,
        'wind_direction': avg_direction,
        'wind_gust': wind_gust,
        'wind_speed': wind_speed,
        'rain_fall': rain_fall.bucket_tipped(),
    }

    data.update(bme280_sensor.get_data())
    data.update(ds18b20_therm.get_data())
    data.update(tsl2561.get_data())
    data.update(veml6075.get_data())
    return data
