import paho.mqtt.client as mqtt
import time
import sys  
import json
import random

deviceId = "DeviceId"
deviceKey = "DeviceKey"
dataChnId1 = "data"
MQTT_SERVER = "mqtt.mcs.mediatek.com"
MQTT_PORT = 1883
MQTT_ALIVE = 60
MQTT_TOPIC1 = "mcs/" + deviceId + "/" + deviceKey + "/" + dataChnId1

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)	

while True:
    h0 = str(random.randint(0,99))
    payload = {"dataChnId":dataChnId1,"value":h0}
    print dataChnId1 + " : " + h0
    mqtt_client.publish(MQTT_TOPIC1, json.dumps(payload), qos=1)
    time.sleep(1)