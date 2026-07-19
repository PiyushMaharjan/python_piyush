class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f'{self.name} is sleeping')

    def dance(self):
        print(f'{self.name} is dancing')

class Dog(Animal):
    pass
class Cat(Animal):
    pass
class Rat(Animal):
    pass

dog=Dog('safal')
cat=Cat('safal')
rat=Rat('safal')

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.dance()