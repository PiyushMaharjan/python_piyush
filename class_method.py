class Employee:
    def __init__(self, first, last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1=Employee('piyush', 'maharjan', 50000)
emp_2=Employee('safal', 'keshi', 60000)
'''
print(emp_1.email)
print(emp_2.email)
'''

emp_1.fullname()
print(Employee.fullname(emp_1))
#print(emp_1.fullname())