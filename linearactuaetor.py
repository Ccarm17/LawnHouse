from time import sleep
from gpiozero import LED


relay1 = LED(17)
relay2 = LED(27)

direction = input()

if direction == "forward":
    
    relay1.on()
    relay2.off()
    sleep(15)
elif direction == "Backward":
    relay1.off()
    relay2.on()
    sleep(15)
else:
    relay1.off()
    relay2.off()
    sleep(2)
    print ("running")
