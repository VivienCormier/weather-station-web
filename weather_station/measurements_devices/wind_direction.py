from gpiozero import MCP3008


adc = MCP3008(channel=0)
count = 0
volts = {
    0.4: 1,
    1.4: 2,
    1.2: 2,
    2.8: 3,
    2.7: 3,
    2.9: 4,
    2.3: 4,
    2.2: 4,
    2.5: 4,
    1.8: 5,
    2.0: 6,
    0.7: 6,
    0.8: 6,
    0.1: 7,
    0.3: 7,
    0.2: 8,
    0.6: 8,
}


def get_data():
    wind = round(adc.value * 3.3, 1)
    return volts[wind] if wind in volts else None
