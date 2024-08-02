import pygame
import numpy as np
import math
import sys
import types
import __main__
import builtins
from pygame import Color
from functools import wraps
from multipledispatch import dispatch
from typing import Callable, Optional
from p5.constants import *

class Image(pygame.Surface):
    def __init__(self):
        pass
        
pgWindow = None
pgCanvas = None
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
builtins.isLooping      = True

builtins.setup_method: Optional[Callable] = None
builtins.draw_method: Optional[Callable] = None
builtins.mouse_clicked_method: Optional[Callable] = None
builtins.mouse_pressed_method: Optional[Callable] = None
builtins.mouse_released_method: Optional[Callable] = None
builtins.mouse_moved_method: Optional[Callable] = None
builtins.mouse_dragged_method: Optional[Callable] = None
builtins.key_pressed_method: Optional[Callable] = None
builtins.key_released_method: Optional[Callable] = None


vertices =[]
shape = None
    

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

def _usrColor(c, a=255):
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
    if (pgCanvas):
        pgCanvas.blit(img, (x, y))
        
def saveCanvas(filename):        
    pygame.image.save(pgCanvas, filename)

# ENVIRONMENT
    
def cursor(type):
    pygame.mouse.set_cursor(*type)
    pass

def noCursor():
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    pass

# SHAPE
def _filledArc(r, start, stop):
    # arc_image = np.zeros((r.height, r.width, 3), dtype = np.uint8)
    # cf = settings["fill_color"]
    # cv.ellipse(arc_image, r.center, (r.height, r.width), 0, math.degrees(start), math.degrees(stop), 0)

    # img = pygame.image.frombuffer(arc_image, r.size, "RGB")
    # print("hello")
    # pgCanvas.blit(img, img.get_rect(center=r.center))
    # return
    pass
  
def _filledShape(func, *args, **kwargs):
    if (pgCanvas):
        if (not settings["no_fill"]):
            func(pgCanvas, settings["fill_color"], *args, **kwargs, width=0)
    
        if (settings["stroke_weight"] > 0):
            func(pgCanvas, settings["stroke_color"], *args, **kwargs, width=settings["stroke_weight"])
    return
    
def arc(x, y, w, h, start, stop):
    r = pygame.Rect(x-w/2, y-h/2, w, h)
    _filledArc(r, start, stop)
    pass

def ellipse(x, y, w, h=None):
    if not h:
        h = w
    
    r = pygame.Rect(x-w/2, y-h/2, w, h)
    _filledShape(pygame.draw.ellipse, r)
    pass

def circle(x, y, d):
    _filledShape(pygame.draw.circle, (x, y), d/2)
    pass

def line(x1, y1, x2, y2):
    if (pgCanvas):
        pygame.draw.line(pgCanvas, settings["stroke_color"], (x1, y1), (x2, y2), width=1)
    pass

def point(x, y):
    _filledShape(pygame.draw.circle, (x, y), 1)
    pass

def quad(x1, y1, x2, y2, x3, y3, x4, y4):
    _filledShape(pygame.draw.polygon, ((x1, y1), (x2, y2), (x3, y3), (x4, y4)))
    pass

def rect(x, y, w, h):
    r = pygame.Rect(x, y, w, h)
    _filledShape(pygame.draw.rect, r)
    pass

def square(x, y, s):
    r = pygame.Rect(x, y, s, s)
    _filledShape(pygame.draw.rect, r)
    pass

def triangle(x1, y1, x2, y2, x3, y3):
    _filledShape(pygame.draw.polygon, ((x1, y1), (x2, y2), (x3, y3)))
    pass

def text(txt, x,y):
    font = pygame.font.SysFont(settings["text_font"], settings["text_size"], settings["text_bold"],  settings["text_italic"])
    txtsurf = font.render(txt, True, settings["fill_color"])
    pgCanvas.blit(txtsurf,(settings["origin_x"] + x, settings["origin_y"] + y))
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
    global shape, vertices
    shape = True
    vertices.clear()
    pass

def vertex(x,y):
    global shape, vertices
    if shape:
        vertices.append((x,y))
    pass
    
