import time

from adafruit_apds9960.apds9960 import APDS9960
from touchio import TouchIn
from support.mytyping import NoReturn

LOOP_DELAY = 0.2

def run_serial_printer(apds: APDS9960, touch1: TouchIn, touch2: TouchIn) -> NoReturn:
    """
    Read the apds and touch pads once every LOOP_DELAY seconds and print:
      proximity
      touch raw value, touch boolean
    
    Args:
        apds (APDS9960): proximity sensor.
        touch1 (TouchIn): touch sensor for confirming input.
        touch2 (TouchIn): touch sensor for confirming input.
    """
    while True:
        prox = apds.proximity
        touch1_bool = touch1.value
        touch1_raw = touch1.raw_value
        touch2_bool = touch2.value
        touch2_raw = touch2.raw_value

        print(f"Proximity: {prox}")
        print(f"Touch1: ({touch1_raw}, {touch1_bool})")
        print(f"Touch2: ({touch2_raw}, {touch2_bool})")

        print()

        time.sleep(LOOP_DELAY)