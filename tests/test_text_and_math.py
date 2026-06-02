from manim import *

class TextTest(Scene):
    """Test basic text rendering"""
    def construct(self):
        # Create simple text
        title = Text("Physics Animations", font_size=48)
        title.to_edge(UP)
        
        subtitle = Text("Created with Manim", font_size=24, color=BLUE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)

class MathTexTest(Scene):
    """Test LaTeX mathematical expressions"""
    def construct(self):
        # Electric field equation
        eq1 = MathTex(r"\vec{E} = \frac{1}{4\pi\epsilon_0} \frac{q}{r^2} \hat{r}")
        eq1.scale(1.5)
        
        # Coulomb's law
        eq2 = MathTex(r"F = k \frac{q_1 q_2}{r^2}")
        eq2.next_to(eq1, DOWN, buff=1)
        eq2.set_color(RED)
        
        # Gauss's law
        eq3 = MathTex(r"\oint \vec{E} \cdot d\vec{A} = \frac{Q_{enc}}{\epsilon_0}")
        eq3.next_to(eq2, DOWN, buff=1)
        eq3.set_color(GREEN)
        
        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(1)
        self.play(Write(eq3))
        self.wait(3)

class LabeledDiagramTest(Scene):
    """Test creating labeled diagrams"""
    def construct(self):
        # Create a coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": GRAY}
        )
        
        # Create points
        point_a = Dot(axes.coords_to_point(-2, 1), color=RED)
        point_b = Dot(axes.coords_to_point(2, -1), color=BLUE)
        
        # Labels
        label_a = MathTex("q_1", color=RED).next_to(point_a, UP)
        label_b = MathTex("q_2", color=BLUE).next_to(point_b, DOWN)
        
        # Vector between points
        vector = Arrow(point_a.get_center(), point_b.get_center(), color=YELLOW)
        vector_label = MathTex(r"\vec{r}", color=YELLOW).next_to(vector, UP)
        
        # Add everything to scene
        self.play(Create(axes))
        self.play(Create(point_a), Create(point_b))
        self.play(Write(label_a), Write(label_b))
        self.play(Create(vector))
        self.play(Write(vector_label))
        self.wait(3)

class EquationAnimationTest(Scene):
    """Test animating equation transformations"""
    def construct(self):
        # Start with basic force equation
        eq1 = MathTex("F", "=", "m", "a")
        eq1.scale(2)
        
        self.play(Write(eq1))
        self.wait(1)
        
        # Transform to Newton's second law with acceleration
        eq2 = MathTex("F", "=", "m", r"\frac{dv}{dt}")
        eq2.scale(2)
        
        self.play(Transform(eq1, eq2))
        self.wait(1)
        
        # Show specific case for gravity
        eq3 = MathTex("F", "=", "m", "g")
        eq3.scale(2)
        eq3[3].set_color(RED)  # Highlight g
        
        self.play(Transform(eq1, eq3))
        self.wait(2)

class FormattedTextTest(Scene):
    """Test different text formatting options"""
    def construct(self):
        # Title
        title = Text("Text Formatting Examples", font_size=36)
        title.to_edge(UP)
        
        # Different font sizes
        large_text = Text("Large Text", font_size=48, color=RED)
        medium_text = Text("Medium Text", font_size=32, color=GREEN)
        small_text = Text("Small Text", font_size=16, color=BLUE)
        
        # Position texts
        large_text.shift(UP)
        small_text.shift(DOWN * 2)
        
        # Styled text
        bold_text = Text("Bold Text", font="Arial", weight=BOLD, color=ORANGE)
        bold_text.shift(DOWN * 3)
        
        self.play(Write(title))
        self.play(Write(large_text))
        self.play(Write(medium_text))
        self.play(Write(small_text))
        self.play(Write(bold_text))
        self.wait(3)