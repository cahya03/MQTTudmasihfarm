import paho.mqtt.client as mqtt
import time
from MQTTDataHandler import Sensor_Data_Handler

MQTT_Broker = "localhost"
MQTT_Port = 1883
MQTT_User = "emonpi"
MQTT_Password = "emonpimqtt2016"
MQTT_Topic = "emon/1001/#"
Keep_Alive_Interval = 60

def on_message(mosq, obj, msg):
	Sensor_Data_Handler(msg.topic, msg.payload)

def on_connect(self, mosq, obj, rc):
	if rc != 0:
		pass
		print("Unable to connect to MQTT Broker...")
	else:
		print("Connected with MQTT Broker: " + str(MQTT_Broker) )
		print("subscribe to MQTT Broker: " + str(MQTT_Topic))
		self.subscribe(MQTT_Topic, 0)
		mqttc.subscribe(MQTT_Topic, 0)


def on_subscribe(mosq, obj, mid, granted_qos):
	pass

def on_disconnect(self, mosq, rc):
	if rc !=0:
		pass


mqttc = mqtt.Client()
mqttc.username_pw_set(MQTT_User, password=MQTT_Password)

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_subscribe = on_subscribe



# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
#mqttc.loop_start()  #Start loop 
#mqttc.loop_stop()    #Stop loop 
# Continue the network loop
mqttc.loop_forever()


