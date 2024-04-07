import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, host, port, topic):
        self.client = mqtt.Client()
        self.host = host
        self.port = port
        self.topic = topic

    def connect(self):
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.connect(self.host, self.port,keepalive=10)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print("Connection failed")

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection from MQTT broker. Reconnecting...")
            self.client.reconnect()

    def publish(self, data):
        if not self.client.is_connected():
            print("Attempting to reconnect to MQTT broker...")
            self.client.reconnect()

        self.client.publish(self.topic, data)
