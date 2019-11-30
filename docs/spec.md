# Classes

## Color

A color represented in RGB

### Properties

- `a`: `float` `[0.0, 1.0]`
- `r`: `int` `[0-255]`
- `g`: `int` `[0-255]`
- `b`: `int` `[0-255]`

- `magnitude`: `float`
 - Distance of color from center of color wheel  

### Operators

#### Color and Color
- `Color``+``Color`
- `Color``-``Color`
- `Color``==``Color`
- `Color` `<` `Color` ????

#### Color and other
- `Color``+``int`
- `Color``-``int`
- `Color``*``int`


### Methods

- `Color getCompliments(int n=1)`
 - `n` is number of colors to return
- `Palette getAnalogous(float n=?)`
 -  `n` is number of colors to return 
- `Palette applyDistance(float distance, int n)`
 - `n` is number of colors to return
- `float distance(Color c)`


## Palette

A unique unordered set of colors

### Properties

- `colors`: `Set[Color]`
- `size`: `int` 

### Methods

- `averageDistance()`
- `add(Color c)`
- `remove(Color c)`
- `Color getFurthest(int n)`
 - Returns `n` colors that have the farthest distance from the others 


## ColorMap

a matrix of colors

### Init

ColorMap(width, height)
ColorMap(image)

### Properties

- `width`: `int`
- `height`: `int`
- `matrix`: `List[List[Color]]`

### Methods

- `show()`
 - Prints current state of matrix.
- `createImage(filetype)`
 - Makes an image, that is the visual representation of the matrix.
- `addColor(color)`
 - Adds color to matrix.
- `set(x: int, y: int, c: Color)`
- `fill(c: Color)`
- `avarageDistance()`
- `palette(int n)`
 - Creates a pallete with the first n amount of dom colors (n < x)
- `ReplaceAreas(int n, p)`
 - Finds all the colors that seem the same to the human eye that seem the same to the dom color, to the first n amount of dom colors. Replaces those areas with the palette given in parameters, if the amounts don't match, it replaces till either area's or the palette is finished. (IFFY)




## FileType

Enum representation of file types

- `JPEG`




