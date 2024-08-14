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
    if scale_xy == 0: scale_xy = 1
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.scale(scale_xy, scale_xy)
    ctx.rotate(rotate_angle)
    ctx.set_line_width(thickness)
    ctx.move_to(x1, y1)
    ctx.line_to(x2, y2)
    if not(settings["no_stroke"]):
        ctx.set_source_rgba(*bgra(stroke_color))
        ctx.stroke()

def draw_rect(surface, x, y, width, height):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    if scale_xy == 0: scale_xy = 1 
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.scale(scale_xy, scale_xy)
    ctx.rotate(rotate_angle)
    ctx.rectangle(x, y, width, height)
    ctx.set_line_width(thickness)
    if not(settings["no_fill"]):
        ctx.set_source_rgba(*bgra(fill_color))
        ctx.fill_preserve() 
    if not(settings["no_stroke"]):
        ctx.set_source_rgba(*bgra(stroke_color))
        ctx.stroke()

def draw_polygon(surface, vertices):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    if scale_xy == 0: scale_xy = 1
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.scale(scale_xy, scale_xy)
    ctx.rotate(rotate_angle)
    ctx.move_to(*vertices[0])
    for n in range(1,len(vertices)):
        ctx.line_to(*vertices[n])    
    ctx.close_path() 
    ctx.set_line_width(thickness)
    if not(settings["no_fill"]):
        ctx.set_source_rgba(*bgra(fill_color))
        ctx.fill_preserve()
    if not(settings["no_stroke"]):
        ctx.set_source_rgba(*bgra(stroke_color))
        ctx.stroke()

def draw_lines(surface, vertices):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    if scale_xy == 0: scale_xy = 1
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.scale(scale_xy, scale_xy)
    ctx.rotate(rotate_angle)
    ctx.move_to(*vertices[0])
    for n in range(1,len(vertices)):
        ctx.line_to(*vertices[n])
    ctx.set_line_width(thickness)
    if not(settings["no_stroke"]):
        ctx.set_source_rgba(*bgra(stroke_color))
        ctx.stroke()
    
def draw_circle(surface, x, y, radius):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    if scale_xy == 0: scale_xy = 1
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)    
    ctx.translate(origin_x, origin_y)
    ctx.rotate(rotate_angle)
    ctx.scale(scale_xy, scale_xy)
    ctx.arc(x, y, radius, 0, 2.0 * math.pi)
    ctx.set_line_width(thickness)
    if not(settings["no_fill"]):
        ctx.set_source_rgba(*bgra(fill_color))
        ctx.fill_preserve() 
    if not(settings["no_stroke"]):
        ctx.set_source_rgba(*bgra(stroke_color))
        ctx.stroke()

def draw_ellipse(surface, x, y, width, height):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    if scale_xy == 0: scale_xy = 1
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.scale(scale_xy, scale_xy)
    ctx.rotate(rotate_angle)   
    radius = width/2
    scale_x = 1.0
    scale_y = height / width
    ctx.save()
    ctx.scale(scale_x, scale_y)
    ctx.arc(x, y/scale_y, radius, 0, 2.0 * math.pi)
    ctx.set_line_width(thickness)
    if not(settings["no_fill"]):
        ctx.set_source_rgba(*bgra(fill_color))
        ctx.fill_preserve() 
    if not(settings["no_stroke"]):
        ctx.set_source_rgba(*bgra(stroke_color))
        ctx.stroke()    
    ctx.restore()
    
def draw_arc(surface, x, y, width, height, angle1, angle2, mode):           
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    if scale_xy == 0: scale_xy = 1
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.scale(scale_xy, scale_xy)
    ctx.rotate(rotate_angle)   
    if mode == "pie":
        ctx.move_to(x, y)
    radius = width/2
    scale_x = 1.0
    scale_y = height / width
    ctx.save()
    ctx.scale(scale_x, scale_y)        
    ctx.arc(x, y/scale_y, radius, angle1, angle2)
    if (mode == "chord") or (mode == "pie"):
        ctx.close_path()
    if (mode == "chord") or (mode == "pie") or (mode == "open"):
        if not(settings["no_fill"]):
            ctx.set_source_rgba(*bgra(fill_color))
            ctx.fill_preserve()
    if not(settings["no_stroke"]):
        ctx.set_source_rgba(*bgra(stroke_color))
        ctx.stroke()
    ctx.restore()
    
