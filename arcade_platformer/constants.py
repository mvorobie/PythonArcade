import pathlib


# Game constants
# Window dimensions

SCREEN_WIDTH = 1290
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Arcade Platformer"
MAP_WIDTH = 3072

# Scaling constants
MAP_SCALING = 1.0

# Player constants
GRAVITY = 1.0
PLAYER_START_X = 65
PLAYER_START_Y = 256
PLAYER_MOVE_SPEED = 10
PLAYER_JUMP_SPEED = 25


# Viewport margins
LEFT_VIEWPORT_MARGIN = 300
RIGHT_VIEWPORT_MARGIN = 300
TOP_VIEWPORT_MARGIN = 150
BOTTOM_VIEWPORT_MARGIN = 150

# Joystick control
DEAD_ZONE = 0.1

# Assets path
ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets"