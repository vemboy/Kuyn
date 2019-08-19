class Color:
    def __init__(self, a: int, r: int, g: int, b: int, magnitude: float) -> None:
        self.a = a
        self.r = r
        self.g = g
        self.b = b
        self.magnitude = magnitude


    #Addition of 2 colors //// Addition of a color and int

    def __add__(self, other) -> list:


        if isinstance(other, int):
            new_a = self.a + other
            new_r = self.r + other
            new_g = self.g + other
            new_b = self.b + other
            return(list([new_a, new_r, new_g, new_b]))

        elif isinstance(other, Color):
            return list([self.a + other.a, self.r + other.r, self.g + other.g, self.b + other.b])

        else:
            return_error = list(["Nothing added?"])
            return(return_error)

    #Substraction of 2 colors //// Substraction of a color and int

    def __sub__(self, other) -> list:
        
        if isinstance(other, int):
            new_a = self.a - other
            new_r = self.r - other
            new_g = self.g - other
            new_b = self.b - other
            return(list([new_a, new_r, new_g, new_b]))

        elif isinstance(other, Color):
            return list([self.a - other.a, self.r - other.r, self.g - other.g, self.b - other.b])

        else:
            return_error = list(["Nothing added?"])
            return(return_error)


    #Checking for Equality of 2 colors

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Color):
            if(self.a == other.a and self.r == other.r and self.g == other.g and self.b == other.b):
                return True
        return False



    

    #Multiplication of a color and int

    def __mul__(self, multiplied_float: float) -> list:
        
        new_a = self.a * multiplied_float
        new_r = self.r * multiplied_float
        new_g = self.g * multiplied_float
        new_b = self.b * multiplied_float
        if(new_a > 100):
            if(new_r > 255 or new_g > 255 or new_b > 255):
                error_rgb = "Red, Green or Blue CANNOT be more than 255"
            error_a = "Alpha cannot be larger than 100"   
        elif(new_r > 255 or new_g > 255 or new_b > 255):
            error_rgb = "Red, Green or Blue CANNOT be more than 255"

        return(list([new_a, new_r, new_g, new_b]))
        


color1 = Color(20,40,25,53, 0)
color2 = Color(204,34,53,65, 0)

print(color1 + color2)
print(color1 + 2)
print(color1 * 2)
print(color1 - color2)
