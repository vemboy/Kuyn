from typing import List
from kuyn.color import Color
from kuyn.convert import *
import math


def H_rotate(HSL_list: HSL, num: int) -> List[Color]:
    num = num + 1
    add_sub_num = 1/num
    count = 0
    comp_color_list = []

    if(num > 1):
        while(num > count):
            if(HSL_list.H + add_sub_num > 1):
                h2 = HSL_list.H + add_sub_num - 1
                count += 1
                HSL_list = HSL(H=h2, S=HSL_list.S, L=HSL_list.L)
                comp_color_list.append(HSL_list)
            else:
                h2 = HSL_list.H + add_sub_num
                count += 1
                HSL_list = HSL(H=h2, S=HSL_list.S, L=HSL_list.L)
                comp_color_list.append(HSL_list)
    else:
        if(HSL_list.H > 0.5):
            h2 = HSL_list.H - add_sub_num
        else:
            h2 = HSL_list.H + add_sub_num
        HSL_list = HSL(H=h2, S=HSL_list.S, L=HSL_list.L)
        comp_color_list.append(HSL_list)

    return comp_color_list


def complement_2(color: Color):
    R = round(math.sqrt(255**2 - color.r**2))
    G = round(math.sqrt(255**2 - color.g**2))
    B = round(math.sqrt(255**2 - color.b**2))
    return Color(R, G, B)


def complement_3(color: Color):
    R = color.b
    G = color.g
    B = color.r
    return Color(R=R, G=G, B=B)


def complement_4(color: Color):
    comp_color = Color(255 - color.r, 255 - color.g, 255 - color.b, a=1.0)
    return comp_color


def get_complement(color: Color, num=1):
    actual_color_list = []
    HSL_list = Color_to_HSL(color)
    HSL_list_comp = H_rotate(HSL_list, num)
    for x in range(0, num+1):
        color_list = HSL_to_Color(HSL_list_comp[x])
        actual_color_list.append(color_list)
    return 0
