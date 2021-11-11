#!/Users/danny.molnar/.pyenv/shims/python

class Car:
    
    #constructor
    def __init__(self, color):
        self.color = color
        
    #method
    def print_color(self):
        print(self.color)
    

#instantialise the class
my_first_car = Car("red")
my_first_car.print_color()

