#nested loop
for _ in range(3):
    print("#")

#using func

def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")


main()

#for horizaontal

def main():
    print_row(4)

def print_row(width):
    print("?"*width)

main()

#2d or square

def main():
    print_square(6)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#",end="")
        print()
main()


#tightening nested square look

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#"*width)

main()