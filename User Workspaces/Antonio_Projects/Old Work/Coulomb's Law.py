from manim import *

class CoulombsLawMayer(Scene):
    def construct(self):
        # Title: Signaling and Personalization
        title = Text("Coulomb's Law Explained")
        title.to_edge(UP)
        self.play(Write(title))
        
        # Introduction: Coherence and Pre-training
        intro = Text("Understanding the force between electric charges.")
        intro.next_to(title, DOWN)
        self.play(Write(intro))
        self.wait(2)
        self.remove(intro)
        
        # Equation: Coherence, Signaling, and Redundancy
        equation = MathTex("F = k \\frac{Q_1 Q_2}{r^2}")
        equation.scale(1.5)
        self.play(Write(equation))
        self.wait(1)
        
        # Components: Redundancy, Segmenting, and Spatial Contiguity
        explanation_F = Tex(r"$F$: Force between the charges (Newtons)")
        explanation_F.next_to(equation, DOWN)
        self.play(Write(explanation_F))
        self.highlight_variable(equation, 0, YELLOW)
        
        self.remove(explanation_F)
        explanation_k = Tex(r"$k$: Coulomb's constant $8.99 \times 10^9 \, \text{Nm}^2/\text{C}^2$")
        explanation_k.next_to(equation, DOWN)
        self.play(Write(explanation_k))
        self.highlight_variable(equation, 2, BLUE)
        
        self.remove(explanation_k)
        explanation_Q1 = Tex(r"$Q_1$: Magnitude of charge 1 (Coulombs)")
        explanation_Q1.next_to(equation, DOWN)
        self.play(Write(explanation_Q1))
        self.highlight_variable(equation, 4, GREEN)
        
        self.remove(explanation_Q1)
        explanation_Q2 = Tex(r"$Q_2$: Magnitude of charge 2 (Coulombs)")
        explanation_Q2.next_to(equation, DOWN)
        self.play(Write(explanation_Q2))
        self.highlight_variable(equation, 5, GREEN)
        
        self.remove(explanation_Q2)
        explanation_r = Tex(r"$r$: Distance between the charges (meters)")
        explanation_r.next_to(equation, DOWN)
        self.play(Write(explanation_r))
        self.highlight_variable(equation, 8, RED)
        
        self.wait(2)
        
        # Summary: Coherence and Temporal Contiguity
        summary = Text("Coulomb's Law describes the force between two charges,")
        summary2 = Text("which is proportional to the product of the charges")
        summary3 = Text("and inversely proportional to the square of the distance between them.")
        summary.next_to(equation, DOWN)
        summary2.next_to(summary, DOWN)
        summary3.next_to(summary2, DOWN)
        self.play(Write(summary))
        self.play(Write(summary2))
        self.play(Write(summary3))
        
        self.wait(3)
        self.clear()
    
    def highlight_variable(self, equation, index, color):
        highlight = SurroundingRectangle(equation[0][index], color=color, buff=0.1)
        self.play(Create(highlight))
        self.wait(1)
        self.play(FadeOut(highlight))