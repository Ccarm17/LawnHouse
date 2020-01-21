import time
import board
import busio
import adafruit_sht31d
import csv
from Adafruit_IO import Client, RequestError, Feed

# the header names for the csv file
HEADER = ['Temperature', 'Temperature1', 'Humidity', 'Humidity1', 'Time']
sleepTime = 20
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)
sensor1 = adafruit_sht31d.SHT31D(i2c)

ADAFRUIT_IO_KEY = "aio_hAvt22je34xRKA3YFj302pNn67OG"
ADAFRUIT_IO_USERNAME = "Ccarm97"
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

loopcount = 0

try:
    humidity = aio.feeds('humidity')
except RequestError: # Doesn't exist, create a new feed
    feed = Feed(name="humidity")
    humidity = aio.create_feed(feed)

try:
    humidity1 = aio.feeds('humidity1')
except RequestError: # Doesn't exist, create a new feed
    feed = Feed(name="humidity1")
    humidity1 = aio.create_feed(feed)

try:
    temperature = aio.feeds('temperature')
except RequestError: # Doesn't exist, create a new feed
    feed = Feed(name="temperature")
    temperature = aio.create_feed(feed)

try:
    temperature1 = aio.feeds('temperature1')
except RequestError: # Doesn't exist, create a new feed
    feed = Feed(name="temperature1")
    temperature1 = aio.create_feed(feed)

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    print("\nTemperature: %0.1f C" % sensor1.temperature)
    print("Humidity: %0.1f %%" % sensor1.relative_humidity)

    aio.send_data(temperature.key, "%0.1f" % sensor.temperature)
    aio.send_data(temperature1.key, "%0.1f" % sensor1.temperature)
    aio.send_data(humidity.key,"%0.1f" % sensor.relative_humidity)
    aio.send_data(humidity1.key,"%0.1f" % sensor1.relative_humidity)

    loopcount += 1
    time.sleep(sleepTime)
