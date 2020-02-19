
from kuyn.util import *
from kuyn.color_util import *
from testing.util import *
from typing import NamedTuple, List
from kuyn.color import Color
import math
import sys
import itertools

class Palette: 
    def __init__(self, colors: List[Color]) -> None:
        self.colors = colors

    @property
    def colors(self):
        return self.__colors

    @colors.setter
    def colors(self, new_colors: List[Color]) -> None: 
        if(has_duplicate(new_colors, "Duplicate colors spotted", 2)):
            return

        else:
            self.__colors = new_colors

    def add(self, new_colors: List[Color]) -> None:
        if(has_duplicate(new_colors, "Duplicate colors spotted", 2)):
            return

        for i in new_colors:
            if(i in self.colors):
                print("Between the colors passed and the colors already in the Palette, duplicates are spotted.")
                return 

        self.colors.extend(new_colors)
        

    def avg_distance(self):
        distance = 0
        counter = 0
        for a, b in itertools.combinations(self.colors, 2):
            couple_distance = get_distance(a,b)
            distance = distance + couple_distance
            counter = counter + 1
        distance = distance/counter
        return distance

    def remove_extremes(self):
        if(len(self.colors) <= 1):
            print("Palette has less than 1 color inside!")
            return
        distance1 = get_distance(self.colors[0],self.colors[1])
        counter = 0
        extreme_colors = []
        for a, b in itertools.combinations(self.colors, 2):
            if(get_distance(a,b) > distance1):
                distance1 = get_distance(a,b)
                counter += 1
                extreme_colors += [a,b]
        for i in range(len(extreme_colors)):
            if extreme_colors[i] in self.colors:
                self.colors.remove(extreme_colors[i])

        
    def remove_outlier(self, n = 1):
        if(n > len(self.colors)):
            print("n cannot be larger than/equal to the amount of colors in the Palette")
            print("No colors were removed")
            return 
        if(len(self.colors) < 3):
            print("The Palette has less than 3 colors")
            print("No colors were removed")
            return 
        if(len(self.colors) == 0):
            print("The Palette has no colors inside!")
            print("No colors were removed")
            return
        all_selected = []
        a_0 = self.colors[0]
        distance = 0
        counter = 0
        for a, b in itertools.combinations(self.colors, 2):
            distance += get_distance(a,b)
            if(a_0 == a):
                counter += 1
                a_0 = self.colors[counter]
                all_selected.append(distance)
                distance = 0
        max_list = get_max(all_selected, n)
        for i in range(n):
            max_distance_index = all_selected.index(max_list[i])
            self.colors.remove(self.colors[max_distance_index])
        print(self.colors)


        


