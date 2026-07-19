class Employee:
    def __init__(self, first, last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@gmail.com'


emp_1=Employee('piyush', 'maharjan', 50000)
emp_2=Employee('safal', 'keshi', 60000)

print(emp_1)
print(emp_2)


print(emp_1.email)
print(emp_2.email)