import pygame
#import pygame.gfxdraw
import math
import sys
import types
import random
import __main__
import builtins
from typing import Callable, Optional
from p5.constants import *
from p5.timedata import *
from p5.drawcurve import *
from p5.settings import *
from p5.color import *
from p5.transform import *
  

builtins.setup_method: Optional[Callable] = None
builtins.draw_method: Optional[Callable] = None
builtins.mouse_clicked_method: Optional[Callable] = None
builtins.mouse_pressed_method: Optional[Callable] = None
builtins.mouse_released_method: Optional[Callable] = None
builtins.mouse_moved_method: Optional[Callable] = None
builtins.mouse_dragged_method: Optional[Callable] = None
builtins.key_pressed_method: Optional[Callable] = None
builtins.key_released_method: Optional[Callable] = None
 

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

def angle_RAD(a):
    if builtins.ANGLEMODE == DEGREES:
        return a * math.pi/180
    else:
        return a    

def angle_DEG(a):
    if builtins.ANGLEMODE == RADIANS:
        return a * 180 / math.pi
    else:
        return a 

# SHAPE
def cxy(xx,yy):   # transform x,y coordinate
    global settings
    a  = settings["rotate_amnt"]
    s  = settings["scale_amnt"]
    ox = settings["origin_x"]
    oy = settings["origin_y"]
    x = xx
    y = yy
    if a > 0 :
        aa = angle_RAD(a)
        x = int(xx * math.cos(aa)) - int(yy * math.sin(aa))
        y = int(yy * math.cos(aa)) + int(xx * math.sin(aa))
    if s != 1 :
        x = x * s
        y = y * s
    if (ox != 0) or (oy != 0):
        x = x + ox
        y = y + oy     
    return (x, y)
    pass

def ctxy(c):    # transform tuple x,y coordinate
    tmp = []
    for i in range(len(c)):
        tmp.append(cxy(c[i][0],c[i][1]))
    return tmp  
        
def draw_rect(surf, x, y, w, h):
    x2 = x + w
    y2 = y
    x3 = x2
    y3 = y + h
    x4 = x
    y4 = y3   
    if (settings["no_fill"] == False):
        pygame.draw.polygon(surf, settings["fill_color"], ctxy([(x,y),(x2,y2),(x3,y3),(x4, y4)]), width=0)
    if (settings["stroke_weight"]) > 0 and (settings["no_stroke"] == False):        
        pygame.draw.polygon(surf, settings["stroke_color"], ctxy([(x,y),(x2,y2),(x3,y3),(x4, y4)]),  int(settings["stroke_weight"]*settings["scale_amnt"]))


def draw_polygon(surf, vertices):     
    if (settings["no_fill"] == False):
        pygame.draw.polygon(surf, settings["fill_color"], ctxy(vertices), width=0)
    if (settings["stroke_weight"]) > 0 and (settings["no_stroke"] == False):
        pygame.draw.polygon(surf, settings["stroke_color"], ctxy(vertices), int(settings["stroke_weight"]*settings["scale_amnt"]))  

def draw_circle(surf, origin, radius):
    color  = settings["fill_color"]
    stroke = settings["stroke_color"]
    thickness = settings["stroke_weight"]
    scale = settings["scale_amnt"]
    radius = radius * scale
    width = radius * 2 + + 2*thickness*scale
    origin = cxy(origin[0],origin[1])
    background = (0, 0, 0, 0)
    circle = pygame.Surface((width, width)).convert_alpha()
    rect = circle.get_rect()
    circle.fill(background)
    
    pygame.draw.circle(circle, color, rect.center, radius + thickness*scale)
    if (settings["stroke_weight"]) > 0 and (settings["no_stroke"] == False):
        pygame.draw.circle(circle, stroke, rect.center, radius + thickness*scale)
    if (not(settings["no_fill"])):
            pygame.draw.circle(circle, color, rect.center, radius)
    if (settings["no_fill"]):
        pygame.draw.circle(circle, background, rect.center, radius)
    surf.blit(circle, (origin[0] - (rect.w / 2), origin[1] - (rect.w / 2)))
    pass

def ellipse_array(x, y, width, height,thickness,scale):
    rx = (width/2  + thickness)*scale
    ry = (height/2 + thickness) * scale

    cx = x * scale
    cy = y * scale
    
    pts =[]
    # Get points on ellipse
    for n in range(0,360):
        xx = cx + int(rx*math.cos(n*math.pi/180))
        yy = cy + int(ry*math.sin(n*math.pi/180))
        pts.append((xx, yy))
    return pts

