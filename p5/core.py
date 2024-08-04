import pygame
import numpy as np
import math
import sys
import types
import random
import __main__
import builtins
from pygame import Color
from functools import wraps
from multipledispatch import dispatch
from typing import Callable, Optional
from p5.constants import *
from p5.timedata import *
from p5.drawcurve import *

class Image(pygame.Surface):
    def __init__(self):
        pass
        
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

builtins.setup_method: Optional[Callable] = None
builtins.draw_method: Optional[Callable] = None
builtins.mouse_clicked_method: Optional[Callable] = None
builtins.mouse_pressed_method: Optional[Callable] = None
builtins.mouse_released_method: Optional[Callable] = None
builtins.mouse_moved_method: Optional[Callable] = None
builtins.mouse_dragged_method: Optional[Callable] = None
builtins.key_pressed_method: Optional[Callable] = None
builtins.key_released_method: Optional[Callable] = None


vertices      = []
curvevertices = []
shape         = None
    

def draw():
    pass

def setup():
    pass

def mouseClicked():
    pass

def mousePressed():
    pass

def mouseReleased():
    pass

def mouseMoved():
    pass

def mouseDragged():
    pass   
        
def keyPressed():
    pass

def keyReleased():
    pass
    

def run():    # Run a sketch.
    
    # get the user-defined function: setup(), draw(), etc

    if hasattr(__main__, "setup"):
        builtins.setup_method = __main__.setup
    else:
        builtins.setup_method = setup

    if hasattr(__main__, "draw"):
        builtins.draw_method = __main__.draw
    else:
        builtins.draw_method = draw
        
    if hasattr(__main__, "mouseClicked"):
        builtins.mouse_clicked_method = __main__.mouseClicked        
    else:
        builtins.mouse_clicked_method = mouseClicked
        
    if hasattr(__main__, "mousePressed"):
        builtins.mouse_pressed_method = __main__.mousePressed           
    else:
        builtins.mouse_pressed_method = mousePressed    

    if hasattr(__main__, "mouseReleased"):
        builtins.mouse_released_method = __main__.mouseReleased           
    else:
        builtins.mouse_released_method = mouseReleased 
    
    if hasattr(__main__, "mouseMoved"):
        builtins.mouse_moved_method = __main__.mouseMoved           
    else:
        builtins.mouse_moved_method = mouseMoved

    if hasattr(__main__, "mouseDragged"):
        builtins.mouse_dragged_method = __main__.mouseDragged           
    else:
        builtins.mouse_dragged_method = mouseDragged
        
    if hasattr(__main__, "keyPressed"):
        builtins.key_pressed_method = __main__.keyPressed           
    else:
        builtins.key_pressed_method = keyPressed
        
    if hasattr(__main__, "keyReleased"):
        builtins.key_released_method = __main__.keyReleased           
    else:
        builtins.key_released_method = keyReleased                
     
    _setup()
    _draw()
    pass      

def to_Color(c, a=255):
    color = None
    if (type(c) == int) and (0 <= c) and (255 >= c):
        color = Color(c, c, c)
    elif (type(c) == float) and (0 <= c) and (255 >= c):
        color = Color(int(c), int(c), int(c))
    elif (type(c) == str):
        color = Color(c)
    elif (type(c) == tuple):
        color = Color(c)
    else:
        color = Color("black")
    color.a = a
    return color

# variables
settings_stack = []
settings_copy  = {}
settings = {
    "fill_color" : "white",
    "no_fill" :   False,
    "stroke_weight" : 1,
    "stroke_color" : "black",
    "rotate_amnt" : 0,
    "scale_amnt" : 1,
    "text_size" : 24,
    "text_font" : "Arial",
    "text_bold" : False,
    "text_italic" : False,
    "origin_x" :   0,
    "origin_y" :   0,
}

# IMAGE

def loadImage(path):
    return pygame.image.load(path)

def image(img, x, y):
    pg_Screen.blit(img, (x, y))
        
def saveCanvas(filename):        
    pygame.image.save(pg_Screen, filename)

def loadPixels(image):
    return pygame.PixelArray(image)

def updatePixels(pixels):
    pixels.close()

# ENVIRONMENT
    
def cursor(type):
    pygame.mouse.set_cursor(*type)
    pass

def noCursor():
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    pass

# SHAPE

def draw_rect(surf, x, y, width, height):    
    shape = pygame.Surface((width, height)).convert_alpha()
    rect = shape.get_rect()
    background = (0, 0, 0, 0)
    shape.fill(background)    
    if (not settings["no_fill"]):
        pygame.draw.rect(shape, settings["fill_color"], rect, width=0)
    if (settings["stroke_weight"] > 0):
        pygame.draw.rect(shape, settings["stroke_color"], rect, settings["stroke_weight"])
    surf.blit(shape, (x, y))

