import math
import sys

def error_checking(Color):
    
    if(Color.r > 255):
        raise Exception("Red cannot be higher than 255")
         
    elif(Color.g > 255):
        raise Exception("Green cannot be higher than 255")
         
    elif(Color.b > 255):
        raise Exception("Blue cannot be higher than 255")
         
    elif(Color.a > 1.0):
        raise Exception("Alpha cannot be higher than 1.0")
    else:
        return(Color.r, Color.g, Color.b, Color.a)
        

class Color:
    def __init__(self, r: int, g: int, b: int, a: float = 1.0) -> None:
        self.a = a
        self.r = r
        self.g = g
        self.b = b

    @property
    def magnitude(self):
        return math.sqrt((self.r - 0)^2 + (self.g - 0)^2 + (self.b - 0)^2)


        

    def __add__(self, other):
        
        if isinstance(other, int):
            
            error_checking(Color(r=self.r + other, g=self.g + other, b=self.b + other, a=self.a + other))
                

        elif isinstance(other, Color):
            
            error_checking(Color(r=self.r + other.r, g=self.g + other.g, b=self.b + other.b, a=self.a + other.a))

        else:
            raise Exception("Added type is not supported.")

    def __sub__(self, other):
        
        if isinstance(other, int):
            
            error_checking(Color(r=self.r - other, g=self.g - other, b=self.b - other, a=self.a - other))

        elif isinstance(other, Color):
            
            error_checking(Color(r=self.r - other.r, g=self.g - other.g, b=self.b - other.b, a=self.a - other.a))

        else:
            raise Exception("Subtracted type is not supported.")

    def __eq__(self, other: object) -> bool:

        if isinstance(other, Color):
            if(self.a == other.a and self.r == other.r and self.g == other.g and self.b == other.b):
                return True
        return False

    def __mul__(self, scalar: float):
    
        error_checking(Color(r=self.a * scalar, g=self.r * scalar, b=self.g * scalar, a=self.b * scalar))

