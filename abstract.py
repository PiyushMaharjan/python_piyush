#abstract class: a class that cannot be instantiated on it own: mean to be subclassed
                #they can cpntain abstract method that has no implementation
                #beneft: prevents instantiation of calss itself
                #        required children to use nherited abstract method




from  abc import ABC, abstractmethod

class Vechile(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vechile):

    def go(self):
        print("drive the car")
    
    def stop(self):
        print("stop the car")

class Bike(Vechile):

    def go(self):
        print("ride the bike")
    
    def stop(self):
        print("stop the bike")

class Boat(Vechile):
    
    def go(self):
        print("sail the boat")
    
    def stop(self):
        print("stop the boat")

car=Car()

car.go()
car.stop()