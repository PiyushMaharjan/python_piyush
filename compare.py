#asking user for inout
x = int(input("whats x?"))
y = int(input("whats y?"))

#adding conditions
if x<y:
    print("x is less than y")
    
#makes mutual exclusion through elif
elif x>y:
    print("x is greater than y")

else: 
    print("X is equal to y")
    