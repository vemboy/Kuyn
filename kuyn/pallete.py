from kuyn.util import *
from testing.util import *
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
    def colors(self, new_colors: List[Color]) -> None: 
        for a, b in itertools.combinations(new_colors, 2):
            if(a == b):
                print("Duplicate colors spotted")
                return


        self.__colors = new_colors

    def add(self, new_colors: List[Color]) -> None:
        for a, b in itertools.combinations(new_colors, 2):
            if(a == b):
                print("Duplicate colors spotted in the colors passed.")
                return 

        for i in new_colors:
            if(i in self.colors):
                print("Between the colors passed and the colors already in the Pallete, duplicates are spotted.")
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
            print("Pallete is empty!")
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
            print("n cannot be larger than/equal to the amount of colors in the Pallete")
            print("No colors were removed")
            return 
        if(len(self.colors) < 3):
            print("The Pallete has less than 3 colors")
            return 
        if(len(self.colors) == 0):
            print("The Pallete has no colors inside!")
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


        


