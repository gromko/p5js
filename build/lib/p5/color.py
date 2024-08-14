from p5.settings import *
from pygame import Color

# COLOR
def get_Color(c, a=255):
    color = None
    if (type(c) == int) and (0 <= c) and (255 >= c):
        color = Color(c, c, c)
    elif (type(c) == float) and (0 <= c) and (255 >= c):
        color = Color(int(c), int(c), int(c))
    elif (type(c) == str):
        color = Color(c)
        if c=="green":
            color =  Color(int(0), int(128), int(0)) # p5.js green color 
    elif (type(c) == tuple):
        color = Color(c)
    else:
        color = Color("black")
    color.a = a
    return color
    
def set_colors(*args):    
    if len(args)==1 :
        return get_Color(args[0])
    if len(args)==2 :
        return get_Color(args[0],args[1])
    if len(args)==3 :
        return get_Color((args[0],args[1],args[2]))
    if len(args)==4 :
        return get_Color((args[0],args[1],args[2]),args[3])

def fill(*args): # set fill color
    settings["fill_color"] = set_colors(*args)
    settings["no_fill"] = False
    settings["text_color"] = settings["fill_color"]
    pass

def noFill():
    settings["no_fill"] = True
    settings["text_color"] = settings["fill_color"]
    pass

def stroke(*args):
    settings["stroke_color"] = set_colors(*args)
    settings["no_stroke"] = False
    settings["text_outline"] = settings["stroke_color"]
    pass    

def color(r, g, b):
    return Color(r, g, b)

def alpha(c):
    return c.a

def red(c):
    return c.r

def green(c):
    return c.g

def blue(c):
    return c.b

def brightness(c):
    return c.hsva[2]

def hue(c):
    return c.hsva[0]

def lightness(c):
    return c.hsla[2]

def saturation(c):
    return c.hsla[1]

def lerpColor(c1, c2, amnt):
    return c1.lerp(c2, amnt)


