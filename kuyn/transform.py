from typing import List
from kuyn.color import Color
from kuyn.convert import *
import math


def H_rotate(hsl: HSL, num: int) -> List[HSL]:
    comp_HSL_list = []
    H = hsl.H
    add_angle = 360.0/(num + 1)

    for i in range(num + 1):
        new_H = int((H + i*add_angle)%360)
        comp_HSL_list.append(HSL(H=new_H, S=hsl.S, L=hsl.L))

    return comp_HSL_list


def get_complement(color: Color, num=1) -> List[Color]:
    HSL_list = RGB_to_HSL(color.RGB)
    HSL_list_comp = H_rotate(HSL_list, num)
    RGB_list_comp = [HSL_to_RGB(hsl) for hsl in HSL_list_comp] 
    return [Color(r=rgb.R, g=rgb.G, b=rgb.B) for rgb in RGB_list_comp]