import smtplib
from email.message import EmailMessage
import time

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "mynotif4u@gmail.com"
    msg['from'] = user
    #password = "foryou123*" #gipuzwjmxnpzgtck 2-step verification password
    password = "gipuzwjmxnpzgtck"


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()
    #not to send email soon time.sleep (60*60) # 1 hour
    

