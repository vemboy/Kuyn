from kuyn.color import Color, RGB, HSL
from kuyn.convert import *
from kuyn.transform import *
from kuyn.pallete import *
from PIL import Image

pallete_1 = Pallete([Color(4,5,6), Color(11,11,11), Color(4,5,7)])
pallete_1.add([Color(22,22,22), Color(25,24,22)])
print(pallete_1.colors)
pallete_1.avg_distance()


"""HSL_list = RGB_to_HSL(color_1.RGB)
print(HSL_list)
HSL_list_comp = H_rotate(HSL_list, num=2)
print(HSL_list_comp)
RGB_list_comp = [HSL_to_RGB(hsl) for hsl in HSL_list_comp] 
print(RGB_list_comp)"""
