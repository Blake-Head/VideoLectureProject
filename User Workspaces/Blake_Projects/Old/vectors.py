from manim import *

class BoxInAPlane(Scene):
    def construct(self):
        box = Rectangle(stroke_color = GREEN_C, stroke_opacity = 0.7,
                        fill_color = RED_B, fill_opacity = 0.5, height = 1, width=1)
        
        plane = (
            NumberPlane(x_range=[-15,15,1], y_range=[-15,15,1])
            .add_coordinates()
        )

        dot = Dot(color=WHITE)
        
        # This will make the dot and box move as a single unit
        box_w_dot = VGroup(box, dot)
        
        self.add(box_w_dot, plane)
        self.play(box_w_dot.animate.shift(RIGHT*2), run_time =2)
        self.play(box_w_dot.animate.shift(UP*3), run_time = 2)
        self.play(box_w_dot.animate.shift(DOWN*5+LEFT*5), run_time =2)
        self.play(box_w_dot.animate.shift(UP*1.5+RIGHT*1), run_time=2)
        # This will slide the entire number plane without moving objects
        self.play(plane.animate.shift(RIGHT*2), run_time=2)
        self.play(box_w_dot.animate.shift(UP*0.5+RIGHT*4), run_time=2)
        self.play(plane.animate.shift(LEFT*2),box_w_dot.animate.shift(LEFT*2), run_time=2)


