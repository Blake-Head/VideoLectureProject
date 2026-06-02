from manim import *
import numpy as np

# Note: This file tests physics concepts without manim_physics dependency
# For actual electric field simulations, use manim_physics library

class ChargeVisualizationTest(Scene):
    """Test visualization of point charges"""
    def construct(self):
        # Create positive and negative charges
        positive_charge = Circle(radius=0.3, color=RED)
        positive_charge.set_fill(RED, opacity=0.8)
        positive_charge.shift(LEFT * 2)
        
        negative_charge = Circle(radius=0.3, color=BLUE)
        negative_charge.set_fill(BLUE, opacity=0.8)
        negative_charge.shift(RIGHT * 2)
        
        # Add charge symbols
        plus_sign = MathTex("+", color=WHITE).move_to(positive_charge.get_center())
        minus_sign = MathTex("-", color=WHITE).move_to(negative_charge.get_center())
        
        # Labels
        pos_label = MathTex(r"q_1 = +2 \mu C", color=RED)
        pos_label.next_to(positive_charge, DOWN, buff=0.5)
        
        neg_label = MathTex(r"q_2 = -3 \mu C", color=BLUE)
        neg_label.next_to(negative_charge, DOWN, buff=0.5)
        
        self.play(Create(positive_charge), Create(negative_charge))
        self.play(Write(plus_sign), Write(minus_sign))
        self.play(Write(pos_label), Write(neg_label))
        self.wait(3)

class VectorFieldTest(Scene):
    """Test creating vector field visualization"""
    def construct(self):
        # Create a grid of vectors to represent an electric field
        vectors = VGroup()
        
        for x in range(-3, 4):
            for y in range(-2, 3):
                if x == 0 and y == 0:
                    continue  # Skip center point
                
                start_point = np.array([x, y, 0])
                # Simulate field pointing away from origin
                direction = start_point / np.linalg.norm(start_point)
                end_point = start_point + 0.4 * direction
                
                vector = Arrow(start_point, end_point, color=YELLOW, stroke_width=3)
                vectors.add(vector)
        
        # Add a source charge at center
        source = Circle(radius=0.2, color=RED)
        source.set_fill(RED, opacity=1)
        source_label = MathTex("+Q", color=WHITE).scale(0.8)
        
        # Title
        title = Text("Electric Field Pattern", font_size=36)
        title.to_edge(UP)
        
        self.play(Write(title))
        self.play(Create(source), Write(source_label))
        self.play(Create(vectors, lag_ratio=0.1))
        self.wait(3)

class ForceVectorTest(Scene):
    """Test force vector between charges"""
    def construct(self):
        # Two charges
        q1 = Circle(radius=0.3, color=RED).set_fill(RED, opacity=0.8)
        q2 = Circle(radius=0.3, color=BLUE).set_fill(BLUE, opacity=0.8)
        
        q1.shift(LEFT * 3)
        q2.shift(RIGHT * 3)
        
        # Charge labels
        q1_label = MathTex("+q", color=WHITE).move_to(q1.get_center())
        q2_label = MathTex("-q", color=WHITE).move_to(q2.get_center())
        
        # Force vectors
        f1 = Arrow(q1.get_center(), q1.get_center() + RIGHT * 1.5, color=GREEN)
        f2 = Arrow(q2.get_center(), q2.get_center() + LEFT * 1.5, color=GREEN)
        
        # Force labels
        f1_label = MathTex(r"\vec{F}_{12}", color=GREEN).next_to(f1, UP)
        f2_label = MathTex(r"\vec{F}_{21}", color=GREEN).next_to(f2, UP)
        
        # Distance indicator
        distance_line = DashedLine(q1.get_center(), q2.get_center(), color=GRAY)
        distance_label = MathTex("r", color=GRAY).next_to(distance_line, UP)
        
        self.play(Create(q1), Create(q2))
        self.play(Write(q1_label), Write(q2_label))
        self.play(Create(distance_line), Write(distance_label))
        self.play(Create(f1), Create(f2))
        self.play(Write(f1_label), Write(f2_label))
        self.wait(3)

class MotionTest(Scene):
    """Test particle motion simulation"""
    def construct(self):
        # Create a particle
        particle = Circle(radius=0.2, color=YELLOW)
        particle.set_fill(YELLOW, opacity=0.8)
        particle.shift(LEFT * 4)
        
        # Create a path
        path = ParametricFunction(
            lambda t: np.array([
                -4 + 8 * t,
                2 * np.sin(2 * PI * t),
                0
            ]),
            t_range=[0, 1],
            color=WHITE
        )
        
        # Labels
        title = Text("Particle Motion", font_size=36)
        title.to_edge(UP)
        
        position_tracker = always_redraw(
            lambda: MathTex(
                f"x = {particle.get_center()[0]:.1f}",
                font_size=24,
                color=YELLOW
            ).to_corner(UL).shift(DOWN)
        )
        
        self.play(Write(title))
        self.play(Create(particle))
        self.play(Create(path))
        self.add(position_tracker)
        
        # Animate particle along path
        self.play(MoveAlongPath(particle, path), run_time=4, rate_func=linear)
        self.wait(2)

class WaveTest(Scene):
    """Test wave visualization"""
    def construct(self):
        # Create sine wave
        wave = ParametricFunction(
            lambda t: np.array([t, np.sin(t), 0]),
            t_range=[-2*PI, 2*PI],
            color=BLUE
        )
        
        # Create axes
        axes = Axes(
            x_range=[-8, 8, PI],
            y_range=[-2, 2, 1],
            axis_config={"color": GRAY}
        )
        
        # Labels
        title = Text("Sine Wave", font_size=36)
        title.to_edge(UP)
        
        equation = MathTex(r"y = \sin(x)", color=BLUE)
        equation.to_corner(UR)
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Write(equation))
        self.play(Create(wave), run_time=3)
        self.wait(2)