def draw_ellipse(surf, x, y, width, height):    

    ellipse_surface = pygame.Surface((builtins.width, builtins.height)).convert_alpha()
    ellipse_surface.fill((0, 0, 0, 0))
    
    color     = settings["fill_color"]
    stroke    = settings["stroke_color"]
    thickness = settings["stroke_weight"]
    scale     = settings["scale_amnt"]

    pts =[]
    # Get points on ellipse    
    pts = ellipse_array(x, y, width, height,thickness,scale)
      
    # Draw outer ellipse of stroke color
    if (settings["stroke_weight"]) > 0 and (settings["no_stroke"] == False):
        pygame.draw.polygon(ellipse_surface,stroke, ctxy(pts))
   
    # Draw inner ellipse
    pts.clear()
    # Get points on ellipse
    pts = ellipse_array(x, y, width, height,0,scale)

    if (settings["no_fill"]):
        pygame.draw.polygon(ellipse_surface,(0,0,0,0), ctxy(pts)) # inner empty ellipse
    else:
        pygame.draw.polygon(ellipse_surface,color, ctxy(pts)) # inner color filled ellipse    
    
    surf.blit(ellipse_surface, (0,0))
    pass    
    
# -----------------------------------------------------    
def draw_arc(surf, x, y, width, height, start_angle, stop_angle):

    arc_surface = pygame.Surface((builtins.width, builtins.height)).convert_alpha()
    background = (0, 0, 0, 0)
    arc_surface.fill(background)
    
    stroke    = settings["stroke_color"]
    thickness = settings["stroke_weight"]
    scale     = settings["scale_amnt"]
      
    rx = (width/2  + thickness  + 0.5)*scale
    ry = (height/2 + thickness) * scale

    cx = x * scale
    cy = y * scale

    # Start list of polygon points
    pts = [(cx, cy)]

    # Get points on arc
    for n in range(start_angle,stop_angle):
        xx = cx + int(rx*math.cos(n*math.pi/180))
        yy = cy + int(ry*math.sin(n*math.pi/180))
        pts.append((xx, yy))
    pts.append((cx, cy))

    # Draw pie segment
    if (settings["stroke_weight"]) > 0 and (settings["no_stroke"] == False):
        if len(pts) > 2:
            pygame.draw.polygon(arc_surface,stroke, ctxy(pts))
    pts.clear()
    # Get points on inner ellipse
    pts = ellipse_array(x, y, width, height, 0, scale)
    pygame.draw.polygon(arc_surface,(0,0,0,0), ctxy(pts)) # inner empty ellipse   

    surf.blit(arc_surface, (0,0))
    pass    


# ----BASIC P5 FUNCTIONS --------------------------

def arc(x, y, w, h, start, stop):    
    draw_arc(pg_Screen, x, y, w, h, angle_DEG(start), angle_DEG(stop))    
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
    if (settings["stroke_weight"]) > 0 and (settings["no_stroke"] == False):    
        pygame.draw.line(pg_Screen, settings["stroke_color"], cxy(x1, y1), cxy(x2, y2), width = int(settings["stroke_weight"]*settings["scale_amnt"]))
    pass

def point(x, y):    
    if (settings["stroke_weight"]) > 0 and (settings["no_stroke"] == False):
        pygame.draw.circle(pg_Screen, settings["stroke_color"], cxy(x, y), int(settings["stroke_weight"]*settings["scale_amnt"]), 0)
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
    txt_size = settings["text_size"]
    outline_txtsurf = font.render(txt, True, settings["stroke_color"])
    outline_txtsurf = pygame.transform.rotate(outline_txtsurf, -settings["rotate_amnt"])
    if (settings["stroke_weight"]) > 0 and (settings["no_stroke"] == False):
        # Render outline
        for i in range(-3, 4):
            for j in range(-3, 4):
                pg_Screen.blit(outline_txtsurf, cxy(x + i, y + j - txt_size ))
    if (settings["no_fill"] == False):
        txtsurf = font.render(txt, True, settings["fill_color"])
        txtsurf = pygame.transform.rotate(txtsurf, -settings["rotate_amnt"])
        pg_Screen.blit(txtsurf,cxy(x, y - txt_size))
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


def createCanvas(w=100, h=100):
    global pg_Screen
    
    builtins.width = w
    builtins.height = h
    pg_Screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('p5-python') 
    pass   
    
def background(*args): # set background color
    pg_Screen.fill(set_colors(*args))
    
def noFill():
    settings["no_fill"] = True
    pass

def stroke(*args):
    settings["stroke_color"] = set_colors(*args)
    settings["no_stroke"] = False
    pass

def strokeWeight(weight):
    settings["stroke_weight"] = weight
    pass

def noStroke():
    settings["no_stroke"] = True
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

def angleMode(amode):
    if amode not in [DEGREES,RADIANS]:
        raise ValueError("AngleMode must be radians/degrees")
    builtins.ANGLEMODE = amode
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
                                    
            transform_canvas_reset()
            builtins.draw_method()
 
            pygame.display.flip()
                    
            cntLoop = 1
            clock.tick(builtins.framerate)
# ---- END ----
