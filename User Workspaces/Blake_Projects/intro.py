from manim import *

class Logo(Scene):
    def construct(self):
        logo = SVGMobject("cute-lion-logo.png")
        self.play(DrawBorderThenFill(logo))
        self.wait(1)
