from kuyn.color import Color
import math
from math import floor
from kuyn.color import HSL, RGB

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


def get_max(l, n):
    return sorted(l)[-n:]

def floor_rgb(rgb: RGB):
    return RGB(R=floor(rgb.R), G=floor(rgb.G), B=floor(rgb.B))

def round_hsl(hsl: HSL):
    return HSL(H=round(hsl.H), S=round(hsl.S), L=round(hsl.L))