import math
import sys
import itertools
from kuyn.util import *
from typing import NamedTuple, List


class Color:
    def __init__(self, r: int, g: int, b: int, a: float = 100.0) -> None:
        self.a = a
        self.r = r
        self.g = g
        self.b = b
        self.RGB = RGB(self.r, self.g, self.b)

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
        self.__r  = clamp(new_r, 0, 255)

    @g.setter
    def g(self, new_g):
        self.__g  = clamp(new_g, 0, 255)

    @b.setter
    def b(self, new_b):
        self.__b  = clamp(new_b, 0, 255)

    @a.setter
    def a(self, new_a):
        self.__a  = clamp(new_a, 0, 1.0)

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
                a=self.a + other,
            )

        elif isinstance(other, Color):
            return Color(
                r=self.r + other.r,
                g=self.g + other.g,
                b=self.b + other.b,
                a=self.a + other.a,
            )

        else:
            raise Exception("Added type is not supported")

    def __sub__(self, other):      
        if isinstance(other, int):
            return Color(
                r=self.r - other,
                g=self.g - other,
                b=self.b - other,
                a=self.a - other,
            )

        elif isinstance(other, Color):
            return Color(
                r=self.r - other.r,
                g=self.g - other.g,
                b=self.b - other.b,
                a=self.a - other.a,
            )

        else:
            raise Exception("Subtracted type is not supported")

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
    def __repr__(self):
            return 'Color(r={}, g={}, b={}, a={})'.format(self.r, self.g, self.b, self.a)


class HSL(NamedTuple):
    H: float  # 0.-360.
    S: float  # 0.-100.
    L: float  # 0.-100.


class RGB(NamedTuple):
    R: float  # 0.-255.
    G: float  # 0.-255.
    B: float  # 0.-255.


class ColorHex(NamedTuple):
    value: str  # '#XXXXXX'