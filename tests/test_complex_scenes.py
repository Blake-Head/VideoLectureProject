from manim import *
import numpy as np

class InteractiveSceneTest(Scene):
    """Test a complex scene with multiple interacting elements"""
    def construct(self):
        # Title
        title = Text("Complex Physics Demonstration", font_size=36)
        title.to_edge(UP)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": GRAY, "stroke_width": 2}
        )
        
        # Add axis labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        
        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

class MultiObjectAnimationTest(Scene):
    """Test scene with many objects animating together"""
    def construct(self):
        # Create a system of planets orbiting
        sun = Circle(radius=0.3, color=YELLOW)
        sun.set_fill(YELLOW, opacity=0.8)
        
        # Create planets at different distances
        planets = VGroup()
        planet_colors = [BLUE, RED, GREEN, ORANGE]
        orbit_radii = [1.5, 2.5, 3.5, 4.5]
        
        for i, (color, radius) in enumerate(zip(planet_colors, orbit_radii)):
            planet = Circle(radius=0.1, color=color)
            planet.set_fill(color, opacity=0.8)
            planet.move_to(RIGHT * radius)
            planets.add(planet)
        
        # Create orbit paths
        orbits = VGroup()
        for radius in orbit_radii:
            orbit = Circle(radius=radius, color=GRAY, stroke_width=1)
            orbit.set_fill(opacity=0)
            orbits.add(orbit)
        
        # Labels
        title = Text("Planetary Motion System", font_size=32)
        title.to_edge(UP)
        
        self.play(Write(title))
        self.play(Create(sun))
        self.play(Create(orbits))
        self.play(Create(planets))
        
        # Animate orbital motion
        def create_orbit_animation(planet, radius, period):
            return Rotating(
                planet,
                angle=2*PI,
                about_point=ORIGIN,
                run_time=period,
                rate_func=linear
            )
        
        # Different orbital periods
        periods = [3, 4, 5, 6]
        orbit_animations = [
            create_orbit_animation(planet, radius, period)
            for planet, radius, period in zip(planets, orbit_radii, periods)
        ]
        
        self.play(*orbit_animations)
        self.wait(1)

class LayeredVisualizationTest(Scene):
    """Test layered visualization with background, midground, and foreground"""
    def construct(self):
        # Background: Grid
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        
        # Midground: Electric field lines
        field_lines = VGroup()
        for angle in np.linspace(0, 2*PI, 12, endpoint=False):
            start = ORIGIN
            end = 2.5 * (np.cos(angle) * RIGHT + np.sin(angle) * UP)
            line = Arrow(start, end, color=YELLOW, stroke_width=2)
            field_lines.add(line)
        
        # Foreground: Charges
        positive_charge = Circle(radius=0.4, color=RED)
        positive_charge.set_fill(RED, opacity=0.9)
        plus_sign = MathTex("+", color=WHITE, font_size=36)
        plus_sign.move_to(positive_charge.get_center())
        
        # Moving test charge
        test_charge = Circle(radius=0.2, color=BLUE)
        test_charge.set_fill(BLUE, opacity=0.8)
        test_charge.shift(RIGHT * 3)
        minus_sign = MathTex("-", color=WHITE, font_size=24)
        minus_sign.move_to(test_charge.get_center())
        
        # Equation display
        coulomb_law = MathTex(
            r"F = k \frac{q_1 q_2}{r^2}",
            font_size=32
        )
        coulomb_law.to_corner(UR)
        coulomb_law.add_background_rectangle(color=BLACK, opacity=0.8)
        
        # Build scene layer by layer
        self.play(Create(grid))
        self.play(Create(field_lines, lag_ratio=0.1))
        self.play(Create(positive_charge), Write(plus_sign))
        self.play(Create(test_charge), Write(minus_sign))
        self.play(Write(coulomb_law))
        
        # Animate test charge movement
        path = Arc(
            start_angle=0,
            angle=PI,
            radius=3,
            arc_center=ORIGIN
        )
        
        self.play(
            MoveAlongPath(test_charge, path),
            MoveAlongPath(minus_sign, path),
            run_time=4
        )
        
        self.wait(2)

class PhysicsLectureSceneTest(Scene):
    """Test a scene that mimics a physics lecture slide"""
    def construct(self):
        # Lecture title
        title = Text("Electric Field and Force", font_size=40, color=BLUE)
        title.to_edge(UP)
        
        # Subtitle
        subtitle = Text("Coulomb's Law Demonstration", font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        # Key concepts box
        concepts_box = Rectangle(width=6, height=3, color=WHITE)
        concepts_box.to_edge(LEFT).shift(DOWN * 0.5)
        
        concepts_title = Text("Key Concepts:", font_size=20, color=BLUE)
        concepts_title.next_to(concepts_box.get_top(), DOWN, buff=0.2, aligned_edge=LEFT)
        concepts_title.shift(RIGHT * 0.2)
        
        concept_list = VGroup(
            Text("• Electric charges create fields", font_size=16),
            Text("• Like charges repel", font_size=16),
            Text("• Unlike charges attract", font_size=16),
            Text("• Force decreases with distance²", font_size=16)
        )
        
        for i, concept in enumerate(concept_list):
            concept.next_to(concepts_title, DOWN, buff=0.3 + i * 0.4, aligned_edge=LEFT)
            concept.shift(RIGHT * 0.2)
        
        # Demonstration area
        demo_area = Rectangle(width=5, height=3, color=WHITE)
        demo_area.to_edge(RIGHT).shift(DOWN * 0.5)
        
        # Charges in demo area
        q1 = Circle(radius=0.3, color=RED).set_fill(RED, opacity=0.8)
        q2 = Circle(radius=0.3, color=BLUE).set_fill(BLUE, opacity=0.8)
        
        q1.move_to(demo_area.get_center() + LEFT * 1.5)
        q2.move_to(demo_area.get_center() + RIGHT * 1.5)
        
        q1_label = MathTex("+q", color=WHITE).move_to(q1.get_center())
        q2_label = MathTex("-q", color=WHITE).move_to(q2.get_center())
        
        # Force arrows
        force_q1 = Arrow(
            q1.get_center(), 
            q1.get_center() + RIGHT * 0.8, 
            color=GREEN, 
            stroke_width=4
        )
        force_q2 = Arrow(
            q2.get_center(), 
            q2.get_center() + LEFT * 0.8, 
            color=GREEN, 
            stroke_width=4
        )
        
        force_label = Text("Attractive Force", font_size=16, color=GREEN)
        force_label.next_to(demo_area, DOWN, buff=0.2)
        
        # Build the scene
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)
        
        self.play(Create(concepts_box))
        self.play(Write(concepts_title))
        for concept in concept_list:
            self.play(Write(concept))
            self.wait(0.3)
        
        self.play(Create(demo_area))
        self.play(Create(q1), Create(q2))
        self.play(Write(q1_label), Write(q2_label))
        self.wait(1)
        
        self.play(Create(force_q1), Create(force_q2))
        self.play(Write(force_label))
        self.wait(2)
        
        # Show charges moving together
        self.play(
            q1.animate.shift(RIGHT * 0.3),
            q1_label.animate.shift(RIGHT * 0.3),
            q2.animate.shift(LEFT * 0.3),
            q2_label.animate.shift(LEFT * 0.3),
            run_time=2
        )
        
        self.wait(3)