def draw_polygon(surf, vertices):     
    if (not settings["no_fill"]):
        pygame.draw.polygon(surf, settings["fill_color"], vertices, width=0)
    if (settings["stroke_weight"] > 0):
        pygame.draw.polygon(surf, settings["stroke_color"], vertices, settings["stroke_weight"])  

def draw_circle(surf, origin, radius):
    color  = settings["fill_color"]
    stroke = settings["stroke_color"]
    thickness = settings["stroke_weight"]
    width = radius * 2
    background = (0, 0, 0, 0)
    circle = pygame.Surface((width, width)).convert_alpha()
    rect = circle.get_rect()
    circle.fill(background)
    
    pygame.draw.circle(circle, color, rect.center, radius)
    if settings["stroke_weight"] > 0:
        pygame.draw.circle(circle, stroke, rect.center, radius)
        if (not(settings["no_fill"])):
            pygame.draw.circle(circle, color, rect.center, radius - thickness)
    if (settings["no_fill"]):
        pygame.draw.circle(circle, background, rect.center, radius - thickness)
    surf.blit(circle, (origin[0] - (rect.w / 2), origin[1] - (rect.w / 2)))
    pass

def draw_ellipse(surf, x, y, width, height):
    color = settings["fill_color"]
    stroke = settings["stroke_color"]
    thickness = settings["stroke_weight"]
    background = (0, 0, 0, 0)
    ellipse = pygame.Surface((width + thickness*2, height+ thickness*2)).convert_alpha()
    rect = ellipse.get_rect()
    ellipse.fill(background)
    pygame.draw.ellipse(ellipse, color, rect)
    
    if settings["stroke_weight"] > 0:
        pygame.draw.ellipse(ellipse, stroke, rect)
        if (not(settings["no_fill"])):
            pygame.draw.ellipse(ellipse, color, (thickness, thickness, width, height))
    
    if (settings["no_fill"]):
        pygame.draw.ellipse(ellipse, background, (thickness, thickness, width, height))
    
    surf.blit(ellipse, (x - (rect.w / 2), y - (rect.h / 2)))
    pass
    
def draw_arc(surf, x, y, width, height, start_angle, stop_angle):
    color = settings["fill_color"]
    stroke = settings["stroke_color"]
    thickness = settings["stroke_weight"]
    background = (0, 0, 0, 0)
    shape = pygame.Surface((width + thickness*2, height+ thickness*2)).convert_alpha()
    rect = shape.get_rect()
    
    shape.fill(background)
    #pygame.draw.ellipse(shape, stroke, (2,2,width-2,height-2))
    
    rx = width/2 + thickness + 0.5
    ry = height/2 + thickness

    cx = rx
    cy = ry

    # Start list of polygon points
    p = [(cx, cy)]

    # Get points on arc
    for n in range(start_angle,stop_angle):
        xx = cx + int(rx*math.cos(n*math.pi/180))
        yy = cy + int(ry*math.sin(n*math.pi/180))
        p.append((xx, yy))
    p.append((cx, cy))

    # Draw pie segment
    if len(p) > 2:
        pygame.draw.polygon(shape, stroke, p)
    
        
    pygame.draw.ellipse(shape, background, (thickness, thickness, width, height))
    
    surf.blit(shape, (x - (rect.w / 2), y - (rect.h / 2)))
    pass    

def arc(x, y, w, h, start, stop):    
    draw_arc(pg_Screen, x, y, w, h, start, stop)    
    pass

def ellipse(x, y, w, h=None):
    if not h:
        h = w
    draw_ellipse(pg_Screen, x, y, w, h)
    pass

def circle(x, y, d):
    draw_circle(pg_Screen, (x, y), d/2)     
    pass

def line(x1, y1, x2, y2):
    pygame.draw.line(pg_Screen, settings["stroke_color"], (x1, y1), (x2, y2), width = settings["stroke_weight"])
    pass

def point(x, y):    
    pygame.draw.circle(pg_Screen, settings["stroke_color"], (x, y), settings["stroke_weight"], 0)
    pass

def quad(x1, y1, x2, y2, x3, y3, x4, y4):
    draw_polygon(pg_Screen,((x1, y1), (x2, y2), (x3, y3), (x4, y4)))
    pass

def rect(x, y, w, h):
    draw_rect(pg_Screen,x, y, w, h)
    pass

def square(x, y, s):
    draw_rect(pg_Screen,x, y, s, s)
    pass

