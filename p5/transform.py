# TRANSFORM
from p5.settings import *

def transform_canvas_reset(): # Transformations are reset at the beginning of the draw loop.
    global settings
    settings["rotate_amnt"] = 0
    settings["scale_amnt"]  = 1
    settings["origin_x"]    = 0
    settings["origin_y"]    = 0
    pass
    
def rotate(angle):
    current_angle = settings["rotate_amnt"]
    current_angle += angle
    if current_angle < 0:
        current_angle = 360 + current_angle
    if current_angle > 359:
        current_angle = current_angle % 360
    settings["rotate_amnt"] = current_angle          
    pass

def scale(amnt):
    settings["scale_amnt"] = amnt
    pass    

def translate(x, y):
    global settings
    settings["origin_x"] = settings["origin_x"] + x
    settings["origin_y"] = settings["origin_y"] + y        
    pass
