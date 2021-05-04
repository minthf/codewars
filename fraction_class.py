import math

class Fraction:

    def __init__(self, numerator, denominator):
        self.top = int(numerator)
        self.bottom = int(denominator)
    
    #Equality test
    
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    def __add__(self, other):
        top = self.top * other.bottom + other.top * self.bottom
        bottom = self.bottom * other.bottom
        greatest_common_division = math.gcd(top, bottom)
        top /= greatest_common_division
        bottom /= greatest_common_division
        return Fraction(top, bottom)
    
    def __str__(self):
        return f"{self.top}/{self.bottom}"