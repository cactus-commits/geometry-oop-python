"""
Test file for Circle class to test functionalities.

"""
from pytest import raises
from circle import Circle
import math

# 1. Test creating a circle
def test_circle_creation():
    c = Circle(x=2, y=3, radius=10)
    assert c.x == 2 and c.y ==3 and c.radius == 10

# 2. Calculate area 
def test_area():
    c = Circle(radius=3)
    # abs() suggested from LLM after multiple failed test without it.
    # by using abs(absolute value) it checks if the values are “close enough”.
    assert abs(c.area - math.pi * 3**2) < 0.0001

# 3. Calculate perimeter 
def test_perimeter():
    c = Circle(radius=3)
    assert abs(c.perimeter - 6*math.pi) < 0.0001

# 4. Check if circle is unit circle
def test_is_unit_circle():
    c1 = Circle(x=0, y=0, radius=1)
    assert c1.is_unit_circle() is True

    c2 = Circle(x=1, y=0, radius = 3)
    assert c2.is_unit_circle() is False

# 5. Moving the circle
def test_translate():
    c = Circle(x=0, y=0, radius=9)
    c.translate(10, 12)
    assert c.x == 10 and c.y == 12

# 6. Compairing two different circles
def test_comparison():
    c1 = Circle(radius=1)
    c2 = Circle(radius=5)
    assert c1 < c2

# 7. Error handling
def test_type_error():
    with raises(TypeError):
        Circle(radius="eight")

def test_value_error():
    with raises(ValueError):
        Circle(radius=-2)
