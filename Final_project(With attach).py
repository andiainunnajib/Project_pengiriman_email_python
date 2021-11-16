import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



def get_email(email_send):
    receiver_list = []
    with open(email_send, 'r') as email_kirim:
        for kirim in email_kirim:
            kirim = kirim.replace('')
            receiver_list.append(kirim)
    return receiver_list

subject = 'subject'


email_user = 'your email'
email_password = 'your pass'
email_send = 'datasets\receiver_list.txt'

for email1 in email_send:
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email1
    msg['Subject'] = subject

    body = 'INI ADA PROJECT PYTHON MENGIRIM EMAIL LEWAT PYTHON DENGAN ATTCHEMENT FILE!'

    msg.attach(MIMEText(body,'plain'))

    filename='datasets/KISI-KISI UN SMP 2019.pdf'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email1,text)
    server.quit()
