# TRANSFORM
from p5.settings import *
import math
import builtins

def transform_canvas_reset(): # Transformations are reset at the beginning of the draw loop.
    global settings
    settings["rotate_amnt"] = 0
    settings["scale_amnt"]  = 0
    settings["origin_x"]    = 0
    settings["origin_y"]    = 0
    settings["real_ox"]     = 0
    settings["real_oy"]     = 0 
    pass

def resetMatrix():
    transform_canvas_reset()
        
def rotate(angle):
    current_angle = settings["rotate_amnt"]
    current_angle += angle
    if builtins.ANGLEMODE == DEGREES:
        if current_angle < 0:
            current_angle = 360 + current_angle
        if current_angle > 359:
            current_angle = current_angle % 360
        settings["rotate_amnt"] = current_angle          
    pass

def scale(amnt):
    settings["scale_amnt"] = settings["scale_amnt"] + amnt
    pass    

def real_oxy(xx,yy):   # calulate real x,y coordinate    
    aa = settings["rotate_amnt"]
    ox = settings["real_ox"]
    oy = settings["real_oy"]
    x = xx
    y = yy
    if builtins.ANGLEMODE == DEGREES:
        aa = aa * math.pi/180
    x = ox + int(xx * math.cos(aa)) - int(yy * math.sin(aa))
    y = oy + int(yy * math.cos(aa)) + int(xx * math.sin(aa))   
    settings["real_ox"] = x
    settings["real_oy"] = y 
    pass


def translate(x, y):
    global settings
    settings["origin_x"] = settings["origin_x"] + x
    settings["origin_y"] = settings["origin_y"] + y 
    real_oxy(x, y) # calculate real origin x,y
       
    pass

def push():
    global stack,settings    
    r  = settings["rotate_amnt"]
    s  = settings["scale_amnt"]
    ox = settings["origin_x"]
    oy = settings["origin_y"]
    rox= settings["real_ox"]
    roy= settings["real_oy"]
    stack.append(r)
    stack.append(s)
    stack.append(ox)
    stack.append(oy)
    stack.append(rox)
    stack.append(roy)
        
def pop():
    global stack,settings
    settings["real_oy"]     = stack.pop()
    settings["real_ox"]     = stack.pop()     
    settings["origin_y"]    = stack.pop()
    settings["origin_x"]    = stack.pop()
    settings["scale_amnt"]  = stack.pop() 
    settings["rotate_amnt"] = stack.pop()
    
