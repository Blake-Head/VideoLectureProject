from manim import *

class PointParticle(Scene):
    def construct(self):

        ground = Line(start=8*LEFT, end=8*RIGHT).to_edge(DOWN)
        sq = Square(side_length=3, fill_color = BLUE, fill_opacity = 0.7).to_corner(DL)
        text1 = Tex("For much of this class, we actually treat object as POINTS").to_edge(UP)
        text2 = Tex("This is an approximation!").next_to(text1, DOWN)

        dot = Dot(color=RED).move_to(sq.get_center())
        #sq_dot = VGroup(sq, dot)

        self.add(ground, text1, text2, sq, dot)
        #self.wait(1)
        self.play(sq.animate.to_corner(DR), dot.animate.shift(RIGHT*10))
        self.play(sq.animate.to_corner(DL), dot.animate.shift(LEFT*10))
        self.play(sq.animate.to_corner(DR), dot.animate.shift(RIGHT*10), FadeOut(sq))
        self.play(sq.animate.to_corner(DL), dot.animate.shift(LEFT*10))