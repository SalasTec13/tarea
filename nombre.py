import sense_hat
from time import sleep,time
from random import randint

from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(0)
red = (255, 0, 0)
sense.show_message("Examen", text_colour=red)
