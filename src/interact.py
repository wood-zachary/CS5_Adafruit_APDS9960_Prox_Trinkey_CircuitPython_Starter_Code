from .serial_printer import run_serial_printer
# from .pulse import run_simple_pulse
# from .prox_pulse import run_prox_pulse
# from .morse_engine import run_morse_engine
# from .space_macro import run_space_macro

'''
Always comment out any imports you're not using to save memory.
'''

def run(
    *,
    apds=None,
    pixels=None,
    touch1=None,
    touch2=None, 
    nunchuk=None,
    gamepad=None
):
    """
    Runs the selected demo on the Trinkey.

    Args:
        proximity   — APDS9960 proximity sensor
        pixels      — NeoPixel object
        touch1      — TouchSensor
        touch2      — TouchSensor
        nunchuk     — Nunchuk controller
        gamepad     — MiniGamepad controller
    """
    run_serial_printer(apds, touch1, touch2)
    # run_simple_pulse(pixels)
    # run_prox_pulse(apds, pixels)
    # run_morse_engine(apds, pixels, touch1, touch2)
    # run_space_macro(apds, pixels)
