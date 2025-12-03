import time

from src import morse_code
from neopixel import NeoPixel
from adafruit_apds9960.apds9960 import APDS9960
from touchio import TouchIn
from support.mytyping import NoReturn

# Constants (Keep same or tests will break)
THRESHOLD: int = 75
UNIT_TIME: float = 0.48

RED   : tuple[int, int, int] = (255, 0,   0)
YELLOW: tuple[int, int, int] = (220, 160, 0)
GREEN : tuple[int, int, int] = (0,   255, 0)

# Legacy ham radio license requirement
# - 0.24 sec unit time (5 words per minute)
# Fastest recorded transcription on a straight key
# - 0.034 sec unit time (35 words per minute)


def set_color(elapsed_time: float, pixels: NeoPixel) -> None:
    """
    Lights the LEDs on the trinkey depending on the length of input.
    
    Args:
        elapsed_time (float): duration of proximity detection.
        pixels : LED controller object.
    """
    # Your Code Here!


def add_mark(elapsed_time: float) -> str:
    """
    Determines if input is a dot (.), dash (-), or nothing ("") based 
    on the length of input.
    
    Args:
        elapsed_time (float): duration of proximity detection.

    Returns:
        str: dot (.), dash (-), or empty ("").
    """
    # Your Code Here!

def run_morse_engine(apds: APDS9960, pixels: NeoPixel, touch1: TouchIn, touch2: TouchIn) -> NoReturn:
    """
    Runs Morse code translation based on proximity input.

    Args:
        apds: proximity sensor.
        pixels: LED controller object.
        touch: touch sensor for confirming input.
    """
    morse = ""                # Dots, dashs, and slashes so far
    start = time.monotonic()  # Time when proximity sensor was first triggered

    # Main loop
    while True:
        if touch1.value or touch2.value:
            print("Touched!")
        print("the message should be here", "<==")
        
