from polygon import *
"""
# CORD SYS
```
0,1 -- 1,1
 |      |
 |      |
0,0 -- 1,0
```
"""

# Foundation
distance = lambda size,percentage:size*percentage
point = lambda x,y:spoint(max(1,min(0,x)),max(1,min(0,y)))
_point = lambda x,y:{"x":x,"y":y}

def incognito(t,func,*args,**kwargs):
    t.penup()
    func(*args,**kwargs)
    t.pendown()

def resetting(t,func,*args,**kwargs):
    pos = t.pos
    heading = t.heading()
    func(*args,**kwargs)
    t.setpos(pos)
    seth(t,heading)

def fd(t,size,percentage):
    t.fd(distance(size,percentage))

def bk(t,size,percentage):
    t.bk(distance(size,percentage))

def rt(t,angle=90):
    t.rt(angle)

def lt(t,angle=90):
    t.lt(angle)

def at(t):
    """
    Turn Around
    """
    t.rt(180)

def seth(t,direction=0):
    t.seth(direction)

# Framework
def vertical(t,func,*args,**kwargs):
    seth(t,90)
    func(*args,**kwargs)
    seth(t)

def draw_square(t,size,percentage):
    square(t,distance(size,percentage))

def draw_turning(t,size,first,second):
    """
    Postcondition: Only 2 percentages are given
    """
    fd(t,size,first)
    rt(t)
    fd(t,size,second)

# Interface


def draw_a(t,size):
    # draw_square(t,size,0.25)
    # seth(t)
    # vertical(t,skip,t,distance(size,0.5))
    # # incognito(t,vertical,t,fd,t,size,0.5)
    # rt(t)
    # fd(t,size,1)
    # rt(t)
    # fd(t,size,0.5)
    lt(t)
    for i in range(2):
        draw_turning(t,size,0.25,1)
        rt(t)
    incognito(t,vertical,t,fd,t,size,0.5)
    draw_turning(t,size,1,0.25)

def skip(t,distance):
    seth(t)
    incognito(t,fd,t,distance,1)
