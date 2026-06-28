x = int(input("whats x?"))
print(f"x is {x}")

#try adn catch/value error

try:
    x = int(input("whats x?"))
    print(f"x is{x}")
except ValueError:
    print("x is not an integer")

#nameerror
try:
    x = int(input("whats x?"))
except ValueError:
    print("x is not an integer")
else:#to remove nameerror
    print(f"x is {x}")


#repromting the user by loop
while True:
    try:
        x = int(input("whats x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")

#get_int

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("whats x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x
        

main()



#pass
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("whats x?"))
        except ValueError:
            pass
        
        
main()



