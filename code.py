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




ADAFRUIT_IO_KEY = 'partharora'
ADAFRUIT_IO_USERNAME = '************************'
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
  
