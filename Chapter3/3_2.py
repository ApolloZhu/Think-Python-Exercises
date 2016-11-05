def do_twice(f,val):
    f(val)
    f(val)

def print_twice(msg):
    do_twice(print,msg)

def do_four(f,val):
    do_twice(f,val)
    do_twice(f,val)

do_twice(print_twice,'spam')
print()

do_four(print,'spam')
