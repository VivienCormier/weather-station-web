import board
import busio
import adafruit_veml6075

i2c = busio.I2C(board.SCL, board.SDA)

veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)


def get_data():
    return {
        "uv_index": round(veml.uv_index, 2),
        "uv_a": round(veml.uva, 1),
        "uv_b": round(veml.uvb, 1),
    }
