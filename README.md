# DHT22 Temperature and Humidity Sensor MQTT Publisher
 -This project enables you to read temperature and humidity data from a DHT22 sensor and publish it to an MQTT    broker

  ## Requirements :
    > Raspberry Pi or similar single-board computer
    > DHT22 sensor
    > Python 3.x installed
    > pip package manager installed

  ## Installation Steps : 
     > Clone the Repository 
     > Install Dependencies
        - pip install -r requirements.txt 
  ## Connect the DHT22 Sensor:
     > Connect the DHT22 sensor to your Raspberry Pi or similar device. Make sure to connect the appropriate pins for power, ground, and data.

  ## Configuration:
     > create .env  file in the some directry of the project and provide your MQTT broker details , pin configration for DHT22 sensor like : 
         MQTT_BROKER_HOST = 'your broker host'
         MQTT_BROKER_PORT = 'broker port'
         MQTT_TOPIC = 'topic for publish message'
         DHT_PIN = 'DHT22 pin'
   ## Run the Script:
      > python room-assistant.py
     


