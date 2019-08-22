from kuyn.color import Color
import math
# Complements


def H_rotate(HSL_list, num: int):

    num = num + 1
    add_sub_num = 1/num
    count = 0
    comp_color_list = []
    print(add_sub_num)
    print(HSL_list[0])

    if(num > 1):
        while(num > count):

            if(HSL_list[0] + add_sub_num > 1):
                h2 = HSL_list[0] + add_sub_num - 1
                count += 1
                HSL_list = [h2, HSL_list[1], HSL_list[2]]
                comp_color_list.append(HSL_list)
            else:
                h2 = HSL_list[0] + add_sub_num
                count += 1
                HSL_list = [h2, HSL_list[1], HSL_list[2]]
                comp_color_list.append(HSL_list)

               
    else:
        if(HSL_list[0] > 0.5):
            h2 = HSL_list[0] - add_sub_num 
            
        else:
            h2 = HSL_list[0] + add_sub_num
        HSL_list = [h2, HSL_list[1], HSL_list[2]]
        comp_color_list.append(HSL_list)

        
    
    print(comp_color_list)
    return comp_color_list


def complement_2(color: Color):
    R = round(math.sqrt(255**2 - color.r**2))
    G = round(math.sqrt(255**2 - color.g**2))
    B = round(math.sqrt(255**2 - color.b**2))
    return Color(R,G,B)

def complement_3(color: Color):
    R = color.b
    G = color.g
    B = color.r
    return Color(R,G,B)

def complement_4(color: Color):    
    comp_color = Color(255 - color.r, 255 - color.g, 255 - color.b, a=1.0)
    return comp_color

