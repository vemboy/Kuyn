import math
from kuyn.color import Color, HSL, RGB
from math import floor



def get_distance(color_1: Color, color_2: Color):
    distance = math.sqrt(
    pow((color_2.r - color_1.r), 2) +
    pow((color_2.g - color_1.g), 2) +
    pow((color_2.b - color_1.b), 2))

    return distance

def invert(color: Color):
    R = color.r * -1 + 255
    G = color.g * -1 + 255
    B = color.b * -1 + 255
    return Color(R,G,B)

