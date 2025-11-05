"""
Test file for Cube class to test functionalities.

"""

from pytest import raises
from cube import Cube

# 1. Creating a cube
def test_cube_creation():
    c = Cube(x=5, y=8, side_length=4)
    assert c.x == 5 and c.y == 8 and c.side_length == 4


# 2. Calculate surface area 
def test_cube_surface_area():
    c = Cube(side_length=4)
    assert c.surface_area == 96

# 3. Calculate volume 
def test_cube_volume():
    c = Cube(side_length=4)
    assert c.volume == 64

# 4. Check if cube is unit cube
def test_is_unit_cube():
    c1 = Cube(x=0, y=0, z=0, side_length=1)
    assert c1.is_unit_cube() is True

    c2 = Cube(x=0, y=0, z=0, side_length=3)
    assert c2.is_unit_cube() is False

# 5. Moving the cube
def test_cube_translate():
    c = Cube(x=0, y=0, z=0, side_length=4)
    c.translate(10,10,10)
    assert c.x == 10 and c.y == 10 and c.z == 10

# 6. Compairing two different cubes
def test_comparison():
    c1 = Cube(side_length=5)
    c2 = Cube(side_length=8)
    assert c1 < c2

# 7. Error handling
def test_type_error(): # -> Type error
    with raises(TypeError):
        Cube(side_length="five")

def test_value_error(): # -> Value error
    with raises(ValueError):
        Cube(side_length=-1)