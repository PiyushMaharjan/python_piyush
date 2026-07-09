"""
name = input("whats your name?")


file=open("names.txt", "w")
file.write(name)
file.close()


#appending

name = input("whats your name?")


file=open("names.txt", "a")
file.write(name)
file.close()   #doesnt keep space(write directly gives the namme)



#gives whitspace
name = input("whats your name?")


file=open("names.txt", "a")
file.write(f"{name}\n")
file.close()  



#using with
name = input("whats your name?")


with open("names.txt", "a")as file:
    file.write(f"{name}\n")


#read

with open ("names.txt", "r") as file:

    for line in file:
        print("hello,", line.rstrip())
        
#list created
names = []
#now iterated the file reading in each line stripping new line and adding just the name from line 49 to 50
with open("names.txt")as file:
    for line in file:
        names.append(line.rstrip())
#sorting names n print in order
for name in sorted(names):
    print(f"hello, {name}")
"""
#sorting file itself
with open("names.txt")as file:
    for line in sorted(file):
        print("hello,", line.strip())