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
builtins.frameCount     = 0
builtins.ellipse_mode   = CENTER
builtins.rect_mode      = CORNER


# variables
stack = [] # store for settings
settings = {
    "fill_color"    : [255,255,255,255],
    "no_fill"       : False,
    "no_stroke"     : False,
    "stroke_weight" : 1,
    "stroke_color"  : [0,0,0,255],
    "rotate_amnt"   : 0,
    "scale_amnt"    : 1,
    "text_size"     : 12,
    "text_font"     : "Arial",
    "text_bold"     : False,
    "text_italic"   : False,
    "text_align"    : LEFT,
    "text_color"    : [0,0,0,255],
    "text_outline"  : [0,0,0,0],
    "origin_x"      : 0,
    "origin_y"      : 0,
    "real_ox"       : 0,
    "real_oy"       : 0,
}


vertices      = []
curvevertices = []
shape         = None

