# Splines/Curves from PAdLib - Ian Mallett - 2013

from math import *
import pygame
# math helper
def rndint(num): return int(num+0.5)
def clamp(num, low,high):
    if num <  low: return  low
    if num > high: return high
    return num

def vec_add(v1,v2):
    return [v1[i]+v2[i] for i in range(len(v1))]
def vec_sub(v1,v2):
    return [v1[i]-v2[i] for i in range(len(v1))]
def vec_dot(v1,v2):
    return sum([v1[i]*v2[i] for i in range(len(v1))])
def vec_scale(sc,v):
    return [sc*v[i] for i in range(len(v))]
def vec_negate(v):
    return [-v[i] for i in range(len(v))]

def vec_length_sq(vec):
    return vec_dot(vec,vec)
def vec_length(vec):
    return vec_dot(vec,vec) ** 0.5
def vec_norm(vec):
    return vec_scale(1.0/vec_length(vec),vec)

def vec_reflect(vec, norm):
    v_dot_n = vec_dot(vec,norm)
    sc = 2 * v_dot_n
    return [sc*norm[i]-vec[i] for i in range(len(vec))]

def point_project_line(p, l1,l2):
    #Adapted from http://www.gamedev.net/topic/444154-closest-point-on-a-line/
    p_l1 = vec_sub(p,l1)
    l2_l1 = vec_sub(l2,l1)

    t = vec_dot(p_l1,l2_l1) / vec_dot(l2_l1,l2_l1)

    return vec_add(l1,vec_scale(t,l2_l1))

# draw bezier curve
def _draw_bezier(surface, color, controlpointslist, steps, aa, width, blend):
    #Algorithm derived from geometric animations on
    #http://en.wikipedia.org/wiki/B[e]zier_curve
    #The "[e]" is actually an e with an inflection
    #over it; removed for this file's portability.
    
    points = []
    
    def draw_curve(controlpointslist):
        l = len(controlpointslist)
        
        def lerp(p1,p2):
            return vec_add(
                vec_scale(1.0-t,p1),
                vec_scale(    t,p2)
            )
        if l == 2:
            points.append(lerp(*controlpointslist))
        else:
            controlpointslist2 = []
            for i in range(l-1):
                controlpointslist2.append(lerp(
                    controlpointslist[i],
                    controlpointslist[i+1]
                ))
            draw_curve(controlpointslist2)
                
    for i in range(steps):
        t = float(i) / float(steps-1)
        draw_curve(controlpointslist)

    if aa:
        #This function can take floating-point values for endpoints.
        pygame.draw.aalines(surface,color,False,points,blend)
    else:
        points = [list(map(rndint,p)) for p in points]
        pygame.draw.lines(surface,color,False,points,width)

#draw spline curve
def _draw_spline(surface, color, closed, pointslist, steps, t,b,c, aa, width, blend):
    #Kochanek-Bartels spline implementation, written long ago and updated.
    t_inc = 1.0/float(steps)

    #This allows us to draw through all visible control points (normal Kochanek-Bartels
    #splines do not draw through their last endpoints).
    if closed:
        pointslist = [pointslist[-2],pointslist[-1]] + pointslist + [pointslist[0],pointslist[1]]
    else:
        pointslist = [pointslist[0]] + pointslist + [pointslist[-1]]

    cona = (1-t)*(1+b)*(1-c)*0.5
    conb = (1-t)*(1-b)*(1+c)*0.5
    conc = (1-t)*(1+b)*(1+c)*0.5
    cond = (1-t)*(1-b)*(1-c)*0.5

    tans = []
    tand = []
    for x in range(len(pointslist)-2):
        tans.append([])
        tand.append([])
    i = 1
    while i < len(pointslist)-1:
        pa = pointslist[i-1]
        pb = pointslist[i  ]
        pc = pointslist[i+1]
        x1 = pb[0] - pa[0]
        y1 = pb[1] - pa[1]
        x2 = pc[0] - pb[0]
        y2 = pc[1] - pb[1]
        tans[i-1] = (cona*x1+conb*x2, cona*y1+conb*y2)
        tand[i-1] = (conc*x1+cond*x2, conc*y1+cond*y2)
        i += 1

    for i in range(1,len(pointslist)-2,1):
        p0 = pointslist[i  ]
        p1 = pointslist[i+1]
        m0 = tand[i-1]
        m1 = tans[i  ]
        
        #draw curve from p0 to p1
        points = [(p0[0],p0[1])]
        t_iter = t_inc
        while t_iter < 1.0:
            h00 = ( 2*(t_iter*t_iter*t_iter)) - ( 3*(t_iter*t_iter)) + 1
            h10 = ( 1*(t_iter*t_iter*t_iter)) - ( 2*(t_iter*t_iter)) + t_iter
            h01 = (-2*(t_iter*t_iter*t_iter)) + ( 3*(t_iter*t_iter))
            h11 = ( 1*(t_iter*t_iter*t_iter)) - ( 1*(t_iter*t_iter))
            px = h00*p0[0] + h10*m0[0] + h01*p1[0] + h11*m1[0]
            py = h00*p0[1] + h10*m0[1] + h01*p1[1] + h11*m1[1]
            points.append((px,py))
            t_iter += t_inc
        points.append((p1[0],p1[1]))
        
        if aa:
            #This function can take floating-point values for endpoints.
            pygame.draw.aalines(surface,color,False,points,blend)
        else:
            points = [list(map(rndint,p)) for p in points]
            pygame.draw.lines(surface,color,False,points,width)


def bezier(surface, color, controlpointslist, steps, width=1):
    _draw_bezier(surface, color, controlpointslist, steps, False, width, False)
def aabezier(surface, color, controlpointslist, steps, blend=True):
    _draw_bezier(surface, color, controlpointslist, steps, True, 1, blend)

def spline(surface, color, closed, pointslist, steps, t=0.0,b=0.0,c=0.0, width=1):
    _draw_spline(surface, color, closed, pointslist, steps, t,b,c, False, width, False)
def aaspline(surface, color, closed, pointslist, steps, t=0.0,b=0.0,c=0.0, blend=True):
    _draw_spline(surface, color, closed, pointslist, steps, t,b,c, True, 1, blend)
