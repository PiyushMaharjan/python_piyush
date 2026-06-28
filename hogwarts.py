students = ["safal","piyush","ron"]

print(students[0])
print(students[1])
print(students[2])

#using loop

students = ["safal","piyush","ron"]

for student in students:
    print(student)

#using len as range doesnt take strings

students = ["safal","piyush","ron"]

for i in range(len(students)):
    print(i+1, (students[i]))#+1 helps to starts the resukt from 1 rather than 0 and gives a ranking


#using dict=dictonary

students = {
    "safal": "godawarai",
    "piyush": "panga",
    "ron": "pokhara",
}

for student in students:
    print(student, students[student], sep=",")

#for multiple strings in dict

students = [
    {"name":"piyush","house":"panga","hobby":"Sleeping"},
    {"name":"safal","house":"godawari","hobby":"eating"},
    {"name":"ron","house":"pokhara","hobby":None},
]

for student in students:
    print(student["name"],student["house"],student["hobby"], sep=",")