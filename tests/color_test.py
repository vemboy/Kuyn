from kuyn.color import Color
import pytest


class TestColor:
    def test_getters(self):
        color = Color(r=1, g=2, b=3, a=0.1)
        assert color.r == 1
        assert color.g == 2
        assert color.b == 3
        assert color.a == 0.1

    def test_setters(self):
        color = Color(r=1, g=2, b=3, a=0.1)
        color.r = 2
        color.g = 3
        color.b = 4
        color.a = 0.2
        assert color.r == 2
        assert color.g == 3
        assert color.b == 4
        assert color.a == 0.2

    def test_setter_invalid(self):
        color = Color(r=1, g=2, b=3, a=0.1)
        with pytest.raises(Exception):
            color.r = 256
        with pytest.raises(Exception):
            color.g = 256
        with pytest.raises(Exception):
            color.b = 256
        with pytest.raises(Exception):
            color.a = 101
        with pytest.raises(Exception):
            color.r = -1
        with pytest.raises(Exception):
            color.g = -1
        with pytest.raises(Exception):
            color.b = -1
        with pytest.raises(Exception):
            color.a = -1

    def test_setrgba(self):
        color = Color(r=1, g=2, b=3, a=1)
        color.set_rgba(r=1, g=1, b=1, a=1)
        assert color.r == 1
        assert color.g == 1
        assert color.b == 1
        assert color.a == 1

    def test_eq(self):
        color_1 = Color(r=1, g=2, b=3, a=1)
        color_2 = Color(r=1, g=2, b=3, a=1)
        assert color_1 == color_2

    def test_add(self):
        color_1 = Color(r=1, g=2, b=3, a=1.0)
        color_2 = Color(r=1, g=2, b=3, a=1.0)
        assert color_1 + 1 == Color(r=2, g=3, b=4, a=1.0)
        assert color_1 + color_2 == Color(r=2, g=4, b=6, a=1.0)

    def test_sub(self):
        color_1 = Color(r=1, g=2, b=3, a=1.0)
        color_2 = Color(r=1, g=2, b=3, a=1.0)
        assert color_1 - 1 == Color(r=0, g=1, b=2, a=1.0)
        assert color_1 - color_2 == Color(r=0, g=0, b=0, a=1.0)

    def test_mult(self):
        color_1 = Color(r=1, g=2, b=3, a=0.5)
        assert color_1 * 2 == Color(r=2, g=4, b=6, a=1)

    def test_distance(self):
        color_1 = Color(r=178, g=200, b=216, a=1.0)
        color_2 = Color(r=10, g=211, b=67, a=1.0)
        get_distance(color_1, color_2)
