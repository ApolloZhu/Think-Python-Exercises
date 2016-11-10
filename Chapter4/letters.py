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

def teleport(t,size,x,y,traceless=True):
    pos = t.pos()
    goto(t,pos[0]+distance(size,x),pos[1]+distance(size,y),traceless)

def goto(t,x,y,traceless=True):
    if traceless:
        incognito(t,t.goto,(x,y))
    else:
        t.goto((x,y))

def resetting(t,func,*args,**kwargs):
    pos = t.pos()
    heading = t.heading()
    func(*args,**kwargs)
    goto(t,*pos)
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

def draw_vertical_line(t,size,percentage=1):
    resetting(t,vertical,t,fd,t,size,percentage)

def draw_dot(t):
    t.dot()

def draw_tail(t,size,percentage=0.7,endingLeft=True):
    heading = t.heading()
    if endingLeft:
        seth(t,270)
        resetting(t,draw_turning,t,size,0.2,percentage)
    else:
        teleport(t,size,percentage,-0.2)
        seth(t,180)
        draw_turning(t,size,percentage,0.2)
    seth(t,heading)

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
    # resetting(t,fd,t,size,1)
    draw_vertical_line(t,size)
    skip(t,size)

def draw_c(t,size):
    lt(t)
    resetting(t,draw_turning,t,size,0.5,1)
    prepare(t,size)

def draw_d(t,size):
    lt(t)
    draw_rect(t,size)
    prepare(t,size)
    # resetting(t,vertical,t,fd,t,size,1)
    draw_vertical_line(t,size)

def draw_e(t,size):
    lt(t)
    fd(t,size,0.25)
    draw_rect(t,size,first=0.25)
    teleport(t,size,0,-0.25)
    prepare(t,size)

def draw_f(t,size):
    skip(t,size/2)
    lt(t)
    resetting(t,draw_turning,t,size,0.7,0.5)
    draw_turning(t,size,0.5,0.5)
    at(t)
    fd(t,size,1)
    teleport(t,size,1,-0.5)

def draw_g(t,size):
    lt(t)
    draw_rect(t,size)
    prepare(t,size)
    draw_tail(t,size)

def draw_h(t,size):
    draw_vertical_line(t,size)
    lt(t)
    draw_turning(t,size,0.5,1)
    vertical(t,fd,t,size,-0.5)

def draw_i(t,size):
    skip(t,size,0.5)
    draw_vertical_line(t,size,0.5)
    teleport(t,size,0,0.7)
    draw_dot(t)
    teleport(t,size,0.5,-0.7)

def draw_j(t,size):
    draw_i(t,size)
    skip(t,size,-0.5)
    draw_tail(t,size,percentage=0.35)
    skip(t,size,0.5)

def draw_k(t,size):
    skip(t,size,0.35)
    draw_vertical_line(t,size)
    skip(t,size,0.35)
    side = 0.35*math.sqrt(2)
    lt(t,135)
    resetting(t,draw_turning,t,size,side,side)
    skip(t,size,0.3)

def draw_l(t,size):
    skip(t,size,0.4)
    draw_vertical_line(t,size)
    draw_tail(t,size,percentage=0.35,endingLeft=False)
    skip(t,size,0.6)

def draw_m(t,size):
    for i in range(2):
        lt(t)
        draw_turning(t,size,0.5,0.5)
        vertical(t,fd,t,size,-0.5)

# encap later
def draw_n(t,size):
    skip(t,size,0.25)
    lt(t)
    draw_turning(t,size,0.5,0.5)
    vertical(t,fd,t,size,-0.5)
    skip(t,size,0.25)

def draw_o(t,size):
    lt(t)
    draw_rect(t,size)
    prepare(t,size)

def draw_p(t,size):
    lt(t)
    draw_rect(t,size)
    resetting(t,vertical,t,fd,t,size,-0.2)
    prepare(t,size)

def draw_q(t,size):
    lt(t)
    draw_rect(t,size)
    prepare(t,size)
    resetting(t,vertical,t,fd,t,size,-0.2)

def draw_r(t,size):
    skip(t,size,0.35)
    draw_vertical_line(t,size,0.5)
    lt(t)
    resetting(t,draw_turning,t,size,0.35,0.35)
    skip(t,size,0.65)

def draw_s(t,size):
    for i in (1,0.25):
        fd(t,size,i)
        lt(t)
    for i in (1,0.25):
        fd(t,size,i)
        rt(t)
    fd(t,size,1)
    teleport(t,size,0,-0.5)


def prepare(t,size,percentage=1):
    seth(t)
    fd(t,size,percentage)

def skip(t,size,percentage=1):
    incognito(t,prepare,t,size,percentage)
