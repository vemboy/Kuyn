from kuyn.color import Color
import math
# HSL - RGB


def RGB_to_HSL(color: Color):
    r = color.r/255
    g = color.g/255
    b = color.b/255

    color_list = [r, g, b]
    max_val = max(color_list)
    min_val = min(color_list)
    max_minus_min = max_val - min_val
    max_plus_min = max_val + min_val

    # Calculate Luninance
    L = max_plus_min/2

    # Grayscale color
    if(min_val == max_val):
        S = 0
        H = 0
        return H, S, round(L * 100)
    
    # Calculate saturation
    if(L < 0.5):
        S = max_minus_min / max_plus_min
    else:
        S = max_minus_min / (2.0 - max_minus_min)

    # Calculate hue
    if(r > g and r > b):
        H_num = (g - b)/max_minus_min
    elif(g > r and g > b):
        H_num = 2.0 + (b - r)/max_minus_min
    elif(b > r and b > g):
        H_num = 4.0 + (r - g)/max_minus_min

    # Conver hue to degrees
    H_degree = H_num * 60
    if(H_degree < 0):
        H_degree += 360

    H = H_degree/360

    return H, S, L

def HSL_to_RGB(H,S,L):
    if(H == 0 and S == 0):
        R = L/100*255
        G = L/100*255
        B = L/100*255
    
    if(L < 0.5):
        temp_1 = L * (1.0 + S)
    else:
        temp_1 = L + S - (L * S)
    
    temp_2 = 2 * L - temp_1

    temp_R = H + 0.333
    temp_G = H 
    temp_B = H - 0.333

    if(temp_R > 1):
        temp_R = temp_R - 1
    elif(temp_R < 0):
        temp_R = temp_R + 1
        
    if(temp_G > 1):
        temp_G = temp_G - 1
    elif(temp_G < 0):
        temp_G = temp_G + 1
        
    if(temp_B > 1):
        temp_B = temp_B - 1
    elif(temp_B < 0):
        temp_B = temp_B + 1
    
    if(6 * temp_R < 1):
        R = temp_2 + (temp_1 - temp_2) * 6 * temp_R
    elif(6 * temp_R > 1):
        if(2 * temp_R < 1):
            R = temp_1
        elif(2 * temp_R > 1):
            if(3 * temp_R < 2): 
                R = temp_2 + (temp_1 - temp_2) * (0.666 - temp_R) * 6
            elif(3 * temp_R > 2):
                R = temp_2

    if(6 * temp_G < 1):
        G = temp_2 + (temp_1 - temp_2) * 6 * temp_G
    elif(6 * temp_G > 1):
        if(2 * temp_G < 1):
            G = temp_1
        elif(2 * temp_G > 1):
            if(3 * temp_G < 2):
                G = temp_2 + ((temp_1 - temp_2) * (0.666 - temp_G) * 6)
            elif(3 * temp_G > 2):
                G = temp_2

    if(6 * temp_B < 1):
        B = temp_2 + (temp_1 - temp_2) * 6 * temp_B
    elif(6 * temp_B > 1):
        if(2 * temp_B < 1):
            B = temp_1
        elif(2 * temp_B > 1):
            if(3 * temp_B < 2):
                B = temp_2 + (temp_1 - temp_2) * (0.666 - temp_B) * 6
            elif(3 * temp_B > 2):
                B = temp_2

    return(round(R*255),round(G*255),round(B*255))



# HEX - RGB

def hex_to_RGB(hex_num):
    h = hex_num.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return Color(RGB[0], RGB[1], RGB[2])

def RGB_to_hex(color: Color):
    hex_tamplate = '#%02x%02x%02x'
    hex_out = hex_tamplate % tuple(color.r, color.g, color.b)
    return hex_out
    