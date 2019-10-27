from kuyn.util import get_distance
from typing import NamedTuple, List
from kuyn.color import Color
import math
import sys
import itertools

class Pallete: 
    def __init__(self, colors: List[Color]) -> None:
        self.colors = colors

    @property
    def colors(self):
        return self.__colors

    @colors.setter
    def colors(self, new_colors: List[Color], key=None):
        #self.__colors = new_colors
        #return(list(map(next, list(map(itemgetter(1), groupby(new_colors, key))))))
        for a, b in itertools.combinations(new_colors, 2):
            if(a == b):
                raise Exception("Duplicate colors spotted")
            else:
                self.__colors = new_colors

    def add(self, new_colors: List[Color]):
        for a, b in itertools.combinations(new_colors, 2):
            if(a == b):
                raise Exception("Duplicate colors spotted")
        else:
            self.colors.append(new_colors)

    def avg_distance(self):
        distance = 0
        counter = 0
        for a, b in itertools.combinations(self.colors, 2):
            couple_distance = get_distance(a,b)
            distance = distance + couple_distance
            counter = counter + 1
        print(distance)