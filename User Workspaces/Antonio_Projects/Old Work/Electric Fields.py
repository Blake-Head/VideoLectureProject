from manim import *

class Introduction(Scene):
    def construct(self):
        text = Text("Introduction to Electric Fields!")
        self.play(Write(text))
        self.wait()
        self.clear()
#Narration to include
    #What Electric Fields are and How they work

class ElectricFields(Scene):
    def construct(self):
        title = Text("Electric Fields")
        title.to_edge(UP)
        self.play(Write(title))

        #Creating a Single Point Charge
        charge = Dot(color=RED).shift(LEFT*2)
        charge_label = Tex("Q").next_to(charge, RIGHT)

        #Create Electric Field Lines
        field_lines = VGroup()
        for angle in np.linspace(0, 2*PI, 8, endpoint=False):
            start = charge.get_center()
            end = start + 3 * np.array([np.cos(angle), np.sin(angle), 0 ])
            line = Arrow(start, end, buff=0, color=YELLOW_A)
            field_lines.add(line)
        
        self.play(Create(charge), Write(charge_label))
        self.play(Create(field_lines))

        #Narration Text
        explanation1 = Tex(
            r"An electric field is a region "
        )
        explanation2 = Tex(
            r"around a charged particle, "
        )
        explanation3 = Tex(
            r"where an electric force is "
        )
        explanation4 = Tex(
            r"exerted on other charges."
        )

        explanation = VGroup(explanation1, explanation2, explanation3, explanation4)
        explanation.arrange(DOWN).next_to(field_lines, RIGHT).scale(0.7)

        self.play(Write(explanation))

        self.wait(2)
        self.clear()

class ElectricFieldEquation(Scene):
    def construct(self):
        # Title
        title = Text("Electric Field Equation")
        title.to_edge(UP)
        self.play(Write(title))

        # Equation
        equation = MathTex("F = E \\cdot Q")
        equation.scale(1.5)
        self.play(Write(equation))
        self.wait(1)

        # Explanation of F
        explanation_F = Tex(
            r"Where $F$ is the force experienced by a charge "
        )
        explanation_F.next_to(equation, DOWN)
        self.play(Write(explanation_F))
        
        force_highlight = SurroundingRectangle(equation[0][0], color=YELLOW, buff=0.1)
        self.play(Create(force_highlight))
        self.wait(1)
        self.play(FadeOut(force_highlight))

        self.remove(explanation_F)  # Remove to make space for the next explanation

        # Explanation of E
        explanation_E = Tex(
            r"$E$ is the electric field strength"
        )
        explanation_E.next_to(equation, DOWN)
        self.play(Write(explanation_E))
        
        field_highlight = SurroundingRectangle(equation[0][2], color=GREEN, buff=0.1)
        self.play(Create(field_highlight))
        self.wait(1)
        self.play(FadeOut(field_highlight))

        self.remove(explanation_E)  # Remove to make space for the next explanation

        # Explanation of Q
        explanation_Q = Tex(
            r"and $Q$ is the charge of the particle."
        )
        explanation_Q.next_to(equation, DOWN)
        self.play(Write(explanation_Q))

        charge_highlight = SurroundingRectangle(equation[0][4], color=RED, buff=0.1)
        self.play(Create(charge_highlight))
        self.wait(1)
        self.play(FadeOut(charge_highlight))

        self.wait(2)
        self.clear()

class CoulombsLaw(Scene):
    def construct(self):
        # Title
        title = Text("Coulomb's Law and Electric Fields")
        title.to_edge(UP)
        self.play(Write(title))
        
        # Coulomb's Law Concept
        concept1 = Tex(
            r"Coulomb's Law describes the force between two point charges."
        )
        concept2 = Tex(
            r"It is given by the formula $F = k \frac{Q_1 Q_2}{r^2}$"
        )
        concept1.next_to(title, DOWN)
        concept2.next_to(concept1, DOWN)
        
        self.play(Write(concept1))
        self.wait(1)
        self.play(Write(concept2))
        self.wait(2)
        
        # Relationship to Electric Field
        electric_field_concept = Tex(
            r"The electric field $E$ is defined as the force per unit charge."
        )
        electric_field_concept.next_to(concept2, DOWN)
        
        self.play(Write(electric_field_concept))
        self.wait(1)
        
        electric_field_formula = MathTex("E = \\frac{F}{Q}")
        electric_field_formula.next_to(electric_field_concept, DOWN)
        self.play(Write(electric_field_formula))
        self.wait(1)
        
        combined_equation = MathTex("E = k \\frac{Q}{r^2}")
        combined_equation.next_to(electric_field_formula, DOWN)
        self.play(Write(combined_equation))
        self.wait(2)
        
        self.clear()


#End video to be produced - Run this on Manim sideview - Use Ctrl + ' and then press r to run
class video(Scene):
    def construct(self):
        scene1 = Introduction.construct(self)
        self.wait()
        scene2 = ElectricFields.construct(self)
        self.wait()
        scene3 = ElectricFieldEquation.construct(self)
        self.wait()
        scene4 = CoulombsLaw.construct(self)
        self.wait()
        scene5 = CoulombsLaw.construct(self)
        self.wait()