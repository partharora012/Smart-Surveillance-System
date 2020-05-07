import RPi.GPIO as G
import picamera 
import base64
import smtplib
from Adafruit_IO import Client, Feed, RequestError

# Importing modules for sending mail
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

sender = 'example@gmail.com'  #enter your email
password = 'abcd1234'         #enter your pwd
receiver = 'example@gmail.com' # enter the receivers mail id



def convertImageToBase64():
 with open("img.jpg", "rb") as image_file:
     encoded = base64.b64encode(image_file.read())
     image_string = encoded.decode("utf-8")
 return image_string




ADAFRUIT_IO_KEY = 'aio_qsAC61OI9x8lP6xxyCBRbIvONU8O'
ADAFRUIT_IO_USERNAME = 'partharora'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
picam_feed = aio.feeds('picam')

G.setmode(G.BCM)
G.setup(2,G.IN)

cam=picamera.PiCamera()
cam.resolution = (200, 200)
if(G.input(2)):
  cam.capture(‘/home/pi/img.jpg’)
  imgg=convertImageToBase64()
  aio.send(picam_feed.key, imgg)
  msg = MIMEMultipart()
  msg['From'] = sender
  msg['To'] = receiver
  msg['Subject'] = 'Movement Detected near picam at your[location]'
    
  body = 'Picture is Attached.'
  msg.attach(MIMEText(body, 'plain'))
  attachment = open(r"/home/pi/img.jpg", 'rb')
  part = MIMEBase('application', 'octet-stream')
  part.set_payload((attachment).read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', 'attachment; filename= "img.jpg"')
  msg.attach(part)
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo() 
  server.starttls()
  server.ehlo() 
  server.login(sender, password)
  text = msg.as_string()
  server.sendmail(sender, receiver, text)
  server.quit()