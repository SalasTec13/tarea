import sense_hat
from sense_hat import SenseHat

sense = SenseHat()

green = (0,255,0)
white = (255,255,255)

while True:
  humidity = sense.get_humidity()
  humidity_value = 64 * humidity / 100
  pixels = [green if i<humidity_value else white for i in range (64)]
  sense.set_pixels(pixels)
