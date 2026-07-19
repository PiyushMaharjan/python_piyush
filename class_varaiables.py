class Students:
    class_year = 2026
    num_student = 0

     
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Students.num_student+=1
    
student1=Students('piyush' ,24)
student2=Students('safal', 18)
student3=Students('sagar', 28)
student4=Students('safalta', 18)
student5=Students('sneha', 18)
student6=Students('prajen', 18)



print(f'Hi!! My name is {student1.name}')
print(f'I am {student1.age} years old')
print(f'I am gradutaing in {Students.class_year} and we have {Students.num_student} students in our class')