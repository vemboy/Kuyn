from kuyn.transform import *
from kuyn.convert import *
import pytest


class TestTransform:

    def test_get_complement(self):

        color_1 = Color(r=64, g=24, b=222, a=1.0)
        comp = get_complement(color_1)
        assert comp == [(180, 220, 24), (64, 24, 220)]