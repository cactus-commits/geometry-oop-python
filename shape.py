from utils import validate_number

class Shape:

    """
    A class for geometric shapes.
    Provides common functionality for 2D shapes. 

    Attributes:
    - x (float): x-coordinates of the shapes center
    - y (float): y-coordinates of the shapes center
    - area (float): Area of the shape (read-only)
    - perimeter (float): Perimeter of the shape (read-only)

    Methods:
    - translate(dx, dy): Move the shape by dx and dy
    
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize a Shape with x and y center coordinates.

        Parameters:
        - x (float): x-coordinate of the center (default:0)
        - y (float): y-coordinate of the center (default:0)
        
        """
        self.x = x
        self.y = y

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
    
    def translate(self, dx: float, dy: float) -> None:
        """
        Move the shape by dx and dy

        Parameters:
        - dx (float): Distance to move in x-direction
        - dy (float): Distance to move in y-direction

        """
        dx = validate_number(dx, "dx")
        dy = validate_number(dy, "dy")

        self._x += dx
        self._y += dy

    
