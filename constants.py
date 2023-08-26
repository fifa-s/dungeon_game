"""All major constants that affect the whole game should be defined here"""

import platform
from pygame import transform

SYSTEM = platform.system()
SCALE_FUNCTION = transform.smoothscale

SCREEN_SIZE = (1920, 1080)
DISPLAY_SIZE = (480, 270) # Not so useful, just the size the screen resizes to when you minimize IT