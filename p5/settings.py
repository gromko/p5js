import builtins
from p5.constants import *

pg_Screen = None
clock = None

builtins.mouseX         = 0
builtins.mouseY         = 0
builtins.pmouseX        = None
builtins.pmouseY        = None
builtins.movedX         = None
builtins.movedY         = None
builtins.mouseButton    = None
builtins.mouseIsPressed = False
builtins.keyIsPressed   = False
builtins.key            = None
builtins.keyCode        = None
builtins.width          = 360
builtins.height         = 360
builtins.shape          = []
builtins.framerate      = 60
builtins.is_Looping     = True
builtins.ANGLEMODE      = DEGREES
builtins.RANDOMSEED     = 0
builtins.MILLIS         = 0

# variables
settings_stack = []
settings_copy  = {}
settings = {
    "fill_color"    : (255,255,255),
    "no_fill"       : False,
    "no_stroke"     : False,
    "stroke_weight" : 1,
    "stroke_color"  : (0,0,0),
    "rotate_amnt"   : 0,
    "scale_amnt"    : 1,
    "text_size"     : 12,
    "text_font"     : "Arial",
    "text_bold"     : False,
    "text_italic"   : False,
    "origin_x"      : 0,
    "origin_y"      : 0,
}


vertices      = []
curvevertices = []
shape         = None