def triangle(x1, y1, x2, y2, x3, y3):
    draw_polygon(pg_Screen,((x1, y1), (x2, y2), (x3, y3)))
    pass

def text(txt, x,y):
    font = pygame.font.SysFont(settings["text_font"], settings["text_size"], settings["text_bold"],  settings["text_italic"])
    txtsurf = font.render(txt, True, settings["fill_color"])
    pg_Screen.blit(txtsurf,(settings["origin_x"] + x, settings["origin_y"] + y))
    pass

def textStyle(style):
    if style == "bold":
           settings["text_bold"] = True 
    if style == "italic":
           settings["text_italic"] = True 
    if style == "bolditalic":
           settings["text_bold"] = True
           settings["text_italic"] = True 
    if style == "normal":
           settings["text_bold"] = False 
           settings["text_italic"] = False
    pass
        
def textSize(size: int): # Sets the current font size
    settings["text_size"] = size
    pass
    
def textFont(font, size=None): # Set current text font.
    settings["text_font"] = font 
    settings["text_size"] = size
    pass
    
def beginShape():
    global shape, vertices, curvevertices
    shape = True
    vertices.clear()
    curvevertices.clear()
    pass

def vertex(x,y):
    global shape, vertices
    if shape:
        vertices.append((x,y))
    pass

def curveVertex(x,y):
    global shape, curvevertices
    if shape:
        curvevertices.append((x,y))
    pass    
    
def endShape(*args): # draw polygon/lines or spline curve
    global shape, vertices,curvevertices
    if len(args)==1 :
        if args[0] == "close":   
            if len(vertices) > 0:            
                draw_polygon(pg_Screen,(vertices))
            if len(curvevertices) > 0:            
                spline(pg_Screen, settings["stroke_color"], True, curvevertices,100, 0,0,0, settings["stroke_weight"])    
    else:
        if len(vertices) > 0:            
                pygame.draw.lines(pg_Screen, settings["stroke_color"], False, vertices, width = settings["stroke_weight"])
        if len(curvevertices) > 0:            
                spline(pg_Screen, settings["stroke_color"], False, curvevertices,100, 0,0,0, settings["stroke_weight"])
    shape = None
    vertices.clear()
    curvevertices.clear()
    pass        

# TRANSFORM
def rotate(angle):
    #global pgCanvas
    #pgCanvas = pygame.transform.rotate(pgCanvas, angle)
    settings["rotate_amnt"] += angle
    pass

def scale(amnt):
    settings["scale_amnt"] = amnt
    pass    

def translate(x, y):
    global settings
    settings["origin_x"] = settings["origin_x"] + x
    settings["origin_y"] = settings["origin_y"] + y        
    pass

def createCanvas(w=100, h=100):
    global pg_Screen
    
    builtins.width = w
    builtins.height = h
    pg_Screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('p5-python')
    pass   
    

def noFill():
    settings["no_fill"] = True
    pass

def stroke(c):
    settings["stroke_color"] = to_Color(c)
    pass

def strokeWeight(weight):
    if (weight == 0):
        settings["stroke_weight"] = -1
    else:
        settings["stroke_weight"] = weight
    pass

def noStroke():
    settings["stroke_weight"] = -1
    pass

def isLooping():
    return builtins.is_Looping
# STRUCTURE
def push():
    global settings
    global settings_copy
    settings_copy = settings.copy()
    settings_stack.append(settings_copy)    
    pass

def pop():
    global settings
    settings = settings_stack.pop()
    pass

def frameRate(f):
    builtins.framerate = f

def loop():    
    builtins.is_Looping = True

def noLoop():    
    builtins.is_Looping = False

def angleMode(a):
    if a not in [DEGREES,RADIANS]:
        raise ValueError("AngleMode must be radians/degrees")
    builtins.ANGLEMODE = a
    pass    

def randomseed(a:int):
    builtins.RANDOMSEED = a
    random.seed(a)
    pass

def millis():
    return milli_sec() - builtins.MILLIS
    pass

def keyIsDown(key):
     return (builtins.key == key)     
    
def _setup():

    global clock         
    pygame.init()
    builtins.MILLIS = milli_sec()
    builtins.setup_method()
    clock = pygame.time.Clock()       


