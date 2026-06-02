from manim import *

class Pith1(Scene):
    def construct(self):
        sq = Star(stroke_color = GREEN, fill_color = BLUE, fill_opacity = 0.75
        )

        self.play(Create(sq), run_time = 3)
        self.wait()

class Pith2(Scene):
    def construct(self):
        sq = Circle(stroke_color = GREEN, fill_color = BLUE, fill_opacity = 0.75
        )

        self.play(Create(sq), run_time = 3)
        self.wait()

class Pith3(Scene):
    def construct(self):
        sq = Rectangle(stroke_color = GREEN, fill_color = BLUE, fill_opacity = 0.75
        )

        self.play(Create(sq), run_time = 3)
        self.wait()

class Pith4(Scene):
    def construct(self):
        sq = RegularPolygram(stroke_color = GREEN, fill_color = BLUE, fill_opacity = 0.75, num_vertices = 10
        )

        self.play(Create(sq), run_time = 3)
        self.wait()