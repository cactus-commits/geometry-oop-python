import doctest
import math 
# https://www.geeksforgeeks.org/python/python-math-module/
from shape_3D import Shape3D
from utils import validate_positive_number

class Sphere(Shape3D):
    """
    A class representing a sphere

   Attributes:
    - x (float): x-coordinates of the sphere's center
    - y (float): y-coordinates of the sphere'scenter
    - z (float): y-coordinates of the sphere's center
    - radius (float): Radius of the sphere (read-only)
    - surface_area (float): Surface area of the sphere (read-only)
    - volume (float): Volume of the sphere (read-only)

    Methods:
    - translate(dx, dy, dz): Move the shape by dx, dy and dz (inherit from ShapeeD)
    - is_unit_sphere(): Check if the sphere is a unit circle (radius=1 and center of origin (0,0,0))

    Example usage:
    >>> sphere = Sphere(x=0, y=0, z=0, radius=5)
    >>> sphere.volume
    523.5987755982989
    >>> sphere.is_unit_sphere()
    False

    """
    def __init__(self, x=0, y=0, z=0, radius = 1):
        """
        Initialize a Sphere

        Parameters:
        - x (float): x-coordinates of center (default:0)
        - y (float): y-coordinates of center (default:0)
        - z (float): z-coordinates of center (default:0)
        - radius (float): Radius of the sphere (default:1) # <- needs to be a positive number
        """
        super().__init__(x, y, z)
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
    def surface_area(self):
        """Calculate the surface area (4 * pi * r^2)"""
        return 4 * math.pi * self.radius**2
    
    @property
    def volume(self):
        """Calculate the volume ((4/3) * pi * r^3)"""
        return (4/3) * math.pi * self.radius**3
    
    def is_unit_sphere(self):
        """Checks if this is a unit sphere (radius=1 and center of origin (0,0,0))"""
        
        return self.radius == 1 and self.x == 0 and self.y == 0
    
    def __str__(self):
        return f"This shere has it's center at ({self.x}, {self.y}, {self.z}) and has the radius {self.radius}"
    
    def __repr__(self):
        return f"Circle_coordinates(x={self.x}, y={self.y}, z={self.z} radius={self.radius})"

    if __name__ == "__main__":
        doctest.testmod(verbose=True)