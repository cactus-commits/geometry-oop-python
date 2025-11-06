from utils import validate_shape_comparison

class AllShape:
    """
    A class that provides comparision operators for 2D and 3D shapes. 

    - 2D shapes -> compared by area
    - 3D shapes -> compared by volume

    Methods to be implementet by child classes:
    - comparison_metric(): Returns the value to use for the comparisons
    
    """

    def comparison_metric(self):

        """
        Returns the metric used for comparing shapes.

        - 2D shapes: returns area
        - 3D shapes: return volume
        
        """
        raise NotImplementedError(f"Comparison_metric must be implemented in child class")
    
    def __eq__(self, other: object) -> bool:
        """ Check if two shapes are equal (have the same comparison metric) -> bool """
        if not isinstance(other, AllShape):
            return False
        return self.comparison_metric() == other.comparison_metric()

    def __lt__(self, other):
        """Check if this shape is smaller than another"""
        validate_shape_comparison(other, AllShape)
        return self.comparison_metric() < other.comparison_metric()
    
    def __le__(self, other):
        """Check if this shape is smaller than or equal to another"""
        validate_shape_comparison(other, AllShape)
        return self.comparison_metric <= other.comparison_metric
    
    def __gt__(self, other):
        """Check if this shape is larger than another"""
        validate_shape_comparison(other, AllShape)
        return self.comparison_metric > other.comparison_metric
    
    def __ge__(self, other):
        """Check if this shape is larger than or equal to another"""
        validate_shape_comparison(other, AllShape)
        return self.comparison_metric >= other.comparison_metric