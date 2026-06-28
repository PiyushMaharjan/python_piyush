i = 0
while i<3:
    print("meow")
    i += 1

for j in [0,1,2]:
    print("woof")


#for positive qn
while True:
    n=int(input("whats n?"))
    if n>0:
        break

for _ in range(n):
    print("meow")


#function for meow

def main():
    number=get_number()
    meow(number)

def get_number():
    while True:
        n=int(input("whats n?"))
        if n>0:
            return n
def meow(n):
    for _ in range(n):
        print("meow")

main()            