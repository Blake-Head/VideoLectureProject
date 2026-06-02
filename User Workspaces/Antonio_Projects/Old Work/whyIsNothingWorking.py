from manim import *
from manimlib.imports import *
#from manim_physics import *
#import numpy as np

# Code to test why literally all of the previous made scene do not run
class ImSad(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)

        self.add(circle)
        self.play(Create(circle))
        self.play(ShowCreation(circle))
        self.wait(1)

# Code produces a recursion error

# Now says no Scenes in module

# Rewrite Circle to Sqaure
# class CircleToSquare(Scene):
#     def construct(self):
#         circle = Circle()
#         circle.set_fill(RED, opacity=0.5)

#         square = Square()
#         square.set_fill(BLUE, opacity=0.5)

#         self.play(ShowCreation(circle))
#         self.wait(1)

#         self.play(Transform(circle, square))
#         self.wait(1)

# Literally the same code as the other transformation_test.py except swapped
#   circle with sqaure and it does not run

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
