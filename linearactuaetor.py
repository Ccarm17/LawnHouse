import RPI.GPIO as GPIO
import time

relay1 = 17
relay2 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
