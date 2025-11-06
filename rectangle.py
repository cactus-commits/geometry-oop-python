import doctest
from shape import Shape
from utils import validate_positive_number

class Rectangle(Shape): 
   
    """
    A class representing a rectangle.

    Attributes:
    - x (float): x-coordinate of the rectangle's center 
    - y (float): y-coordinate of the rectangle's center
    - width (float): The width of the rectangle
    - height (float): The height of the rectangle 
    - area (float): The area of the rectangle (read only)
    - perimeter (float): The perimeter of the rectangle (read only)

    Methods:
    - is_square(): Check if rectangle is a square
    - translate(dx, dy): Move the rectangle (inherit from Shape)

    Example usage:
    >>> r = Rectangle(x=0, y=0, width=4, height=3)
    >>> r.area
    12.0
    >>> r.is_square()
    False

    """

    def __init__(self, x=0, y=0, width=1, height=1): # <- Setting width and height to 1 because we need a positive number
        
        """
        Initializing a Rectangle
        
        Parameters: 
        x (float): x-coordinates of center (default: 0)
        y (float): y-coordinates of center (default: 0)
        width (float): The width of the recrangle (default:1)
        height (float): The height of the rectangle (default:1)    
        
        """
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Getting the width"""
        return self._width
    
    @width.setter
    def width(self, value):
        """Validate and set the width"""
        self._width = validate_positive_number(value, "width")
    
    @property
    def height(self):
        """Getting the height"""
        return self._height
    
    @height.setter
    def height(self, value):
        """Validate and set the height"""
        self._height = validate_positive_number(value, "height")

    @property
    def area(self):
        """Calculate the area: width * height"""
        return self.width * self.height
    
    @property
    def perimeter(self):
        """Calculate the perimeter: 2 * (width + height)"""
        return 2 * (self.width + self.height)
    
    def is_square(self):
        """Check if the rectangle is a square (width == hight)"""
        return self.width == self.height
    
    def __str__(self):
        return f"This rectangle has it's center at ({self.x}, {self.y}), width {self.width} and height {self.height}"
    
    def __repr__(self):
        return f"Rectangle_coordinates(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    if __name__ == "__main__":
        doctest.testmod(verbose=True)