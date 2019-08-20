import math
import sys

class Color:
    def __init__(self, r: int, g: int, b: int, a: float = 1.0) -> None:
        self.__a = a
        self.__r = r
        self.__g = g
        self.__b = b

    @property
    def magnitude(self):
        return math.sqrt((self.__r - 0)^2 + (self.__g - 0)^2 + (self.__b - 0)^2)
    @property
    def r(self):
        return self.__r
    @property
    def g(self):
        return self.__g
    @property
    def b(self):
        return self.__b
    @property
    def a(self):
        return self.__a

    @r.setter
    def set_r(self, new_r):
        if new_r > 255:
            raise Exception("r value cannot be greater than 255")
        self.__r = new_r
    @g.setter
    def set_g(self, new_g):
        if new_g > 255:
            raise Exception("r value cannot be greater than 255")
        self.__g = new_g
    @b.setter
    def set_b(self, new_b):
        if new_b > 255:
            raise Exception("r value cannot be greater than 255")
        self.__b = new_b
    @a.setter
    def set_a(self, new_a):
        if new_a> 255:
            raise Exception("r value cannot be greater than 255")
        self.__a = new_a    

    def __add__(self, other):
        
        if isinstance(other, int):
            self.set_r(new_r=self.__r + other)
            self.set_g(new_g=self.__g + other)
            self.set_b(new_b=self.__b + other)
            self.set_a(new_a=self.__a + other)
            return Color(self.__r, self.__g, self.__b, self.__a)

        elif isinstance(other, Color):
            
            self.set_r(new_r=self.__r + other)
            self.set_g(new_g=self.__g + other)
            self.set_b(new_b=self.__b + other)
            self.set_a(new_a=self.__a + other)
            return Color(self.__r, self.__g, self.__b, self.__a)

        else:
            raise Exception("Added type is not supported.")

    def __sub__(self, other):
        
        if isinstance(other, int):
            
            self.set_r(new_r=self.__r - other)
            self.set_g(new_g=self.__g - other)
            self.set_b(new_b=self.__b - other)
            self.set_a(new_a=self.__a - other)
            return Color(self.__r, self.__g, self.__b, self.__a)

        elif isinstance(other, Color):
            
            self.set_r(new_r=self.__r - other)
            self.set_g(new_g=self.__g - other)
            self.set_b(new_b=self.__b - other)
            self.set_a(new_a=self.__a - other)
            return Color(self.__r, self.__g, self.__b, self.__a)

        else:
            raise Exception("Subtracted type is not supported.")

    def __eq__(self, other: object) -> bool:

        if isinstance(other, Color):
            if(self.__a == other.__a and self.__r == other.__r and self.__g == other.__g and self.__b == other.__b):
                return True
        return False

    def __mul__(self, scalar: float):
    
        Color(r=self.__a * scalar, g=self.__r * scalar, b=self.__g * scalar, a=self.__b * scalar)