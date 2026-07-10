"""with open("students.csv")as file:
    for line in file:
        name, house=line.rstrip().split(",")
        print(f"{name} is in {house}")



#making a dictonary
students=[]#global variable

with open("students.csv")as file:
    for line in file:
        name,house=line.rstrip().split(",")
        student = {}
        student["name"]=name
        student["house"]=house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
  


students=[]#global variable

with open("students.csv")as file:
    for line in file:
        name,house=line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)
#retruns students name from dictionry
def get_house(student):
    return student["house"]


for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")


students=[]#global variable

with open("students.csv")as file:
    for line in file:
        name, home=line.rstrip().split(",")
        student = {"name":name, "house":home}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")  """


import csv

students=[]#global variable

with open("students.csv")as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name":name, "home":home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}") 