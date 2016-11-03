def print_grid(row,col):
    separator = ("+"+" -"*4+" ")*col+"+\n"
    single = ("|"+" "*9)*col+"|\n"
    whole = single * 4 
    print((separator+whole)*row+separator)

def print_2x2_grid():
    print_grid(2,2)

def print_4x4_grid():
    print_grid(4,4)

if __name__ == "__main__":
    print_2x2_grid()
    print_4x4_grid()
    print_grid(int(input("row: ")),int(input("col: ")))
