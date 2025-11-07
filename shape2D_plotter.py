import matplotlib.pyplot as plt
import matplotlib.patches as patches
from circle import Circle
from rectangle import Rectangle

class Shape2DPlotter:

    """
    Class for plotting multiple 2D shapes (Circle and Rectangle) in the same axes.



    """

    def __init__(self):
        """Initialize the plotter figure and axes"""
        self.shapes = [] # List of shapes
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')  # Make circles look circular instead of oval - got help from LLM to do this since all my circles were oval.

    def add_shape(self, shape):
        """
        Add a shape to plot.

        Parameters:
        - shape: A 2D shape object (Circle or Rectangle)

        """
        if not isinstance(shape, (Circle, Rectangle)):
            raise TypeError(f"Sorry, can only plot Circle or Rectangle for now")
        self.shapes.append(shape)

    def plot(self):
        """Draw all the shapes"""
        for shape in self.shapes:
            if isinstance(shape, Circle):
                # Creating a circle patch"
                circle = patches.Circle(
                    (shape.x, shape.y), # <- The center position
                    shape.radius, # <- radius
                    fill=False,
                    edgecolor="purple"

                    )

                self.ax.add_patch(circle)

            elif isinstance(shape, Rectangle):
                # For plotting a rectangle we need the lower left corner (https://www.geeksforgeeks.org/python/matplotlib-patches-rectangle-in-python/)
                lower_left_x = shape.x - shape.width/2
                lower_left_y = shape.y - shape.height/2

                # Create a rectangle patch
                rect = patches.Rectangle(
                    (lower_left_x, lower_left_y),
                    shape.width,
                    shape.height,
                    fill=False,
                    edgecolor="orange"
                    )
                self.ax.add_patch(rect)

        self.ax.autoscale() # This autoscales the graph - got this from LLM after not being able to figure out why I could only see parts of the shapes in the graph
        self.ax.set(title= "2D Shapes", xlabel="x", ylabel="y")

    def show(self):
        """Show the plot"""
        plt.show()
