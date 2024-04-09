from pushover import Client

def notif(subject,title):
	client = Client("u7hr6s4kuzauxjyta866gpcj5s1zbe", api_token="ak7qnvsyrjvemdw3v3etr75i7fnhub")
	client.send_message(subject, title=title, sound="siren", retry="60", expire="120", priority="2")


##with open('/path/to/my/image.png', 'rb') as image:
##    client.send_message('Message with image', attachment=image)

