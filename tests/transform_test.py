from kuyn.transform import *
from kuyn.convert import *
from kuyn.util import floor_rgb
import pytest


class TestTransform:

    def test_get_complement(self):
        color_1 = Color(r=64, g=24, b=222, a=1.0)
        comp = get_complement(color_1,2)
        """assert comp == [
            Color(r=64, g=24, b=220),
            Color(r=221, g=64, b=24),
            Color(r=25, g=220, b=64),
        ]"""

    def test_H_rotate(self):
        return 0