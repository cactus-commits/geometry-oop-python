import doctest
import math 
# https://www.geeksforgeeks.org/python/python-math-module/
from shape import Shape
from utils import validate_positive_number

class Circle(Shape):
    """
    A class representing a circle

   Attributes:
    - x (float): x-coordinates of the circle's center
    - y (float): y-coordinates of the circle's center
    - radius (float): Radius of the circle (read-only)
    - area (float): Area of the circle (read-only)
    - perimeter (float): Perimeter of the circle (read-only)

    Methods:
    - translate(dx, dy): Move the shape by dx and dy (inherit from Shape)
    - is_unit_circle(): Check if the circle is a unit circle (radius=1 and center of origin (0,0))

    Example usage:
    >>> circle = Circle(x=0, y=0, radius=5)
    >>> circle.area
    78.53981633974483
    >>> circle.is_unit_circle()
    False

    """
    def __init__(self, x=0, y=0, radius = 1):
        """
        Initialize a Circle

        Parameters:
        - x (float): x-coordinates of center (default:0)
        - y (float): y-coordinates of center (default:0)
        - radius (float): Radius of the circle (default:1) # <- needs to be a positive number

        """
        super().__init__(x, y)
        self.radius = radius

    
    @property
    def radius(self): 
        """Geting the radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Validating and setting the radius"""
        self._radius = validate_positive_number(value, "radius")

    @property
    def area(self):
        """Calculate the area (pi * r^2)"""
        return math.pi * self.radius ** 2
    
    @property
    def perimeter(self):
        """Calculate the perimiter (2 * pi * r)"""
        return 2 * math.pi * self.radius
    
    def is_unit_circle(self):
        """Checks if this is a unit circle (radius=1 and center of origin (0,0))"""
        
        return self.radius == 1 and self.x == 0 and self.y == 0
    
    def __str__(self):
        return f"This circle has it's center at ({self.x}, {self.y}) and has the radius {self.radius}"
    
    def __repr__(self):
        return f"Circle_coordinates(x={self.x}, y={self.y}, radius={self.radius})"

    if __name__ == "__main__":
        doctest.testmod(verbose=True)