mport RPi.GPIO as G
import picamera 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
sender = 'example@gmail.com'  #enter your email
password = 'abcd1234'         #enter your pwd
receiver = 'example@gmail.com' # enter the receivers mail id
mail=MIMEMultipart()
 msg['From'] = sender
 msg['To'] = receiver
 msg['Subject'] = 'Movement Detected near picam at your[location]'
 body = 'Picture is Attached.'
G.setmode(G.BCM)
data=””
def sendMail(data):
	mail.attach(MIMEText(body,”plain”))
	print data
	dat=’%s.jpg’%data
	print dat
	attachment=open(dat,’rb’)
	image=MIMEImage(attachment.read())
	attachment.close()
	mail.attach(image)
	server=smtplib.SMTP(‘smtp.gmail.com’,587)
	server.starttls()
	server.login(sender,password)
	text=mail.as_string()
	server.sendmail(sender, receiver, text)
 	server.quit()

def capture_image():
	data=time.strftime(“%d_%b_%Y|%H:%M:%S”)
	camera.start_preview()
	time.sleep(1)
	print data
	camera.capture(’%s.jpg’%data)
	camera.stop_preview()
	time.sleep(1)
	sendMail(data)

camera=picamera.PiCamera()
t=1
if(t==1):
	capture_image()
	time.sleep(1)
	t=0
