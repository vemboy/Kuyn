from kuyn.color import Color
from kuyn.convert import *
from kuyn.util import *
from kuyn.transform import *

color_1 = Color(r=50, g=168, b=82)



#distance = get_distance(color_1, color_2)

#print("HSL_list", HSL_list)

#print("HSL_list_comp", HSL_list_comp)

comp_l = get_complement(color_1)
print(comp_l)
#RGB = HSL_to_Color(HSL_color)
#print(RGB)
