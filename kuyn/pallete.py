from kuyn.util import get_distance, get_max
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
    def colors(self, new_colors: List[Color]):
        for a, b in itertools.combinations(new_colors, 2):
            if(a == b):
                print("Duplicate colors spotted")
                return 0


        self.__colors = new_colors

    def add(self, new_colors: List[Color]):
        for a, b in itertools.combinations(new_colors, 2):
            if(a == b):
                print("Duplicate colors spotted")
                return 0

        for i in new_colors:
            if(i in self.colors):
                print("Duplicate colors spotted")
                return 0

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
        distance1 = get_distance(self.colors[0],self.colors[1])
        counter = 0
        color_pairs = []
        for a, b in itertools.combinations(self.colors, 2):
            if(get_distance(a,b) > distance1):
                distance1 = get_distance(a,b)
                counter += 1
                color_pairs += [a,b]
        for i in range(len(color_pairs)):
            if color_pairs[i] in self.colors:
                self.colors.remove(color_pairs[i])

        
    def remove_outlier(self, n = 1):
        if(n > len(self.colors) or n > len(self.colors)):
            print("n cannot be larger than/equal to the amount of colors in the Pallete")
            return 0
        if(len(self.colors) < 3):
            print("The Pallete has less than 3 colors")
            return 0
        all_list = []
        a_0 = self.colors[0]
        distance = 0
        counter = 0
        for a, b in itertools.combinations(self.colors, 2):
            distance += get_distance(a,b)
            if(a_0 == a):
                counter += 1
                a_0 = self.colors[counter]
                all_list.append(distance)
                distance = 0
        max_list = get_max(all_list, n)
        for i in range(n):
            max_distance_index = all_list.index(max_list[i])
            self.colors.remove(self.colors[max_distance_index])


        


