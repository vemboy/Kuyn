from kuyn.transform import *
from kuyn.convert import *
import pytest

color_1 = Color(r=64, g=24, b=222, a=1.0)

class TestTransform:

    def test_get_complement(self):

        get_complement(color_1,3)
    
    def test_compement_234(self):
        
        RGB = complement_2(color_1)
        RGB2 = complement_3(color_1)
        RGB3 = complement_4(color_1)

        print(RGB)
        print(RGB2)
        print(RGB3)

