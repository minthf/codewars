class Person:
    def __init__(self, my_name):
        self.name = my_name
        
    def greet(self, your_name):
        return f"Hello {your_name}, my name is {self.name}"