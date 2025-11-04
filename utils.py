"""
Functions for validation.

"""

def validate_number(value: float, name: str) -> float:
    """
    Validate that value is a number.

    Parameters:
    - value: The value that needs to be validated
    - name (str): Name of the parameter
    
    """
    if not isinstance(value,(int, float)):
        raise TypeError(f"{name} must be a number, not {type(value)}")
    return float(value)


def validate_positive_number(value: float, name: str) -> float:
    """
    Validate that a value is a positive number.

    Parameters:
    - value: The value that needs to be validated
    - name (str): Name of the parameter

    """
    
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be anumber, not {type(value)}")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return float(value)