def draw_text(surface, txt, x, y, style):
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    if scale_xy == 0: scale_xy = 1
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["text_outline"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["text_color"]
    font_name    = settings["text_font"] 
    font_size    = settings["text_size"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.scale(scale_xy, scale_xy)
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
    if not(settings["no_stroke"]):
        ctx.set_source_rgba(*bgra(stroke_color))
        i = -thickness
        while i < thickness-0.3 :
            j =-thickness
            while j < thickness-0.3 :
                ctx.move_to(x + i, y + j)
                ctx.show_text(txt)
                j = j + 0.2
            i = i + 0.2            
    if not(settings["no_fill"]):
        ctx.set_source_rgba(*bgra(fill_color))
        ctx.fill_preserve()
    ctx.move_to(x, y)
    ctx.show_text(txt)
    if not(settings["no_stroke"]):
        ctx.set_source_rgba(*bgra(stroke_color))
        ctx.stroke()  

def draw_spline(surface, curvevertices, mode):
    vertices =[]
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    if scale_xy == 0: scale_xy = 1
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["text_outline"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["text_color"]
    font_name    = settings["text_font"] 
    font_size    = settings["text_size"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.scale(scale_xy, scale_xy)
    ctx.rotate(rotate_angle)
    ctx.set_line_width(thickness)  
    vertices = list(curvevertices)
    ctx.move_to(vertices[0][0],vertices[0][1] )
    vertices_length = len(vertices)
    cached_vertices = []
    curTightness = 0
    if vertices_length >  0:
      # closeShape = mode 
      # if the shape is closed, the first element is also the last element
        if mode:
            vertices.append(vertices[0])
        # curveVertex -> bezierVertex
        if  vertices_length > 3 :
            b = [None,None,None,None]
            s = 1 - curTightness;
            '''
            Matrix to convert from Catmull-Rom to cubic Bezier
            where t = curTightness
            |0         1          0         0       |
            |(t-1)/6   1          (1-t)/6   0       |
            |0         (1-t)/6    1         (t-1)/6 |
            |0         0          0         0       |
            '''
            i = 1
            while (i+2 < vertices_length):          
                cached_vertices = vertices[i]
                b[0] = [cached_vertices[0], cached_vertices[1]]
                b[1] = [cached_vertices[0] + (s * vertices[i+1][0] - s * vertices[i-1][0]) / 6, \
                       cached_vertices[1] + (s * vertices[i+1][1] - s * vertices[i-1][1]) / 6]
                b[2] = [vertices[i+1][0] + (s * vertices[i][0] - s * vertices[i+2][0]) / 6, \
                       vertices[i+1][1] + (s * vertices[i][1] - s * vertices[i+2][1]) / 6]
                b[3] = [vertices[i+1][0], vertices[i+1][1]]
                i = i + 1
                ctx.curve_to(b[1][0], b[1][1], b[2][0], b[2][1], b[3][0], b[3][1]) # draw bezier curve
    if mode:
        ctx.line_to(vertices[0][0],vertices[0][1])
    
    if not(settings["no_fill"]):
        ctx.set_source_rgba(*bgra(fill_color))
        #ctx.fill_preserve() 
    if not(settings["no_stroke"]):
        ctx.set_source_rgba(*bgra(stroke_color)) 
    ctx.stroke()
    
    pass
# end of draw_spline

def draw_bezier(surface, x, y, bezier_vertices, mode):
  
    rotate_angle = a_radians(settings["rotate_amnt"])
    scale_xy     = settings["scale_amnt"]
    if scale_xy == 0: scale_xy = 1
    origin_x     = settings["real_ox"]
    origin_y     = settings["real_oy"]
    stroke_color = settings["stroke_color"] 
    thickness    = settings["stroke_weight"]
    fill_color   = settings["fill_color"]
    ctx = cairo.Context(surface)
    ctx.translate(origin_x, origin_y)
    ctx.scale(scale_xy, scale_xy)
    ctx.rotate(rotate_angle)
    ctx.set_line_width(thickness)
    ctx.move_to(x, y)
    for i in range(len(bezier_vertices)):
        b = bezier_vertices[i]        
        ctx.curve_to(*b) # draw bezier curve
        
    if mode:
        ctx.line_to(x, y)
    if not(settings["no_fill"]):
        ctx.set_source_rgba(*bgra(fill_color))
        ctx.fill_preserve() 
    if not(settings["no_stroke"]):
        ctx.set_source_rgba(*bgra(stroke_color)) 
        ctx.stroke()
