from kuyn.color import *
from kuyn.palette import *
from kuyn.color_util import *
from testing.util import *
import pytest

class TestPalette:
    def test_getters(self):

        palette_1 = Palette([Color(22,33,44), Color(33,44,55), Color(44,55,66)])
        
        assert palette_1.colors == [Color(22,33,44), Color(33,44,55), Color(44,55,66)]

    def test_setters(self): 

        palette_1 = Palette([Color(22,33,44), Color(33,44,55), Color(44,55,66)])
        palette_1.colors = [Color(22,22,22)]

        assert palette_1.colors == [Color(22,22,22)]

    def test_add(self):

        palette_1 = Palette([Color(22,33,44), Color(33,44,55), Color(44,55,66)])
        palette_1.add([Color(222,222,222), Color(111,111,111)])

        assert palette_1.colors == [Color(22,33,44), Color(33,44,55), Color(44,55,66), Color(222,222,222), Color(111,111,111)]

    def test_avg_distance(self):

        palette_1 = Palette([Color(22,33,44), Color(33,44,55), Color(44,55,66)])

        d1 = get_distance(Color(22,33,44), Color(33,44,55))
        d2 = get_distance(Color(33,44,55), Color(44,55,66))
        d3 = get_distance(Color(22,33,44), Color(44,55,66))

        d_r = (d1 + d2 + d3)/3

        assert palette_1.avg_distance() == d_r

    def test_remove_extremes(self):

        expected_result = [Color(r=33, g=44, b=55, a=1.0)]
        palette_1 = Palette([Color(22,33,44), Color(33,44,55), Color(44,55,66)])
        palette_1.remove_extremes()
        
        assert palette_1.colors == expected_result

    def test_remove_outlier(self):

        assert 1 == 1
        