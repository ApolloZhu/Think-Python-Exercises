import turtle
import math
import sys
from polygon import *

def draw_flower(t,pedal,length):
    t.lt(90)
    start_angle = 180/pedal
    outter_angle = 360 / pedal
    t.rt(start_angle)
    for i in range(int(pedal)):
        t.rt(30)
        arc(t,length,60)
        t.lt(120)
        arc(t,length,60)
        t.lt(150)
        t.lt(outter_angle)

if __name__ == "__main__":
    bob = turtle.Turtle()
    count = 0
    length = 0
    if len(sys.argv)>1:
        count = int(sys.argv[1])
        if len(sys.argv) > 2:
            length = int(sys.argv[2])
    if not count:
        count = int(input("Pedal Count: "))
    if not length:
        length = int(input("Pedal Length: "))
    draw_flower(bob,count,length)
    input("Enter to continue")
