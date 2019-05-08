import bme280
import smbus2

port = 1
address = 0x77  # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)


def get_data():
    bme280_data = bme280.sample(bus, address)
    return {
        'humidity': bme280_data.humidity,
        'pressure': bme280_data.pressure,
    }
