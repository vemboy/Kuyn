from kuyn.convert import *
from kuyn.color import RGB
import pytest


class TestConvert:

    def test_RGB_to_HSL(self):
        in_rgb = RGB(R=50, G=168, B=82)
        expected_hsl = RGB_to_HSL(in_rgb)
        assert expected_hsl.H == 136
        assert expected_hsl.S == 54
        assert expected_hsl.L == 43

    def test_HSL_to_RGB(self):
        in_rgb = RGB(R=50, G=168, B=82)
        hsl = RGB_to_HSL(in_rgb)
        out_rgb = HSL_to_RGB(hsl)
        assert in_rgb.R == out_rgb.R
        assert in_rgb.G == out_rgb.G
        assert in_rgb.B == out_rgb.B

    def test_hex_to_RGB(self):
        hex_num_1 = '#32a852'
        out_rgb = hex_to_RGB(hex_num_1)
        assert out_rgb.R == 50
        assert out_rgb.G == 168
        assert out_rgb.B == 82

    def test_RGB_to_hex(self):
        expected_hex = '#32a852'
        in_rgb = RGB(R=50, G=168, B=82)
        hex_num = RGB_to_hex(in_rgb)
        assert hex_num.value == expected_hex
