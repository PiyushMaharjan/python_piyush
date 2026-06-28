def main():
    x,y=input("enter two numbers:" ).split()
    sum(x,y)
    diff(x,y)
    multiply(x,y)
    divison(x,y)

def sum(x,y):
    sum=int(x)+int(y)
    print(f"the sum is : {sum}")

def diff(x,y):
    diff=int(x)-int(y)
    print(f"the diff is : {diff}")

def multiply(x,y):
    mul=int(x)*int(y)
    print(f"the multiplication is : {mul}")

def divison(x,y):
    div=int(x)/int(y)
    print(f"the division is : {div:.2f}")

main()