def endShape():
    global shape, vertices    
    _filledShape(pygame.draw.polygon, (vertices))
    shape = None
    pass        

# TRANSFORM
def rotate(angle):
    global pgCanvas
    pgCanvas = pygame.transform.rotate(pgCanvas, angle)
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
    global pgWindow
    global pgCanvas
    
    builtins.width = w
    builtins.height = h
    pgWindow = pygame.display.set_mode((w, h))
    pygame.display.set_caption('p5py')
    pgCanvas = pygame.Surface(pgWindow.get_size(), pygame.SRCALPHA)
    pass   
    

def noFill():
    settings["no_fill"] = True
    pass

def stroke(c):
    settings["stroke_color"] = _usrColor(c)
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
    builtins.isLooping = True

def noLoop():    
    builtins.isLooping = False

def _setup():

    global clock         
    pygame.init()
    builtins.setup_method()
    clock = pygame.time.Clock()       

def keyIsDown(key):
     return (builtins.key == key)     

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

    global pgWindow
    global pgCanvas
    global clock
    doLoop = builtins.isLooping

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

            if (pgWindow and pgCanvas):
                pgWindow.blit(pgCanvas, (settings["origin_x"], settings["origin_y"]))
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
    if (pgCanvas):
        x = _usrColor(c)
        pgCanvas.fill(x)
    pass

@dispatch(tuple, int)
def background(c, a):
    if (pgCanvas):
        x = _usrColor(c, a)
        pgCanvas.fill(x)
    pass
    
@dispatch(int)
def background(c):
    if (pgCanvas):
        x = _usrColor(c)
        pgCanvas.fill(x)
    pass

@dispatch(int, int)
def background(c, a):
    if (pgCanvas):
        x = _usrColor(c, a)
        pgCanvas.fill(x)
    pass

@dispatch(str)
def background(c):
    if (pgCanvas):
        x = _usrColor(c)
        pgCanvas.fill(x)
    pass

@dispatch(str, int)
def background(c, a):
    if (pgCanvas):
        x = _usrColor(c, a)
        pgCanvas.fill(x)
    pass

@dispatch(float)
def background(c):
    if (pgCanvas):
        x = _usrColor(c)
        pgCanvas.fill(x)
    pass

@dispatch(float, int)
def background(c, a):
    if (pgCanvas):
        x = _usrColor(c, a)
        pgCanvas.fill(x)
    pass

@dispatch(int, int, int)
def background(r, g, b):
    if (pgCanvas):
        x = _usrColor((r, g, b))
        pgCanvas.fill(x)
    pass

@dispatch(int, int, int, int)
def background(r, g, b, a):
    if (pgCanvas):
        x = _usrColor((r, g, b), a)
        pgCanvas.fill(x)
    pass

@dispatch(int)
def fill(c):
    settings["fill_color"] = _usrColor(c)
    settings["no_fill"] = False
    pass

@dispatch(int, int)
def fill(c, a):
    settings["fill_color"] = _usrColor(c, a)
    settings["no_fill"] = False
    pass

@dispatch(float)
def fill(c):
    settings["fill_color"] = _usrColor(c)
    settings["no_fill"] = False
    pass

@dispatch(float, int)
def fill(c, a):
    settings["fill_color"] = _usrColor(c, a)
    settings["no_fill"] = False
    pass

@dispatch(str)
def fill(c):
    settings["fill_color"] = _usrColor(c)
    settings["no_fill"] = False
    pass

@dispatch(str, int)
def fill(c, a):
    settings["fill_color"] = _usrColor(c, a)
    settings["no_fill"] = False
    pass

@dispatch(tuple)
def fill(c):
    settings["fill_color"] = _usrColor(c)
    settings["no_fill"] = False
    pass

@dispatch(tuple, int)
def fill(c, a):
    settings["fill_color"] = _usrColor(c, a)
    settings["no_fill"] = False
    pass

@dispatch(int, int, int)
def fill(r, g, b):
    settings["fill_color"] = _usrColor((r, g, b))
    settings["no_fill"] = False
    pass

@dispatch(int, int, int, int)
def fill(r, g, b, a):
    settings["fill_color"] = _usrColor((r, g, b), a)
    settings["no_fill"] = False
    pass