def _draw():
    
    #events manager 
    def _keyPressed(ekey):
        builtins.keyCode = ekey
        builtins.key=pygame.key.name(ekey)
        builtins.key_pressed_method()
    pass
    
    def _keyReleased(ekey):
        builtins.keyCode = ekey
        builtins.key=pygame.key.name(ekey)       
        builtins.key_released_method()
    pass  

    def _mousePressed():       
        builtins.mouse_clicked_method()
        builtins.mouse_pressed_method()
    pass  

    global clock
    doLoop = builtins.is_Looping

    cntLoop = 0

    while True:
        while (doLoop or cntLoop == 0):
            builtins.pmouseX = builtins.mouseX
            builtins.pmouseY = builtins.mouseY
            builtins.mouseX, builtins.mouseY = pygame.mouse.get_pos()
            builtins.movedX = builtins.mouseX - builtins.pmouseX
            builtins.movedY = builtins.mouseY - builtins.pmouseY
            
            if (builtins.movedX != 0) or (builtins.movedY != 0) :
                if builtins.mouseIsPressed :
                    builtins.mouse_dragged_method()
                else:
                    builtins.mouse_moved_method()                                       
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    doLoop = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    _keyPressed(event.key)
                elif event.type == pygame.KEYUP:
                    _keyPressed(event.key)
                    _keyReleased(event.key)    
                elif event.type == pygame.MOUSEBUTTONUP:
                    builtins.mouseIsPressed = False
                    builtins.mouse_released_method()
                elif event.type == pygame.MOUSEBUTTONDOWN:                    
                    builtins.mouseIsPressed = True
                    mouse_button = pygame.mouse.get_pressed()
                    builtins.mouseButton = None
                    if mouse_button[0] :
                        builtins.mouseButton = "left"
                    elif mouse_button[1] :
                        builtins.mouseButton = "center"
                    elif mouse_button[2] :
                        builtins.mouseButton = "right" 
                    _mousePressed()
                elif event.type == pygame.MOUSEMOTION:
                    if (not builtins.mouseIsPressed):
                        pass 
                                                       
            builtins.draw_method()
           
            pygame.display.flip()
                    
            cntLoop = 1
            clock.tick(builtins.framerate)
 
# COLOR
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



@dispatch(tuple)
def background(c):

    x = to_Color(c)
    pg_Screen.fill(x)
    pass

@dispatch(tuple, int)
def background(c, a):

    x = to_Color(c, a)
    pg_Screen.fill(x)
    pass
    
@dispatch(int)
def background(c):

    x = to_Color(c)
    pg_Screen.fill(x)
    pass

@dispatch(int, int)
def background(c, a):

    x = to_Color(c, a)
    pg_Screen.fill(x)
    pass

@dispatch(str)
def background(c):

    x = to_Color(c)
    pg_Screen.fill(x)
    pass

@dispatch(str, int)
def background(c, a):

    x = to_Color(c, a)
    pg_Screen.fill(x)
    pass

@dispatch(float)
def background(c):

    x = to_Color(c)
    pg_Screen.fill(x)
    pass

@dispatch(float, int)
def background(c, a):

    x = to_Color(c, a)
    pg_Screen.fill(x)
    pass

@dispatch(int, int, int)
def background(r, g, b):

    x = to_Color((r, g, b))
    pg_Screen.fill(x)
    pass

@dispatch(int, int, int, int)
def background(r, g, b, a):

    x = to_Color((r, g, b), a)
    pg_Screen.fill(x)
    pass

@dispatch(int)
def fill(c):
    settings["fill_color"] = to_Color(c)
    settings["no_fill"] = False
    pass

@dispatch(int, int)
def fill(c, a):
    settings["fill_color"] = to_Color(c, a)
    settings["no_fill"] = False
    pass

@dispatch(float)
def fill(c):
    settings["fill_color"] = to_Color(c)
    settings["no_fill"] = False
    pass

@dispatch(float, int)
def fill(c, a):
    settings["fill_color"] = to_Color(c, a)
    settings["no_fill"] = False
    pass

@dispatch(str)
def fill(c):
    settings["fill_color"] = to_Color(c)
    settings["no_fill"] = False
    pass

@dispatch(str, int)
def fill(c, a):
    settings["fill_color"] = to_Color(c, a)
    settings["no_fill"] = False
    pass

@dispatch(tuple)
def fill(c):
    settings["fill_color"] = to_Color(c)
    settings["no_fill"] = False
    pass

@dispatch(tuple, int)
def fill(c, a):
    settings["fill_color"] = to_Color(c, a)
    settings["no_fill"] = False
    pass

@dispatch(int, int, int)
def fill(r, g, b):
    settings["fill_color"] = to_Color((r, g, b))
    settings["no_fill"] = False
    pass

@dispatch(int, int, int, int)
def fill(r, g, b, a):
    settings["fill_color"] = to_Color((r, g, b), a)
    settings["no_fill"] = False
    pass

