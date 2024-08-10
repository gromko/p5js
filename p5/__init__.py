import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from p5.corefunctions import (run, createCanvas, saveCanvas, angleMode,
                              line, ellipse, circle, rect, quad, arc, triangle,
                              point, beginShape, vertex, curveVertex,
                              endShape, cursor, strokeWeight, noStroke, 
                              loadImage, image, keyIsDown, frameRate, loop, noLoop,  
                              background,text,textFont, textSize, textStyle, textAlign)

from p5.constants import (TWO_PI, HALF_PI, PI, QUARTER_PI, TAU, CURSOR_ARROW, CURSOR_DIAMOND, 
    CURSOR_BROKEN_X, CURSOR_TRI_LEFT, CURSOR_TRI_RIGHT, BOLD, ITALIC, BOLDITALIC, NORMAL,
    BACKSPACE,TAB,RETURN,ENTER,PAUSE,ESCAPE,SPACE,DELETE,EXCLAIM,QUOTEDBL,HASH,DOLLAR,AMPERSAND,QUOTE,LEFTPAREN,RIGHTPAREN,
    ASTERISK,PLUS,COMMA,MINUS,PERIOD,SLASH,COLON,SEMICOLON,LESS,EQUALS,GREATER,QUESTION,AT,LEFTBRACKET,RIGHTBRACKET,CARET,
    UNDERSCORE,BACKQUOTE,UP,DOWN,RIGHT,LEFT,UP_ARROW,DOWN_ARROW,LEFT_ARROW,RIGHT_ARROW,INSERT,HOME,END,PAGEUP,PAGEDOWN,PGUP,
    PGDN,KP0,KP1,KP2,KP3,KP4,KP5,KP6,KP7,KP8,KP9,KP_PERIOD,KP_DIVIDE,KP_MULTIPLY,KP_MINUS,KP_PLUS,F1,F2,F3,F4,F5,
    F6,F7,F8,F9,F10,F11,F12,NUMLOCK,CAPSLOCK,SCROLLOCK,RSHIFT,LSHIFT,RCTRL,LCTRL,RALT,LALT,RMETA,LMETA,CONTEXTMENU,
    PRINT,SYSREQ,BREAK,MENU,CENTER,CLOSE,RADIANS,DEGREES, CORNER, CORNERS, RADIUS,CHORD, PIE, OPEN, ARC)
    
from p5.mathfunctions import (pow, map, randomSeed, random, constrain, floor, ceil, dist, exp, lerp, log, log10, log2, logb, mag,
                              rerange, norm, sq, sqrt, frac, sin, cos, tan, asin, acos, atan, atan2, degrees, radians, integral)

from p5.color import (fill,noFill, stroke, red, green, blue, brightness, hue, lightness, saturation, lerpColor, color, alpha)

from p5.timedata import (hour, minute, second, day, month, year, milli_sec,  millis)

from p5.drawcurve import (bezier,spline)

from p5.transform import (scale, rotate, translate,  push, pop, resetMatrix)

__all__ = ["run", "createCanvas", "translate", "background", "fill", "noFill", "line", "ellipse", "circle", "rect", "triangle", "quad", "arc",
    "push", "pop", "cursor", "TWO_PI", "HALF_PI", "PI", "QUARTER_PI", "TAU", "CURSOR_ARROW", "CURSOR_DIAMOND", "CURSOR_BROKEN_X", "CURSOR_TRI_LEFT",
    "CURSOR_TRI_RIGHT", "BOLD", "ITALIC", "BOLDITALIC", "NORMAL", "strokeWeight", "stroke", "noStroke", "loadImage", "image", "point", "CORNER", "CORNERS", "RADIUS",
     "frameRate", "random", "constrain", "floor", "ceil", "dist", "exp", "lerp", "log", "log10", "log2", "logb", "mag", "textAlign", "CHORD", "PIE", "OPEN", "ARC",
    "rerange", "norm", "sq", "sqrt", "frac", "sin", "cos", "tan", "asin", "acos", "atan", "atan2", "degrees",    "radians", "loop", "noLoop", "integral",
    "text","textFont", "textSize", "textStyle","beginShape", "vertex", "endShape", "keyIsDown", "saveCanvas", "scale", "rotate", "translate",
    "BACKSPACE","TAB","RETURN","ENTER","PAUSE","ESCAPE","SPACE","DELETE","EXCLAIM","QUOTEDBL","HASH","DOLLAR","AMPERSAND","QUOTE","LEFTPAREN","RIGHTPAREN",
    "ASTERISK","PLUS","COMMA","MINUS","PERIOD","SLASH","COLON","SEMICOLON","LESS","EQUALS","GREATER","QUESTION","AT","LEFTBRACKET","RIGHTBRACKET","CARET",
    "UNDERSCORE","BACKQUOTE","UP","DOWN","RIGHT","LEFT","UP_ARROW","DOWN_ARROW","LEFT_ARROW","RIGHT_ARROW","INSERT","HOME","END","PAGEUP","PAGEDOWN","PGUP",
    "PGDN","KP0","KP1","KP2","KP3","KP4","KP5","KP6","KP7","KP8","KP9","KP_PERIOD","KP_DIVIDE","KP_MULTIPLY","KP_MINUS","KP_PLUS","F1","F2","F3","F4","F5",
    "F6","F7","F8","F9","F10","F11","F12","NUMLOCK","CAPSLOCK","SCROLLOCK","RSHIFT","LSHIFT","RCTRL","LCTRL","RALT","LALT","RMETA","LMETA","CONTEXTMENU",
    "PRINT","SYSREQ","BREAK","MENU","CENTER","CLOSE", "pow", "map", "angleMode", "curveVertex", "randomSeed", "resetMatrix",
    "hour", "minute", "second", "day", "month", "year", "milli_sec", "millis", "bezier", "spline"
]

__version__ = "0.5.04"

print("Thank you for using p5\n")

