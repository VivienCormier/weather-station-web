from gpiozero import Button

rain_sensor = Button(6)
BUCKET_SIZE = 0.2794
count = 0


def bucket_tipped():
    global count
    count = count + 1


def reset_rainfall():
    global count
    count = 0


def get_data():
    global count
    return round(count * BUCKET_SIZE, 2)


rain_sensor.when_pressed = bucket_tipped
