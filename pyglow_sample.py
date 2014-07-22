#sample code from Pimoroni

from pyglow import PyGlow
from time import sleep

pyglow = PyGlow()

#set all the LEDs to off:
pyglow.all(0)

#turn on LEDs then off again
pyglow.led(1,100)
sleep(1)
pyglow.led(1,0)
sleep(1)

#light up the LEDs
pyglow.update_leds()


pyglow.led(2,100)
sleep(1)
pyglow.led(2,0)
sleep(1)
pyglow.update_leds()

pyglow.led(3,100)
sleep(1)
pyglow.led(3,0)
sleep(1)
pyglow.update_leds()

pyglow.led(4,100)
sleep(1)
pyglow.led(4,0)
sleep(1)
pyglow.update_leds()
