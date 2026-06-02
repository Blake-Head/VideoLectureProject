from manim import *
from manimlib.imports import *

# Testing the embeded command
    # This new scene is writen from 3b1bs manim guide
class Embeded(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_A, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()

        self.embed()

        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(circle.animate.stretch(4, 0))
        self.play(Rotate(circle, 90 * DEGREES))
        self.play(circle.animate.shift(2 * RIGHT).scale(0.25))

        text = Text("""
                    This type of stuff is useful for
                    to develop new scenes -3b1b
        """)
        self.play(Write(text))

        always(circle.move_to, self.mouse_point)

# Need to see how 3b1b gets the embed comand from manimlib as it is not working