from gpiozero import MCP3008


adc = MCP3008(channel=0)
count = 0
volts = {0.4: "n",
         1.4: "n-e",
         1.2: "n-e",
         2.8: "e",
         2.7: "e",
         2.9: "s-e",
         2.3: "s-e",
         2.2: "s-e",
         2.5: "s-e",
         1.8: "s",
         2.0: "s-w",
         0.7: "s-w",
         0.8: "s-w",
         0.1: "w",
         0.3: "w",
         0.2: "n-w",
         0.6: "n-w"}


def get_data():
    wind = round(adc.value * 3.3, 1)
    return volts[wind] if wind in volts else None
