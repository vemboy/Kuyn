import math
import sys


class Color:
    def __init__(self, r: int, g: int, b: int, a: float = 100.0) -> None:
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
        if new_r > 255:
            new_r = 255
        elif new_r < 0:
            new_r = 0
        else:
            new_r = new_r
        self.__r = new_r

    @g.setter
    def g(self, new_g):
        if new_g > 255:
            new_g = 255
        elif new_g < 0:
            new_g = 0
        else:
            new_g = new_g
        self.__g = new_g

    @b.setter
    def b(self, new_b):
        if new_b > 255:
            new_b = 255
        elif new_b < 0:
            new_b = 0
        else:
            new_b = new_b
        self.__b = new_b

    @a.setter
    def a(self, new_a):
<<<<<<< Updated upstream
        if new_a > 100 or new_a < 0:
            raise Exception("a must be in range [0,100]")
=======
        if new_a > 1.0:
            new_a = 1.0
        elif new_a < 0:
            new_a = 0
        else:
            new_a = new_a
>>>>>>> Stashed changes
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
            print("Added type is not supported.")
            return 0

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
            print("Subtracted type is not supported.")
            return 0
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
