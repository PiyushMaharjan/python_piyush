def main():
    x=int(input("whats x?"))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n%2==0:
        return True
    else:
        return False
    
#also can be written as:
    return True if n % 2 == 0 else False

#also as:
    return n % 2 == 0

main()

                