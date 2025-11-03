class Rectangle: 
    """
    A class representing a rectangle ans it's position.

    Attributes:
    - width (float): The with of the rectangle -> read-only
    - height (float): The height of the rectangle -> read only
    - area (float): The area of the rectangle -> read only 
    - x (float): The x-coordinate of the rectangles center 
    - y (float): The y-coordinate of the rectangles center
    - perimeter (float): The perimiter of the rectangle -> read-only

    """

# 1. Initializing the class rectangle
    def __init__(self, width:float, height:float, x:float, y:float =0):
        # using type hints to make it clearer and easier to understand the code and see bugs)

        # Validate and store dimensions
        self._width = self._validate_positive_number(width, "width")
        self._height = self._validate_positive_number(height, "hight")