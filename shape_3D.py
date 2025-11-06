from all_shape import AllShape 
from utils import validate_number

class Shape3D(AllShape):

    """
    A class for geometric shapes.
    Provides common functionality for 3D shapes. 

    Attributes:
    - x (float): x-coordinates of the shapes center
    - y (float): y-coordinates of the shapes center
    - z (float): z-coordinate of the shape's center
    - surface_area (float): Surface area of the shape (read-only)
    - volume (float): Volume of the shape (read-only)

    Methods:
    - translate(dx, dy): Move the shape by dx and dy
    - comparison_metric(self): Returns the metric used for comparing shapes (inherits from AllShape)
    
    """

    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        """
        Initialize a 3D Shape with x, y and z center coordinates.

        Parameters:
        - x (float): x-coordinate of the center (default:0)
        - y (float): y-coordinate of the center (default:0)
        - z (float): z-coordinate of the center (default:0)
        
        """
        self.x = x
        self.y = y
        self.z = z

    @property
    def x(self): 
        """Get the x-coordinate"""
        return self._x
    
    @x.setter
    def x(self, value): 
        """Validate before setting x-coordinate"""
        self._x = validate_number(value, "x")

    
    @property
    def y(self):
        """Get the y-coordinate"""
        return self._y 
    
    @y.setter 
    def y(self, value):
        """Validate before setting y-coordinate"""
        self._y = validate_number(value, "y")

    @property
    def z(self):
        """Get the z-coordinate"""
        return self._z 
    
    @z.setter 
    def z(self, value):
        """Validate before setting z-coordinate"""
        self._z = validate_number(value, "z")
    
    def translate(self, dx: float, dy: float, dz: float) -> None:
        """
        Move the shape by dx and dy

        Parameters:
        - dx (float): Distance to move in x-direction
        - dy (float): Distance to move in y-direction
        - dz (float): Distance to move in z-direction

        """
        dx = validate_number(dx, "dx")
        dy = validate_number(dy, "dy")
        dz = validate_number(dz, "dz")

        self._x += dx
        self._y += dy
        self._z += dz

    def comparison_metric(self):
        """Returns the volume of the 3D shape comparison"""
        return self.volume
    
    
