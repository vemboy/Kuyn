from kuyn.color import Color
from kuyn.convert import *
from kuyn.util import *
from kuyn.transform import *

color_1 = Color(r=64, g=24, b=222, a=1.0)



#distance = get_distance(color_1, color_2)

#print("HSL_list", HSL_list)

#print("HSL_list_comp", HSL_list_comp)


new_rgb = hex_to_RGB('#d55eb6')

def get_complement(color: Color, num=1):
    actual_RGB_list = []
    HSL_list = RGB_to_HSL(color)
    HSL_list_comp = H_rotate(HSL_list, num)
    for x in range(0,num+1):
        RGB_list = HSL_to_RGB(HSL_list_comp[x][0], HSL_list_comp[x][1], HSL_list_comp[x][2])
        actual_RGB_list.append(RGB_list)
    print(actual_RGB_list)
    print("Your original color is the last one")
    return 0

get_complement(color_1,2)
