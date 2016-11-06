import turtle, math, sys

def draw_isosceles_triangle(t,side_length,vertex_angle):
    base_angle = (180 - vertex_angle) / 2
    base_length = math.sin(vertex_angle/2*math.pi/180)*side_length*2
    t.fd(side_length)
    t.lt(180-base_angle)
    t.fd(base_length)
    t.lt(180-base_angle)
    t.fd(side_length)

def draw_pie(t,slices,r):
    for i in range(slices):
        draw_isosceles_triangle(t,r,360/slices)
        t.lt(180)

if __name__ == "__main__":
    bob = turtle.Turtle()
    count = 0
    length = 0
    if len(sys.argv)>1:
        count = int(sys.argv[1])
        if len(sys.argv) > 2:
            length = int(sys.argv[2])
    if not count:
        count = int(input("Side Count: "))
    if not length:
        length = int(input("Petal Length: "))
    draw_pie(bob,count,length)
    input("Enter to continue . . .")
