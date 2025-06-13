import time
import board
import touchio
import neopixel
from adafruit_apds9960.apds9960 import APDS9960

def setup() -> tuple[APDS9960, neopixel.NeoPixel, touchio.TouchIn, touchio.TouchIn]:
    """
    Returns (proximity_sensor, leds, touch_pad):
      - proximity_sensor.proximity → int
      - leds.fill((r,g,b))
      - touch_pad.value → bool
    """
    i2c  = board.I2C()

    apds = APDS9960(i2c)
    apds.enable_proximity = True
    # apds.enable_color = True
    # apds.enable_gesture = True

    leds = neopixel.NeoPixel(
        board.NEOPIXEL,
        2,
        brightness=0.1
    )

    touch1 = touchio.TouchIn(board.TOUCH1)
    touch2 = touchio.TouchIn(board.TOUCH2)

    time.sleep(0.01)
    return apds, leds, touch1, touch2
