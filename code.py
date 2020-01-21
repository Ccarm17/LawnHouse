import time
import board
import busio
import adafruit_sht31d
import csv

# the header names for the csv file
HEADER = ['Temperature', 'Temperature1', 'Humidity', 'Humidity1', 'Time']
sleepTime = 2
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)
sensor1 = adafruit_sht31d.SHT31D(i2c)

loopcount = 0



while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    print("\nTemperature: %0.1f C" % sensor1.temperature)
    print("Humidity: %0.1f %%" % sensor1.relative_humidity)

    loopcount += 1
    time.sleep(sleepTime)
