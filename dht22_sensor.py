import Adafruit_DHT

class DHT22Sensor:
    def __init__(self, pin):
        self.sensor = Adafruit_DHT.DHT22
        self.pin = pin

    def read(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        # temperature = 32
        # humidity = 82
        return humidity, temperature
