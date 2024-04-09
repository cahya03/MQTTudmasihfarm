import json
import time

from MQTTMailAlert import email_alert

#notif from gmail
newsubject = "Notification STATUS SIAGA 1"
body = "ALERT status *bahaya*"
to = "swardika@gmail.com"


def Sensor_Data_Handler(Topic, jsonData):
	try:
		json_object = json.loads(jsonData)
	except ValueError as e:
		return False

	json_Dict = json.loads(jsonData) 
	t1001 = json_Dict['temperature']
	h1001 = json_Dict['humidity']
	i1001 = json_Dict['heatindex']

	print(t1001," ",h1001," ",i1001)

	if (i1001 < 27.00): subject = "Green"
	elif (i1001 < 33.00): subject = "Caution"
	elif (i1001 < 40.00): subject = "Extreme caution"
	elif (i1001 < 52.00): subject = "Danger"
	else: subject = "Extreme danger"

	global newsubject
	if (i1001 >= 50):
		if (newsubject != subject):
			email_alert(subject, body, to)
			newsubject = subject





