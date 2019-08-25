from kuyn.transform import *
from kuyn.convert import *
from testing.util import floor_rgb
import pytest


class TestTransform:

    def test_get_complement(self):
        color_1 = Color(r=64, g=24, b=222, a=1.0)
        comp = get_complement(color_1,2)
        assert comp == [
            Color(r=63, g=24, b=220, a=1.0),
            Color(r=220, g=64, b=24, a=1.0),
            Color(r=24, g=220, b=64, a=1.0),
        ]

    def test_H_rotate(self):
        assert "done" == "not"
