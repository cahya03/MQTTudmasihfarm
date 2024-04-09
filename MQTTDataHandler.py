import json
import time

from MQTTPushover import notif
from MQTTMailAlert import email_alert

# notif from mynotif4u@gmail.com
alert = False
subject = "*Notification STATUS SIAGA*"
title = "*Notification STATUS SIAGA*"
to = "muditaputu@gmail.com"
body = ""

# json = "{\"temperature\":" +String(t,2)+",\"humidity\":"+String(h,0)+",\"heatindex\":"+String(hic,2)+"}";
def Sensor_Data_Handler(Topic, jsonData):
	try:
		json_object = json.loads(jsonData)
	except ValueError as e:
		return False

	json_Dict = json.loads(jsonData)
	t = json_Dict['temperature']
	print(t)
	if (t < 29.00):
		alert = True; subject = "Suhu DROP"
	elif (t > 39.00):
		alert = True; subject = "Suhu NAIK"
	else:
		alert = False

	global newsubject
	if (alert):
		#email_alert(subject, body, to)
		notif(subject, title)





