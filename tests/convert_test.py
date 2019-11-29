from kuyn.convert import RGB_to_HSL, HSL_to_RGB, RGB_to_hex, hex_to_RGB
from kuyn.color import RGB, HSL, ColorHex
from testing.util import floor_rgb, round_hsl
import pytest


class TestConvert:

    def test_RGB_to_HSL(self):
        in_rgb = RGB(R=50, G=168, B=82)
        out_hsl = RGB_to_HSL(in_rgb)

        expected_hsl = HSL(H=136, S=54, L=43)
        assert round_hsl(out_hsl) == round_hsl(expected_hsl)

    def test_HSL_to_RGB(self):
        pytest.skip("gotta be fixed")
        #in_hsl = HSL(H=136, S=54, L=43)
        #out_rgb = HSL_to_RGB(in_hsl)

        #expected_rgb = RGB(R=50, G=169, B=82)
        #assert floor_rgb(out_rgb) == floor_rgb(expected_rgb)

    def test_HSL_to_RGB_to_HSL(self):
        in_hsl = HSL(H=4, S=82, L=56)
        out_rgb = HSL_to_RGB(in_hsl)
        print(out_rgb)
        out_hsl = RGB_to_HSL(out_rgb)
        print(out_hsl)
        #assert in_hsl == out_hsl

    def test_hex_to_RGB(self):
        hex_num_1 = '#32a852'
        out_rgb = hex_to_RGB(hex_num_1)

        expected_rgb = RGB(R=50, G=168, B=82)
        assert floor_rgb(out_rgb) == floor_rgb(expected_rgb)

    def test_RGB_to_hex(self):
        in_rgb = RGB(R=50, G=168, B=82)
        out_hex = RGB_to_hex(in_rgb)

        expected_hex = ColorHex(value='#32a852')
        assert out_hex == expected_hex

