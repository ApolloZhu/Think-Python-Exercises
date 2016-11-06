import turtle
import math
import sys
from polygon import *

# Referenced from http://greenteapress.com/thinkpython2/code/flower.py

def draw_petal(t,length):
    for i in range(2):
        arc(t,length,60)
        t.lt(120)

def draw_flower(t,petal_count,length):
    for i in range(petal_count):
        draw_petal(t,length)
        t.lt(360/petal_count)

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
