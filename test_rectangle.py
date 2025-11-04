"""
Test file for Rectangle class to test functionalities.

"""

from pytest import raises
from rectangle import Rectangle

# 1. Creating a rectangle
def test_rectangle_creation():
    r = Rectangle(x=5, y=8, width=2, height=4)
    assert r.x == 5 and r.y == 8 and r.width == 2 and r.height == 4


# 2. Calculate area 
def test_rectangle_area():
    r = Rectangle(width=2, height=4)
    assert r.area == 8

# 3. Calculate perimeter 
def test_rectangle_perimeter():
    r = Rectangle(width=2, height=4)
    assert r.perimeter == 12

# 4. Check if rectangle is square
def test_is_square():

    square = Rectangle(width=4, height=4)
    assert square.is_square() is True

    not_square = Rectangle(width=5, height=3)
    assert not_square.is_square() is False

# 5. Moving the rectangle
def test_rectangle_translate():
    r = Rectangle(x=0, y=0, width=2, height=4)
    r.translate(10,10)
    assert r.x == 10 and r.y == 10

# 6. Compairing two different rectangle
def test_comparison():
    r1 = Rectangle(width=5, height=5)
    r2 = Rectangle(width=8, height=8)
    assert r1 < r2

# 7. Error handling
def test_type_error():
    with raises(TypeError):
        Rectangle(width="five")

def test_value_error():
    with raises(ValueError):
        Rectangle(height=-1)