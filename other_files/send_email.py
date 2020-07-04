import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send(name,semail,subjects,messages,jw):
    email = os.environ.get('EMAIL')
    password = os.environ.get('EMAIL_PASSWORD')
    send_to_email = ''
    send_to_emails = [semail,email] # List of bcc
    subject = subjects
    message = f"Sender Detials : <br> <b>Name</b> : {name} <br><b>Email</b> : {semail} <br> <b>Message</b> : {messages}<br>" 
    if jw=="Yes":
        message += f"I want to join WhatsApp group"   
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'html'))
        server.sendmail(email, [send_to_email]+send_to_emails, msg.as_string()) 
        server.quit()
        return "Send"
    except:
        return "Error"