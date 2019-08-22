from kuyn.color import Color
from kuyn.convert import RGB_to_HSL
from kuyn.util import *
from kuyn.transform import *

color_1 = Color(r=64, g=24, b=222, a=1.0)



#distance = get_distance(color_1, color_2)
HSL_list = convert.RGB_to_HSL(color_1)
#print("HSL_list", HSL_list)
HSL_list_comp = convert.H_rotate(HSL_list, 3)
#print("HSL_list_comp", HSL_list_comp)
RGB_list = HSL_to_RGB(HSL_list_comp[0], HSL_list_comp[1], HSL_list_comp[2])
print("RGB_list", RGB_list)

new_rgb = hex_to_RGB('#d55eb6')