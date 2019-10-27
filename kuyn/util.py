from kuyn.color import Color
import math

def get_distance(color_1: Color, color_2: Color):
    try:
        distance = math.sqrt(
        (color_2.r - color_1.r) ^ 2 +
        (color_2.g - color_1.g) ^ 2 +
        (color_2.b - color_1.b) ^ 2)
    except ValueError:
        distance = math.sqrt(
        (color_1.r - color_2.r) ^ 2 +
        (color_1.g - color_2.g) ^ 2 +
        (color_1.b - color_2.b) ^ 2)
    return distance

def invert(color: Color):
    R = color.r * -1 + 255
    G = color.g * -1 + 255
    B = color.b * -1 + 255
    return Color(R,G,B)