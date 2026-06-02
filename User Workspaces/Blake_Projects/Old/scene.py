from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class Testing(Scene):
    def construct(self):
        
        name = Tex("Blake").to_edge(UL, buff = 0.5)
        sq = Square(side_length = 0.5, fill_color=GREEN, fill_opacity=0.75).shift(LEFT * 3)
        tri = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), run_time = 2)
        self.play(Create(tri))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time=1)
        self.play(sq.animate.scale(3), tri.animate.to_edge(DL), run_time=3)
        self.wait()

class Getters(Scene):
    def construct(self):

        rect = Rectangle(
            color = WHITE, 
            height=3, 
            width=2.5
            ).to_edge(UL)

        circ = Circle().to_edge(DOWN)

        arrow = always_redraw(
            lambda : Line(
                start=rect.get_center(), 
                end = circ.get_center()
                ).add_tip())

        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait()
        self.play(rect.animate.to_edge(UR), circ.animate.scale(2), run_time = 4)
        self.play(circ.animate.to_edge(UL))
        self.play(rect.animate.to_edge(DR))
        self.play(circ.animate.to_edge(UR))

class Updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        box = always_redraw(lambda:
                            SurroundingRectangle(num, 
                                   color = RED, 
                                   fill_opacity = 0.4, 
                                   fill_color = BLUE, 
                                   buff = 0.5))
        
        name = always_redraw(lambda:
                             Tex("Blake").next_to(box, DOWN, buff = 0.25))

        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT * 2), run_time = 2)
        self.wait()

class ValueTrackers(Scene):
    def construct(self):

        k = ValueTracker(5)

        num = always_redraw(lambda:
                            DecimalNumber().set_value(k.get_value()))

        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(0), run_time = 5, rate_func=smooth)

class Graphing(Scene):
    def construct(self):
        plane = (
            NumberPlane(x_range = [-4, 4, 2], x_length=7, y_range=[0,16,4],  y_length=8)
            .to_edge(DOWN)
            .add_coordinates()
        )

        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

        parab = plane.plot(lambda x : 
                                x**2, 
                                x_range=[-4,4],
                                color = GREEN)
        
        func_label = (
            MathTex("f(x)={x}^{2}")
            .scale(0.6)
            .next_to(parab, RIGHT, buff=0.5)
            .set_color(GREEN)
        )

        area = plane.get_riemann_rectangles(graph = parab, x_range=[-2,2], dx=0.2, stroke_width=0.1, stroke_color=WHITE)


        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(labels)))
        self.play(Create(VGroup(parab, func_label), run_time = 3))
        self.wait()
        self.play(Create(area))
        self.wait()

class UpdaterGraphing(Scene):

    def construct(self):

        k = ValueTracker(-4) # This is where k will START

        ax = (
            Axes
            (x_range=[-4,4,1], 
             y_range=[-2,16,2], 
             x_length = 10, 
             y_length = 6)
             .to_edge(DOWN)
             .add_coordinates()
        ).set_color(WHITE)

        func = (
            ax.plot(lambda x: x**2,
                    x_range=[-4,4],
                    color=BLUE)
                )
        
        # always_redraw allows the slope to be re-drawn each time k updates 
        # make sure when adding a always_redraw function to also add a lambda function right after
        slope = always_redraw(
            lambda: ax.get_secant_slope_group(
            x = k.get_value(), 
            graph = func, 
            dx = 0.01, 
            secant_line_color=GREEN, 
            secant_line_length=7)
                 )
        
        pt = (
            always_redraw(lambda : Dot().move_to(ax.c2p(k.get_value(), 
                                                        func.underlying_function(k.get_value())))
            )
        )
        
        self.add(ax, func, slope, pt) # This won't animiate anything, just instantly put on screen
        self.wait()
        self.play(k.animate.set_value(4), run_time = 6)
