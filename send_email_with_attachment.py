import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_name = 'Home Security'
sender = 'senders_mail_id@gmail.com'
receiver = 'receivers_mail_id@gmail.com'
sub = 'Test Only!'

msg = MIMEMultipart()
msg['From'] = sender_name
msg['To'] = receiver
msg['Subject'] = sub

body = "Hello there!\n\n This mail is sent from python program!"
msg.attach(MIMEText(body,'plain'))

fname = 'original.jpg'
attachment = open(fname,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+fname)

msg.attach(part)

text = msg.as_string()

sr = smtplib.SMTP('smtp.gmail.com',587)
sr.starttls()
sr.login(sender,'############')


sr.sendmail(sender,receiver,text)
sr.quit()