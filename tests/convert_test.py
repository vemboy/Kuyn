from kuyn.convert import *
from kuyn.color import Color
import pytest


class TestConvert:

    def test_RGB_to_HSL(self):
        color_1 = Color(r=50, g=168, b=82, a=1.0)
        global HSL
        HSL = RGB_to_HSL(color_1)
        assert HSL[0] == 136
        assert HSL[1] == 54
        assert HSL[2] == 43

    def test_HSL_to_RGB(self):
        color_1 = Color(r=50, g=168, b=82, a=1.0)
        RGB = HSL_to_RGB(HSL[0], HSL[1], HSL[2])
        assert RGB[0] == color_1.r
        assert RGB[1] == color_1.g
        assert RGB[2] == color_1.b

    def test_hex_to_RGB(self):
        hex_num_1 = '#32a852'
        RGB = hex_to_RGB(hex_num_1)
        assert RGB.r == 50
        assert RGB.g == 168
        assert RGB.b == 82

    def test_RGB_to_hex(self):
        hex_num_1 = '#32a852'
        color_1 = Color(r=50, g=168, b=82, a=1.0)
        hex_num = RGB_to_hex(color_1)
        assert hex_num == hex_num_1
