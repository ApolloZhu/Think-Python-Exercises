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

def teleport(t,size,x,y):
    pos = t.pos()
    goto(t,pos[0]+distance(size,x),pos[1]+distance(size,y))

def goto(t,x,y):
    incognito(t,t.goto,(x,y))

def resetting(t,func,*args,**kwargs):
    pos = t.pos()
    heading = t.heading()
    func(*args,**kwargs)
    goto(t,*pos)
    # incognito(t,t.goto,pos)
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

def draw_rect(t,size,first=0.5,second=1):
    for i in range(2):
        draw_turning(t,size,first,second)
        rt(t)

# Interface

def draw_a(t,size):
    lt(t)
    draw_rect(t,size,first=0.25)
    teleport(t,size,0,0.5)
    seth(t)
    draw_turning(t,size,1,0.5)

def draw_b(t,size):
    lt(t)
    draw_rect(t,size)
    resetting(t,fd,t,size,1)
    skip(t,size)

def draw_c(t,size):
    lt(t)
    resetting(t,draw_turning,t,size,0.5,1)
    seth(t)
    fd(t,size,1)

def draw_d(t,size):
    lt(t)
    draw_rect(t,size)
    seth(t)
    fd(t,size,1)
    resetting(t,vertical,t,fd,t,size,1)

def draw_e(t,size):
    lt(t)
    fd(t,size,0.25)
    draw_rect(t,size,first=0.25)
    teleport(t,size,0,-0.25)
    seth(t)
    fd(t,size,1)

def skip(t,distance):
    seth(t)
    incognito(t,fd,t,distance,1)
