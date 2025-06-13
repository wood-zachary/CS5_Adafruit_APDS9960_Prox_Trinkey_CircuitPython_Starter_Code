from .pulse import pulse
from neopixel import NeoPixel
from adafruit_apds9960.apds9960 import APDS9960
from support.mytyping import NoReturn

THRESHOLD: int = 75

RED: tuple[int, int, int] = (150, 10, 10)
GREEN: tuple[int, int, int] = (30, 100, 10)


def prox_pulse(pixels: NeoPixel, color: tuple[int, int, int], prox: int) -> None:
    """
    Maps proximity value to pulse duration and calls pulse.

    Args:
        pixels: LED controller object.
        color (tuple): color to pulse.
        prox (int): proximity value.
    """
    # Your Code Here!


def run_prox_pulse(apds: APDS9960, pixels: NeoPixel) -> NoReturn:
    """
    Runs proximity-based pulsing demo.

    Args:
        apds: proximity sensor.
        pixels: LED controller object.
    """
    # Main loop
    while True:
        print(apds.proximity)
        # Your Code Here!
