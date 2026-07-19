class Employee:
    raise_amount = 1.04

    def __init__(self, first, last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1=Employee('piyush', 'maharjan', 50000)
emp_2=Employee('safal', 'keshi', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#emp_1.raise_amount
#Employee.raise_amount