import os
import time
from dotenv import load_dotenv
from mqtt_client import MqttClient
from dht22_sensor import DHT22Sensor

if __name__ == "__main__":
    # Load configuration from .env file
    load_dotenv()
    MQTT_BROKER_HOST = os.getenv("MQTT_BROKER_HOST")
    MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT"))
    MQTT_TOPIC = os.getenv("MQTT_TOPIC")
    DHT_PIN = int(os.getenv("DHT_PIN"))

    # Initialize sensor and MQTT client
    sensor = DHT22Sensor(DHT_PIN)
    mqtt_client = MqttClient(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_TOPIC)

    # Connect to MQTT broker
    mqtt_client.connect()

    try:
        while True:
            # Read temperature and humidity
            humidity, temperature = sensor.read()
            if humidity is not None and temperature is not None:
                # Publish data to MQTT broker
                mqtt_client.publish(f"Temperature: {temperature}, Humidity: {humidity}")
                print("Published data to MQTT broker")
            else:
                print("Failed to retrieve data from sensor")

            time.sleep(10)  # Wait for 10 seconds before reading again

    except KeyboardInterrupt:
        print("Exiting...")
        mqtt_client.client.disconnect()
