import math
import cairo
from p5.settings import *

def bgra(color): #convert color RGBA 0-255 to BGRA 0-1
    b_g_r_a = [0,0,0,0]
    b_g_r_a[0] = color[2]/255
    b_g_r_a[1] = color[1]/255
    b_g_r_a[2] = color[0]/255

    if len(color)<4:
        b_g_r_a[3] = 1    
    else:
        b_g_r_a[3] = color[3]/255    
    return b_g_r_a   

def a_radians(a):
    if builtins.ANGLEMODE == DEGREES:
        return a * math.pi/180
    else:
        return a  
def clear_background(surface, width, height, color):
    
    ctx = cairo.Context(surface)
    ctx.set_source_rgba(*bgra(color))
    ctx.rectangle(0, 0, width, height)
    ctx.fill()

def draw_line(surface, x1, y1, x2, y2):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.rotate(rotate_angle)
    ctx.set_line_width(thickness)
    ctx.move_to(x1, y1)
    ctx.line_to(x2, y2)
    ctx.set_source_rgba(*bgra(stroke_color))
    ctx.stroke()

def draw_rect(surface, x, y, width, height):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.rotate(rotate_angle)
    ctx.rectangle(x, y, width, height)
    ctx.set_line_width(thickness)
    ctx.set_source_rgba(*bgra(fill_color))
    ctx.fill_preserve() 
    ctx.set_source_rgba(*bgra(stroke_color))
    ctx.stroke()

def draw_polygon(surface, vertices):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.rotate(rotate_angle)
    ctx.move_to(*vertices[0])
    for n in range(1,len(vertices)):
        ctx.line_to(*vertices[n])    
    ctx.close_path() 
    ctx.set_line_width(thickness)
    ctx.set_source_rgba(*bgra(fill_color))
    ctx.fill_preserve() 
    ctx.set_source_rgba(*bgra(stroke_color))
    ctx.stroke()

def draw_lines(surface, vertices):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.rotate(rotate_angle)
    ctx.move_to(*vertices[0])
    for n in range(1,len(vertices)):
        ctx.line_to(*vertices[n])
    ctx.set_line_width(thickness)
    ctx.set_source_rgba(*bgra(stroke_color))
    ctx.stroke()
    
def draw_circle(surface, x, y, radius):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)    
    ctx.translate(origin_x, origin_y)
    ctx.rotate(rotate_angle)
    ctx.arc(x, y, radius, 0, 2.0 * math.pi)
    ctx.set_line_width(thickness)
    ctx.set_source_rgba(*bgra(fill_color))
    ctx.fill_preserve() 
    ctx.set_source_rgba(*bgra(stroke_color))
    ctx.stroke()

def draw_ellipse(surface, x, y, width, height):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.rotate(rotate_angle)   
    radius = width/2
    scale_x = 1.0
    scale_y = height / width
    ctx.scale(scale_x, scale_y)
    ctx.arc(x, y/scale_y, radius, 0, 2.0 * math.pi)
    ctx.set_line_width(thickness)
    ctx.set_source_rgba(*bgra(fill_color))
    ctx.fill_preserve() 
    ctx.set_source_rgba(*bgra(stroke_color))
    ctx.stroke()    
    
def draw_arc(surface, x, y, width, height, angle1, angle2, mode):           
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.rotate(rotate_angle)   
    if mode == "pie":
        ctx.move_to(x, y)
    radius = width/2
    scale_x = 1.0
    scale_y = height / width
    ctx.scale(scale_x, scale_y)        
    ctx.arc(x, y/scale_y, radius, angle1, angle2)
    if (mode == "chord") or (mode == "pie"):
        ctx.close_path()
    if (mode == "chord") or (mode == "pie") or (mode == "open"):
        ctx.set_source_rgba(*bgra(fill_color))
        ctx.fill_preserve()
    ctx.set_source_rgba(*bgra(stroke_color))
    ctx.stroke()

def draw_text(surface, txt, x, y, style):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["text_outline"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["text_color"]
    font_name    = settings["text_font"] 
    font_size    = settings["text_size"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.rotate(rotate_angle)    
    font_options = cairo.FontOptions()
    font_options.set_antialias(cairo.ANTIALIAS_DEFAULT)
    ctx.set_font_options(font_options)
    cairo_slant  = cairo.FONT_SLANT_NORMAL
    cairo_weight = cairo.FONT_WEIGHT_NORMAL
    if style == "italic" or style == "bolditalic":
        cairo_slant = cairo.FONT_SLANT_ITALIC
    if style == "bold" or style == "bolditalic":
        cairo_weight = cairo.FONT_WEIGHT_BOLD
    ctx = cairo.Context(surface)        
    ctx.select_font_face(font_name, cairo_slant,cairo_weight)
    ctx.set_font_size(font_size)
    xbearing, ybearing, width, height, dx, dy = ctx.text_extents(txt)
    if settings["text_align"] == RIGHT:
        x = x - width 
    if settings["text_align"] == CENTER:
        x = x - width/2    
    # Render outline
    ctx.set_source_rgba(*bgra(stroke_color))
    for i in range(-thickness, thickness+1):
        for j in range(-thickness, thickness+1):
            ctx.move_to(x + i, y + j)
            ctx.show_text(txt)
    
    ctx.set_source_rgba(*bgra(fill_color))
    ctx.move_to(x, y)
    ctx.show_text(txt)
    ctx.stroke()   
'''    
def draw_curve(surface,color):    
    x, y = 100, 50
    x1, y1 = 140, 50
    x2, y2 = 60, 100
    x3, y3 = 190, 150
    ctx = cairo.Context(surface)
    ctx.move_to(x, y)
    ctx.curve_to(x1, y1, x2, y2, x3, y3)
    ctx.set_source_rgba(*bgra(color))
    ctx.stroke()
'''    
    
