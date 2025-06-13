import time

from neopixel import NeoPixel
from support.mytyping import NoReturn

BLUE: tuple[int, int, int] = (0, 0, 255)
TIME: int = 1


def pulse(pixels: NeoPixel, color: tuple[int, int, int], duration: float) -> None:
    """
    Fills pixels with a color for a duration, then turns them off.

    Args:
        pixels (NeoPixel): NeoPixel object.
        color (tuple): Color to display.
        duration (float): time in seconds to keep the color on/off.
    """
    # Your Code Here!


def run_simple_pulse(pixels: NeoPixel) -> NoReturn:
    """
    Runs a simple pulse demo.

    Args:
        pixels: NeoPixel object.
    """
    # Main loop
    while True:
        pulse(pixels, BLUE, TIME)
