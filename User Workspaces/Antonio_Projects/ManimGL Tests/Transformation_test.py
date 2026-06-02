from manim import *
from manimlib.imports import *
    # for all future code, use this import

class SquareToCircle(Scene):
    def construct(self):
        # Create the square first
        square = Square()
        square.set_fill(RED, opacity=0.5)

        # Create the circle
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)

        # Adding the shapes to the scene
        self.play(ShowCreation(square))
        self.wait(1)

        # Transformation time
        self.play(Transform(square, circle))
        self.wait(1)
