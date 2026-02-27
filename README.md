# Geometry OOP - Python

Object-oriented Python project implementing 2D and 3D geometric shapes using class inheritance, operator overloading, and matplotlib visualization.

Built as part of my data engineering studies — first deep dive into OOP design with UML planning before implementation.

---

## Stack
Python, Matplotlib, Pytest

---

## Class Structure

| Class | Type | Inherits from |
|-------|------|---------------|
| `AllShape` | Base | — |
| `Shape` | 2D base | `AllShape` |
| `Shape3D` | 3D base | `AllShape` |
| `Circle` | 2D shape | `Shape` |
| `Rectangle` | 2D shape | `Shape` |
| `Sphere` | 3D shape | `Shape3D` |
| `Cube` | 3D shape | `Shape3D` |
| `Shape2DPlotter` | Utility | — |

2D shapes are compared by area, 3D shapes by volume.

---

## How to Run
```bash
# Manual tests
jupyter notebook test_manual.ipynb

# Unit tests
pytest test_circle.py test_rectangle.py test_sphere.py test_cube.py
```

---

*First time designing a class hierarchy from scratch using UML — learned a lot about inheritance, operator overloading, and when to push logic into base classes.*
