import math
import sys
import imageio
import itertools
from typing import NamedTuple, List
from kuyn.color import Color
from PIL import Image
import numpy as np
from kuyn.util import *
from kuyn.color_util import *
from testing.util import *
from skimage import *
import pandas as pd

dt = np.dtype(object) 

class Colormap:
    def __init__(self, color_list: List[List[Color]]) -> None:
        self.color_list = color_list

    @property
    def color_list(self):
        return self.__color_list

    @color_list.setter
    def color_list(self, new_color_list_list: List[List[Color]]) -> None:
        self.__color_list = np.array(new_color_list_list)
        # self.__color_list = np.array([], dtype=Color)
        # new_color_list_list = np.asarray(new_color_list_list)
        # for i in new_color_list_list:
        #     self.__color_list = np.concatenate(new_color_list_list[i], axis=0, dtype=Color)

    #def addColor(self, new_color: Color) -> None:
    #    self.color_list = np.array(self.color_list)

    def dimensions(self) -> None:
        matrix = np.array(self.color_list)
        return matrix.shape
    
    def height(self) -> None:
        matrix = np.array(self.color_list)
        shape = matrix.shape[0]
        return shape

    def width(self) -> None:
        matrix = np.array(self.color_list)
        shape = matrix.shape[1]
        return shape        
        
    def show(self) -> None:
        return self.color_list
    
    def get_image(self, img: str) -> None:
        #np.set_printoptions(threshold=sys.maxsize)
        img = Image.open(img)
        self.color_list = np.array(img)
        
    def createImage(self) -> None:
        arr = self.color_list
        print(type(arr[0][0][0]))
        print(arr.shape)
        imageio.imwrite("image2.png", img_as_uint(arr))

    def randomImage(self, height, width) -> None:
        r = np.empty((height, width, 3), dtype=Color)
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                r[i][j] = list(random_color().RGB)
        self.color_list = r.astype(np.uint8)
        return self.color_list

    # def avarageDistance(self) -> None:
    #     average_d = 0
    #     counter = 0
    #     matrix = self.color_list
    #     for a, b in itertools.combinations(matrix, 2):
    #         print(str(a) + ": A")
    #         print(str(b) + ": B")
    #         distance = get_distance(Color(a[0], a[1], a[2]), Color(b[0], b[1], b[2]))
    #         average_d = average_d + distance
    #         counter = counter + 1
    #     average_d = average_d/counter
    #     print(counter)

    def extract_dom(self) -> None:
        matrix = self.color_list
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                print(most_frequent(matrix[i]))



                

        # self.color_list = np.array([])
        
        # x = 0 
        # while(x < height*width):
        #     rc = np.array([tuple(random_color().RGB)])
        #     print(rc)
        #     self.color_list = np.concatenate((self.color_list, rc))
        #     x = x + 1
        # self.color_list = self.color_list.reshape(-1, width)
        # return self.color_list
        
        




        