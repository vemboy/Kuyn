from math import floor
from kuyn.color import HSL, RGB


def floor_rgb(rgb: RGB):
    return RGB(R=floor(rgb.R), G=floor(rgb.G), B=floor(rgb.B))

def round_hsl(hsl: HSL):
    return HSL(H=round(hsl.H), S=round(hsl.S), L=round(hsl.L))