class Vectors(Scene):
    def construct(self):
        plane = (
            NumberPlane(x_range=[-15,15,1], y_range=[-15,15,1])
            .add_coordinates()
        )

        box = Rectangle(height=2.25, width=4, stroke_color = WHITE, fill_color = BLACK, fill_opacity = 1).move_to(DOWN*2+LEFT*3.5)
        box2 = box.copy().move_to(UP*2+LEFT*3.5)

        exp1 = Tex(r"{0.55\textwidth} Suppose we want to add two vectors."
                   r"The Yellow vector has an x-component of 1 unit and a y-component of 2 units."
                   r"The Red vector has an x-component of 4 units and a y-component of 1 unit.",
                   tex_environment="minipage").move_to(box2.get_center()).scale(.4)

        dot = Dot(color= PURE_GREEN).scale(1.5)

        text1 = Tex("Yellow then Red").move_to(box.get_top()).shift(DOWN*.35)
        text1_width = text1.width
        box_width = box.width
        text1.scale(text1_width / box_width)
        text2 = Tex("Red then Yellow").move_to(box.get_top()).shift(DOWN*.35)
        text2_width = text2.width
        text2.scale(text2_width / box_width)
        # Vector Components
        a1 = 1
        a2 = 2

        b1 = 4
        b2 = 1

        # Vectors
        vec1 = Vector(direction=[a1,a2], color = YELLOW)
        vec1_copy = vec1.copy()

        lab1 = vec1.coordinate_label(color = YELLOW).scale(.7)

        vec2 = Vector(direction=[b1,b2], color = RED)
        vec2_copy = vec2.copy()
        lab2 = vec2.coordinate_label(color = RED).scale(.7)

        vec3 = Vector(direction=[a1+b1,a2+b2], color = GREEN)
        lab3 = vec3.coordinate_label(color=GREEN).move_to(UP*1+RIGHT*3.5).scale(.7)

        eq1 = Matrix([{a1}, {a2}]).set_color(YELLOW)
        plussign = Tex("+")
        eq2 = Matrix([{b1}, {b2}]).set_color(RED)
        eqlsign = Tex("=")
        eq3 = Matrix([{a1+b1}, {a2+b2}]).set_color(GREEN)

        sol = VGroup(eq1, plussign, eq2, eqlsign, eq3).arrange(RIGHT).move_to(box.get_center()).shift(DOWN*.25)
        sol_width = sol.width
        sol.scale(sol_width/box_width * .7)

        # Animations
        self.add(plane, vec1, vec2, vec1_copy, box, box2)
        self.play(FadeIn(lab1, lab2))
        self.play(Write(exp1))

        self.play(Write(text1))
        self.play(FadeIn(sol[0:4]))
        self.wait(2)

        self.play(FadeOut(lab1, lab2, exp1))
        exp2 = Tex(r"{0.55\textwidth} We can imagine these vectors as a person walking along two paths."
                   r"The first path (yellow) takes the person up two units (maybe meters) "
                   r"while the second path (red) takes the person another 4 units to the left and 1 more up."
                   r"We can visualize this by sliding the red vector so that it begins just where the yellow path ends.",
            tex_environment="minipage").move_to(box2.get_center()).scale(.4)
        self.play(Write(exp2))
        self.wait(3)

        self.play(vec2.animate.shift(UP*2+RIGHT*1), run_time=2)
        self.play(FadeIn(dot))
        self.play(dot.animate.shift(UP*2+RIGHT*1))
        self.play(dot.animate.shift(UP*1+RIGHT*4))
        self.wait(3)

        self.play(FadeOut(exp2))
        exp3 = Tex(r"{0.55\textwidth} If we measure how far we now are from out starting point, "
                   r"we could draw another vector to represent that distance.  Here, it's a green arrow."
                   r"This green vector is called the `resultant'.",
            tex_environment="minipage").move_to(box2.get_center()).scale(.4)
       
        # Add resultant
        self.play(Write(exp3))
        self.wait(3)
        self.play(GrowArrow(vec3), run_time=2)
        self.wait(3)
       
       # Show green dot move up and down resultant 
        self.play(FadeOut(exp3))
        exp4 = Tex(r"{0.55\textwidth} Another way to think about the resultant is that it"
                   r"represents a path we COULD have taken to get to the exact same ending position. "
                   r"Sort of a `as-the-crow-flies' path.",
            tex_environment="minipage").move_to(box2.get_center()).scale(.4)

        self.play(Write(exp4))
        self.wait(3)
        self.play(dot.animate.shift(DOWN*3+LEFT*5), run_time=1.5)
        self.play(dot.animate.shift(UP*3+RIGHT*5), run_time=1.5)
        self.wait(3)

        self.play(FadeOut(exp4))
        exp5 = Tex(r"{0.55\textwidth} To actually calculate the value of the resultant, we "
                   r"can either add the numerical vectors together or, in this case, simply look "
                   r"at the picure.",
    tex_environment="minipage").move_to(box2.get_center()).scale(.4)
        
        self.play(Write(exp5))
        self.wait(3)
        linea = Vector(direction=[5,0], color=RED)
        lineb = Vector(direction=[0,3], color=RED).shift(RIGHT*5)
        linea_len = Tex("5", color=RED).next_to(linea, DOWN)
        lineb_len = Tex("3", color=RED).next_to(lineb, RIGHT)
        line_lens = VGroup(linea_len, lineb_len)
        self.play(FadeIn(linea, lineb), run_time=2)
        self.play(FadeIn(line_lens), run_time = 2)
        self.play(Transform(line_lens, lab3), FadeOut(linea, lineb))
        self.play(FadeIn(sol[4]))
        self.wait(3)

        self.play(FadeOut(line_lens, exp5))

        self.play(vec1.animate.shift(RIGHT*4+UP*1), FadeIn(vec2_copy), run_time=2)
        exp6 = Tex(r"{0.55\textwidth} In fact, we could have first traveled along the red path "
                   r"and THEN take the yellow path.  In the end, we end up at the same place."
                   r" In vector speak, we say that vector addition is `commutative'",
    tex_environment="minipage").move_to(box2.get_center()).scale(.4)
        self.play(Write(exp6))
        self.wait(3)
        sol2 = VGroup(eq2, plussign, eq1, eqlsign, eq3).arrange(RIGHT).move_to(box.get_center()).shift(DOWN*.25)
        sol2_width = sol2.width
        sol2.scale(sol2_width/box_width)
        self.play(Transform(text1, text2), Transform(sol, sol2))
        self.play(dot.animate.shift(DOWN*3+LEFT*5), run_time=1.5)
        self.play(dot.animate.shift(UP*1+RIGHT*4))
        self.play(dot.animate.shift(UP*2+RIGHT*1))
        self.wait(3)
        self.play(FadeOut(text2, sol2, vec1, dot, vec3, vec2, text1, exp6))
