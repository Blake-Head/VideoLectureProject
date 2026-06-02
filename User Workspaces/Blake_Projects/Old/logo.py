from manim import *

config.background_color = WHITE

class Logo(Scene):
    def construct(self):

        shape_colors = YELLOW_D
        shape_opacity = 1
        text_stroke = 2

        vertices_tri = [
            np.array([-2, -2, 0]),  # Bottom-left
            np.array([4, -2, 0]),   # Bottom-right
            np.array([4, 2, 0]),   # Top-right
        ]
        tri = Polygon(*vertices_tri, 
                      color = BLACK, 
                      fill_color = shape_colors, 
                      fill_opacity = shape_opacity,
                      stroke_width = 5
                      ).shift(LEFT*1)
        

        vertices_cro = [
            np.array([-2,-2,0]),    # Bottom-left
            np.array([2, -2, 0]),   # Bottom-right
            np.array([1.5, 3 ,0]),  # Right tip
            np.array([1, 0, 0]),    # Right low-point
            np.array([0, 2, 0]),    # Middle Tip
            np.array([-1, 0, 0]),   # Left low-point
            np.array([-1.5, 3, 0]), # Left tip
        ]

        crown = Polygon(*vertices_cro,
                        color = BLACK,
                        fill_color = shape_colors,
                        fill_opacity = shape_opacity,
                        stroke_width = 5).scale(.3).shift(UP*1.7+LEFT*1).rotate(35*PI/180)
        
        arc = Arc(angle = PI/2, color = BLACK, stroke_width = 5).move_to(tri.get_bottom()).scale(.5).shift(UP*.25+LEFT*2)

        moto1 = Tex("Everything",color = PURE_RED, font_size = 60).to_edge(LEFT).shift(UP*1).set_stroke(width =text_stroke, color = BLACK)
        moto2 = Tex("is a",color = PURE_RED, font_size = 60).to_edge(LEFT).shift(UP*0).set_stroke(width =text_stroke, color = BLACK)
        moto3 = Tex("triangle.",color = PURE_RED, font_size = 60).to_edge(LEFT).shift(DOWN*1).set_stroke(width =text_stroke, color = BLACK)
        moto = VGroup(moto1, moto2, moto3)

        text_r = Tex("R", color = PURE_RED, font_size = 60).next_to(tri, UP).shift(DOWN*1.5).set_stroke(width =text_stroke, color = BLACK)
        text_cos = Tex("R cos$\\theta$", color = PURE_RED, font_size = 60).next_to(tri, DOWN).set_stroke(width =text_stroke, color = BLACK)
        text_sin = Tex("R sin$\\theta$", color = PURE_RED, font_size = 60).next_to(tri, RIGHT).set_stroke(width =text_stroke, color = BLACK).rotate(PI/2).shift(LEFT*.5)
        text_theta = Tex("$\\theta$", color = PURE_RED, font_size = 60).next_to(tri, DOWN).set_stroke(width =text_stroke, color = BLACK).next_to(arc, RIGHT).shift(UP*.25)

        self.play(DrawBorderThenFill(tri), run_time=3)
        self.play(Write(text_r))
        self.play(Create(arc))
        self.play(Write(text_theta))
        self.wait(1)
        self.play(Write(text_cos), Write(text_sin), run_time = 1)
        self.wait(1)
        self.play(DrawBorderThenFill(crown), run_time = 3)
        self.play(Flash(crown, line_length=1, flash_radius=1, color = shape_colors))
        self.play(Write(moto), run_time = 2)
        self.wait(4)