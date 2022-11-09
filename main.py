from sense_hat import SenseHat
import time

sense = SenseHat()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

pre_hum = 0;
col = red

def trigger_water():
  global pre_hum
  global col
  humidity = sense.humidity
  humidity_value = 64 * humidity / 100
  pixels = [col if i < humidity_value else white for i in range(64)]
  if humidity < 50 and humidity != pre_hum:
    print("need to water plants, humidity : " + str(humidity))
    pre_hum = humidity
    col = red
  elif humidity != pre_hum:
    col = green
  sense.set_pixels(pixels)

while True:
    trigger_water()
    time.sleep(1)
