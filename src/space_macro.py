from neopixel import NeoPixel
from adafruit_apds9960.apds9960 import APDS9960
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode 
from support.mytyping import NoReturn

def run_space_macro(apds: APDS9960, pixels: NeoPixel) -> NoReturn:
    """
    Press the space key with a component or peripheral of your Trinkey.
    
    Args:
        apds (APDS9960): proximity sensor.
        pixels (NeoPixel): NeoPixel object.
    """
    THRESHOLD = 3 
    DURATION = 0.25
    INTERVAL = 0.05
    GREEN = ((0, 150, 0))
    YELLOW = ((75, 75, 0))

    kb_macro = Keycode.SPACE
    kb = Keyboard(usb_hid.devices) 
    pixels.fill(YELLOW)
    
    last_prox = 0
    
    while True:
        prox = apds.proximity

        # Your Code Here!

        time.sleep(INTERVAL)


