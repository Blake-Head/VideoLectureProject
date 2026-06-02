from manim import *

class BasicShapesTest(Scene):
    """Test basic geometric shapes and their properties"""
    def construct(self):
        # Create basic shapes
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=RED)
        triangle = Triangle(color=GREEN)
        
        # Position shapes
        circle.shift(LEFT * 3)
        square.shift(RIGHT * 3)
        triangle.shift(UP * 2)
        
        # Add shapes to scene
        self.play(Create(circle), Create(square), Create(triangle))
        self.wait(2)

class ColorAndFillTest(Scene):
    """Test different colors and fill options"""
    def construct(self):
        # Create shapes with different fill properties
        solid_circle = Circle().set_fill(YELLOW, opacity=1.0)
        transparent_square = Square().set_fill(PURPLE, opacity=0.5)
        outlined_triangle = Triangle().set_stroke(ORANGE, width=5)
        
        # Position shapes
        solid_circle.shift(LEFT * 2)
        transparent_square.shift(RIGHT * 2)
        outlined_triangle.shift(DOWN * 2)
        
        # Animate creation
        self.play(FadeIn(solid_circle))
        self.play(DrawBorderThenFill(transparent_square))
        self.play(ShowCreation(outlined_triangle))
        self.wait(2)

class TransformationTest(Scene):
    """Test shape transformations"""
    def construct(self):
        # Create initial shape
        square = Square(color=BLUE)
        square.set_fill(BLUE, opacity=0.7)
        
        self.play(Create(square))
        self.wait(1)
        
        # Transform to circle
        circle = Circle(color=RED)
        circle.set_fill(RED, opacity=0.7)
        
        self.play(Transform(square, circle))
        self.wait(1)
        
        # Transform to triangle
        triangle = Triangle(color=GREEN)
        triangle.set_fill(GREEN, opacity=0.7)
        
        self.play(Transform(square, triangle))
        self.wait(2)

class MovementTest(Scene):
    """Test object movement and positioning"""
    def construct(self):
        # Create a dot to move around
        dot = Dot(color=YELLOW, radius=0.2)
        
        self.play(Create(dot))
        
        # Move in different directions
        self.play(dot.animate.shift(RIGHT * 3))
        self.play(dot.animate.shift(UP * 2))
        self.play(dot.animate.shift(LEFT * 6))
        self.play(dot.animate.shift(DOWN * 4))
        self.play(dot.animate.move_to(ORIGIN))
        
        self.wait(1)

class ScalingTest(Scene):
    """Test scaling and rotation"""
    def construct(self):
        # Create a rectangle
        rect = Rectangle(width=2, height=1, color=PINK)
        rect.set_fill(PINK, opacity=0.5)
        
        self.play(Create(rect))
        
        # Scale up and down
        self.play(rect.animate.scale(2))
        self.play(rect.animate.scale(0.5))
        
        # Rotate
        self.play(Rotate(rect, PI/4))
        self.play(Rotate(rect, PI/2))
        
        self.wait(2)