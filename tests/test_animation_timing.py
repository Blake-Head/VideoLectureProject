from manim import *

class TimingBasicsTest(Scene):
    """Test basic timing and waiting"""
    def construct(self):
        circle = Circle(color=BLUE)
        
        self.play(Create(circle))
        self.wait(2)  # Wait 2 seconds
        
        self.play(circle.animate.set_color(RED))
        self.wait(1)  # Wait 1 second
        
        self.play(FadeOut(circle))
        self.wait(0.5)  # Wait half a second

class SequentialAnimationsTest(Scene):
    """Test sequential animations"""
    def construct(self):
        shapes = VGroup(
            Circle(color=RED).shift(LEFT * 2),
            Square(color=GREEN),
            Triangle(color=BLUE).shift(RIGHT * 2)
        )
        
        # Create shapes one by one
        for shape in shapes:
            self.play(Create(shape))
            self.wait(0.5)
        
        # Transform all shapes sequentially
        self.play(shapes[0].animate.shift(UP))
        self.play(shapes[1].animate.rotate(PI/4))
        self.play(shapes[2].animate.scale(1.5))
        
        self.wait(2)

class SimultaneousAnimationsTest(Scene):
    """Test simultaneous animations"""
    def construct(self):
        shapes = VGroup(
            Circle(color=RED).shift(LEFT * 2),
            Square(color=GREEN),
            Triangle(color=BLUE).shift(RIGHT * 2)
        )
        
        # Create all shapes simultaneously
        self.play(*[Create(shape) for shape in shapes])
        self.wait(1)
        
        # Animate all shapes simultaneously
        self.play(
            shapes[0].animate.shift(UP * 2),
            shapes[1].animate.rotate(PI),
            shapes[2].animate.scale(0.5).set_color(YELLOW)
        )
        
        self.wait(2)

class RunTimeTest(Scene):
    """Test different run times for animations"""
    def construct(self):
        dots = VGroup(*[
            Dot().shift(UP * 2 + RIGHT * (i - 2)) 
            for i in range(5)
        ])
        
        labels = VGroup(*[
            Text(f"{0.5 + i * 0.5}s", font_size=20).next_to(dot, DOWN)
            for i, dot in enumerate(dots)
        ])
        
        self.add(dots, labels)
        
        # Animate dots with different run times
        animations = [
            dot.animate.shift(DOWN * 3)
            for dot in dots
        ]
        
        run_times = [0.5, 1.0, 1.5, 2.0, 2.5]
        
        self.play(*[
            anim.set_run_time(rt) for anim, rt in zip(animations, run_times)
        ])
        
        self.wait(1)

class RateFunctionTest(Scene):
    """Test different rate functions"""
    def construct(self):
        # Create dots for different rate functions
        dots = VGroup(*[
            Dot(color=BLUE).shift(LEFT * 4 + UP * (1.5 - i * 0.75))
            for i in range(5)
        ])
        
        # Labels for rate functions
        labels = VGroup(
            Text("linear", font_size=20),
            Text("smooth", font_size=20),
            Text("rush_into", font_size=20),
            Text("rush_from", font_size=20),
            Text("there_and_back", font_size=20)
        )
        
        for i, (dot, label) in enumerate(zip(dots, labels)):
            label.next_to(dot, LEFT, buff=0.5)
        
        self.add(dots, labels)
        
        # Animate with different rate functions
        rate_functions = [linear, smooth, rush_into, rush_from, there_and_back]
        
        self.play(*[
            dot.animate.shift(RIGHT * 8).set_run_time(3)
            for dot in dots
        ])
        
        self.wait(1)

class LagRatioTest(Scene):
    """Test lag ratio for staggered animations"""
    def construct(self):
        # Create a grid of squares
        squares = VGroup(*[
            Square(side_length=0.5, color=BLUE).shift(
                RIGHT * (i % 5 - 2) + UP * (1 - i // 5)
            )
            for i in range(15)
        ])
        
        title = Text("Lag Ratio Demo", font_size=36)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Create squares with lag ratio
        self.play(Create(squares, lag_ratio=0.1))
        self.wait(1)
        
        # Change color with lag ratio
        self.play(squares.animate.set_color(RED), lag_ratio=0.05)
        self.wait(1)
        
        # Scale with lag ratio
        self.play(squares.animate.scale(1.5), lag_ratio=0.1)
        self.wait(2)

class ComplexTimingTest(Scene):
    """Test complex timing combinations"""
    def construct(self):
        # Create multiple objects
        center_circle = Circle(radius=1, color=YELLOW)
        outer_circles = VGroup(*[
            Circle(radius=0.3, color=BLUE).shift(
                2 * RIGHT * np.cos(i * PI / 3) + 
                2 * UP * np.sin(i * PI / 3)
            )
            for i in range(6)
        ])
        
        # Phase 1: Create center first
        self.play(Create(center_circle))
        self.wait(0.5)
        
        # Phase 2: Create outer circles with lag
        self.play(Create(outer_circles, lag_ratio=0.2))
        self.wait(1)
        
        # Phase 3: Simultaneous complex animation
        self.play(
            center_circle.animate.scale(0.5).set_color(RED),
            outer_circles.animate.rotate(PI, about_point=ORIGIN),
            run_time=2
        )
        
        # Phase 4: Sequential cleanup
        self.play(FadeOut(center_circle))
        self.play(FadeOut(outer_circles, lag_ratio=0.1))
        
        self.wait(1)