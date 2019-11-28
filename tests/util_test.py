from kuyn.color import *
from kuyn.color_util import *
from testing.util import *
import pytest

class TestColor():
    def test_get_distance(self):
        color1 = Color(5,66,77)
        color2 = Color(223, 22, 53)

        distance = get_distance(color1, color2)
        assert distance == 223.6872817126624

    def test_invert(self):
        color1 = Color(5,66,77) 
        inverted = invert(color1)

        assert inverted == Color(250, 189, 178)



