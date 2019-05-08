import board
import busio
import adafruit_veml6075

i2c = busio.I2C(board.SCL, board.SDA)

veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)


def get_data():
    return {
        'uv_index': veml.uv_index,
        'uv_a': veml.uva,
        'uv_b': veml.uvb,
    }
