from kuyn.palette import *
from kuyn.color import *
from kuyn.colormap import *
from kuyn.color_util import *
import numpy as np
from PIL import Image
import imageio
import sys

"""


1) Implement the image color taking code into Kuyn
2) Create functions relating to upcoming project (like changing certain colors, and making similar colors form into 1 color)
3) Start project with library -> Taking an artists multiple paintings and seeing if the distances between those images are close
-> Trying to (by will) make a images distance smaller by changing colors but not changing the picture -> Applying some artists average distances to others
-> Creating an image with randomly generated colors -> ETC ETC


"""

colormap_1 = Colormap([
    [Color(1,1,1),Color(2,2,2)],
    [Color(3,3,3),Color(4,4,4)],
    [Color(3,3,3),Color(4,4,4)]
])


# array = np.zeros([100, 200, 3], dtype=np.uint8)
# print(array)     
# array[:,:100] = [255, 128, 0] #Orange left side
# array[:,100:] = [0, 0, 255]   #Blue right side

# img = Image.fromarray(array)
# img.show()

#np.set_printoptions(threshold=sys.maxsize)

#img = Image.open('testrgb.png')
#arr = np.array(img)

#print(arr)
# matrix = [
#     [(1,1,1),(2,2,2), (4,4,4), (5,5,5)],
#     [(3,3,3),(4,4,4), (66,55,44), (66,44,33)],
#     [(1,1,1),(2,2,2), (4,4,4), (5,5,5)],
#     [(3,3,3),(4,4,4), (66,55,44), (66,44,33)],
#     [(1,1,1),(2,2,2), (4,4,4), (5,5,5)],
#     [(3,3,3),(4,4,4), (66,55,44), (66,44,33)],
#     [(1,1,1),(2,2,2), (4,4,4), (5,5,5)],
#     [(3,3,3),(4,4,4), (66,55,44), (66,44,33)],
#     [(1,1,1),(2,2,2), (4,4,4), (5,5,5)],
#     [(3,3,3),(4,4,4), (66,55,44), (66,44,33)],
#     [(1,1,1),(2,2,2), (4,4,4), (5,5,5)],
#     [(3,3,3),(4,4,4), (66,55,44), (66,44,33)],
#     [(1,1,1),(2,2,2), (4,4,4), (5,5,5)],
#     [(3,3,3),(4,4,4), (66,55,44), (66,44,33)],
#     [(1,1,1),(2,2,2), (4,4,4), (5,5,5)],
#     [(3,3,3),(4,4,4), (66,55,44), (66,44,33)],
#     [(1,1,1),(2,2,2), (4,4,4), (5,5,5)],
#     [(3,3,3),(4,4,4), (66,55,44), (66,44,33)]

    
# ]

#imageio.imwrite("image.png", arr)

# colormap_2 = Colormap([])
# colormap_2.get_image('test.png')
# print(colormap_2.show())

colormap_2 = Colormap([])
colormap_2.randomImage(100,100)
colormap_2.show()
colormap_2.extract_dom()


