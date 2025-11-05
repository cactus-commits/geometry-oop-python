import doctest
from shape_3D import Shape3D
from utils import validate_positive_number

class Cube(Shape3D):
    """
    A class representing a cube.

   Attributes:
    - x (float): x-coordinates of the cubes's center
    - y (float): y-coordinates of the cubes's center
    - z (float): z-coordinates of the cubes's center
    - side_length (float): Side length of the cube (read-only)
    - surface_area (float): Surface area of the cubes (read-only)
    - volume (float): Volume of the cubes (read-only)

    Methods:
    - translate(dx, dy, dz): Move the shape by dx, dy and dz (inherit from Shape3D)
    - is_unit_cube(): Check if the cube is a unit cube (side=1 and center of origin (0,0,0))

    Example usage:
    >>> cube = Cube(x=0, y=0, z=0, side_length=5)
    >>> cube.volume
    125.0
    >>> cube.is_unit_cube()
    False

    """
    def __init__(self, x=0, y=0, z=0, side_length=1):
        """
        Initialize a Cube

        Parameters:
        - x (float): x-coordinates of center (default:0)
        - y (float): y-coordinates of center (default:0)
        - z (float): z-coordinates of center (default:0)
        - side_length (float): Side length of the cube (default:1)

        """
        super().__init__(x, y, z)
        self.side_length = side_length

    
    @property
    def side_length(self): 
        """Geting the length of the side"""
        return self._side_length
    
    @side_length.setter
    def side_length(self, value):
        """Validating and setting the side length"""
        self._side_length = validate_positive_number(value, "side")

    @property
    def surface_area(self):
        """Calculate the surface area (6 * side length^2)"""
        return 6 * self.side_length ** 2
    
    @property
    def volume(self):
        """Calculate the volume (side length^3)"""
        return self.side_length**3
    
    def is_unit_cube(self):
        """Checks if this is a unit cube (side length=1 and center of origin (0,0,0))"""
        return self.side_length == 1 and self.x == 0 and self.y == 0 and self.z == 0
    
    def __str__(self):
        return f"This cube has it's center at ({self.x}, {self.y}, {self.z}) and has the side length {self.side_length}"
    
    def __repr__(self):
        return f"Cube_coordinates(x={self.x}, y={self.y}, z={self.z}, side_length={self.side_length})"

    if __name__ == "__main__":
        doctest.testmod(verbose=True)