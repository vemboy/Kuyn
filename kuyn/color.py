import math
import sys
from typing import NamedTuple
class Color:
    def __init__(self, r: int, g: int, b: int, a: float = 1.0)-> None:
        self.a = a
        self.r = r
        self.g = g
        self.b = b

    @property
    def magnitude(self):
        return math.sqrt(
            (self.__r - 0) ^ 2 +
            (self.__g - 0) ^ 2 +
            (self.__b - 0) ^ 2
        )

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
    def r(self, new_r):
        if new_r > 255 or new_r < 0:
            raise Exception("r must be in range [0,255]")
        self.__r = new_r

    @g.setter
    def g(self, new_g):
        if new_g > 255 or new_g < 0:
            raise Exception("g must be in range [0,255]")
        self.__g = new_g

    @b.setter
    def b(self, new_b):
        if new_b > 255 or new_b < 0:
            raise Exception("b must be in range [0,255]")
        self.__b = new_b

    @a.setter
    def a(self, new_a):
        if new_a > 1.0 or new_a < 0.0:
            raise Exception("a must be in range [0,100]")
        self.__a = new_a

    def set_rgba(self, r: int, g: int, b: int, a: int):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __add__(self, other):
        if isinstance(other, int):
            return Color(
                r=self.r + other,
                g=self.g + other,
                b=self.b + other,

            )

        elif isinstance(other, Color):
            return Color(
                r=self.r + other.r,
                g=self.g + other.g,
                b=self.b + other.b,
            )

        else:
            raise Exception("Added type is not supported.")

    def __sub__(self, other):      
        if isinstance(other, int):
            return Color(
                r=self.r - other,
                g=self.g - other,
                b=self.b - other,
            )

        elif isinstance(other, Color):
            return Color(
                r=self.r - other.r,
                g=self.g - other.g,
                b=self.b - other.b,

            )

        else:
            raise Exception("Subtracted type is not supported.")

    def __eq__(self, other: object) -> bool:

        if isinstance(other, Color):
            if(
                self.a == other.a and
                self.r == other.r and
                self.g == other.g and
                self.b == other.b
            ):
                return True
        return False

    def __mul__(self, scalar: int):
        return Color(
            r=self.r * scalar,
            g=self.g * scalar,
            b=self.b * scalar,
            a=self.a * scalar,
        )

class HSL(NamedTuple):
    H: int
    S: int
    L: int

class RGB(NamedTuple):
    R: int
    G: int
    B: int

class ColorHex(NamedTuple):
    value: str

        










