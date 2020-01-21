from time import sleep
from gpiozero import LED


relay1 = LED(17)
relay2 = LED(27)

while True:
    relay1.on()
    relay2.on()
    sleep(2)
    relay1.off()
    relay2.off()
    sleep(2)
    print ("running")
