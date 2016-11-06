import turtle
import math
from polygon import *

def draw_flower(t,pedal,length):
    t.lt(90)
    start_angle = 180/pedal
    outter_angle = 360 / pedal
    interval  = 180 - outter_angle
    radius = math.cos((180-360/pedal)/2*math.pi/180)*length*2
    t.pu()
    t.rt(start_angle)
    t.fd(length)
    t.lt(outter_angle)
    t.pd()
    for i in range(int(pedal)):
        arc(t,radius,interval)
        t.lt(interval)


if __name__ == "__main__":
    bob = turtle.Turtle()
    draw_flower(bob,7,50)
    input("Enter to continue")
