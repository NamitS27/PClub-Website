import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

def send(name,semail,subjects,messages,jw):
    email = 'noreplyahdunipclub@gmail.com'
    password = 'Noreply@Pclub9'
    send_to_email = ''
    send_to_emails = [semail,'suhanee.p@ahduni.edu.in','namit.s@ahduni.edu.in'] # List of bcc
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