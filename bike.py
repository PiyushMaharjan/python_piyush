class Bike:
    #attributes in instances
    def __init__(self, model, color, for_sale):

        self.model=model
        self.color=color
        self.for_sale=for_sale
    #methods 
    def ride(self):
        print(f'ride the {self.color}{self.model}')

    def stop(self):
        print(f'stop the {self.color}{self.model}')

    def describe(self):
        print(f'this is a {self.color} {self.model} which is ready for {self.for_sale}')