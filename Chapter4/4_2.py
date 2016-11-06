import turtle
import math
import sys
from polygon import *

def draw_flower(t,petal_count,length):
    t.lt(90)
    start_angle = 180 / petal_count
    outter_angle = 360 / petal_count
    t.rt(start_angle)
    for i in range(int(petal_count)):
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
        count = int(input("Petal Count: "))
    if not length:
        length = int(input("Petal Length: "))
    draw_flower(bob,count,length)
    input("Enter to continue")
