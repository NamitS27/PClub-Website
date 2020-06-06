import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

def send(name,semail,subjects,messages,jw):
    email = 'namit.s@ahduni.edu.in'
    password = 'Nsahduni27'
    send_to_email = 'suhanee.p@ahduni.edu.in'
    send_to_emails = [] # List of bcc
    subject = subjects
    message = f"name : {name} , email : {semail} \n message : {messages}" 
    if jw=="Yes":
        message += f"\nI want to join Whatsapp grp"   
    # file_location = 'C:\\Users\\You\\Desktop\\attach.txt'

    # Create the attachment file (only do it once)
    # filename = os.path.basename(file_location)
    # attachment = open(file_location, "rb")
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server.sendmail(email, [send_to_email]+send_to_emails, msg.as_string()) 
    server.quit()