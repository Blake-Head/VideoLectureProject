from manim import *

class Units(Scene):
    def construct(self):
        #Text.set_default(font="Arial", font_size=50)

        video_title = Tex("Units in Physics").to_edge(UP)

        self.play(Write(video_title))
        
        # Intro Section, stating WHAT units are, what are the SI units, which 
        # ones we will be using
        all_si = Tex("kg, ", "m, ", "s", ", mol, ", "A, ", "K, ", "cd")

        self.play(Write(all_si))
        self.wait(2)
        #self.play(Unwrite(all_si[3:7]))
        self.play(Wiggle(all_si[0:3]), run_time = 4)

        imp_si = Tex("kg, m, s")

        self.play(Transform(all_si, imp_si))
        self.wait(2)
        self.play(FadeOut(all_si), FadeOut(video_title))
        self.wait(2)

        # Kilogram 

        table1 = Table(
            [["Kilogram", "kg", "Mass"],
             ["Meter", "m", "Length"],
             ["Second", "s", "Time"]],
             col_labels=[Text("Unit Name"), Text("Symbol"), Text("Measures")]
        )

        self.play(FadeIn(table1))
        self.wait(3)

        cell = table1.get_cell((2,1))
        cell_width = cell.get_width()
        cell_height = cell.get_height()
        box = Rectangle(height=cell_height, width=cell_width, stroke_color = GREEN, fill_color = GREEN, fill_opacity = .3).move_to(table1.get_cell((2,1)))
        self.play(FadeIn(box))

        cell = table1.get_cell((2,2))
        cell_width = cell.get_width()
        cell_height = cell.get_height()
        box1 = Rectangle(height=cell_height, width=cell_width, stroke_color = GREEN, fill_color = GREEN, fill_opacity = .3).move_to(table1.get_cell((2,2)))
        self.play(Transform(box, box1))

        cell = table1.get_cell((2,3))
        cell_width = cell.get_width()
        cell_height = cell.get_height()
        box2 = Rectangle(height=cell_height, width=cell_width, stroke_color = GREEN, fill_color = GREEN, fill_opacity = .3).move_to(table1.get_cell((2,3)))
        self.play(Transform(box, box2))

        # Meter

        cell = table1.get_cell((3,1))
        cell_width = cell.get_width()
        cell_height = cell.get_height()
        box3 = Rectangle(height=cell_height, width=cell_width, stroke_color = GREEN, fill_color = GREEN, fill_opacity = .3).move_to(table1.get_cell((3,1)))
        self.play(Transform(box, box3))

        cell = table1.get_cell((3,2))
        cell_width = cell.get_width()
        cell_height = cell.get_height()
        box4 = Rectangle(height=cell_height, width=cell_width, stroke_color = GREEN, fill_color = GREEN, fill_opacity = .3).move_to(table1.get_cell((3,2)))
        self.play(Transform(box, box4))

        cell = table1.get_cell((3,3))
        cell_width = cell.get_width()
        cell_height = cell.get_height()
        box5 = Rectangle(height=cell_height, width=cell_width, stroke_color = GREEN, fill_color = GREEN, fill_opacity = .3).move_to(table1.get_cell((3,3)))
        self.play(Transform(box, box5))

        # Seconds

        cell = table1.get_cell((4,1))
        cell_width = cell.get_width()
        cell_height = cell.get_height()
        box6 = Rectangle(height=cell_height, width=cell_width, stroke_color = GREEN, fill_color = GREEN, fill_opacity = .3).move_to(table1.get_cell((4,1)))
        self.play(Transform(box, box6))

        cell = table1.get_cell((4,2))
        cell_width = cell.get_width()
        cell_height = cell.get_height()
        box7 = Rectangle(height=cell_height, width=cell_width, stroke_color = GREEN, fill_color = GREEN, fill_opacity = .3).move_to(table1.get_cell((4,2)))
        self.play(Transform(box, box7))

        cell = table1.get_cell((4,3))
        cell_width = cell.get_width()
        cell_height = cell.get_height()
        box8 = Rectangle(height=cell_height, width=cell_width, stroke_color = GREEN, fill_color = GREEN, fill_opacity = .3).move_to(table1.get_cell((4,3)))
        self.play(Transform(box, box8))

        self.play(FadeOut(table1, box))


        # Manipulating Units 
        velocity = MathTex(r"v", "=", r"\frac{distance}{time}", font_size = 105)

        self.play(FadeIn(velocity[0]))
        self.wait(1)
        self.play(FadeIn(velocity[1:3]))

        velocity2 = MathTex(r"[", "v", r"]", "=", r"\frac{m}{s}", font_size = 105)
        #velocity2 = MathTex(r"[v]=\frac{m}{s}", font_size = 105)


        self.play(Transform(velocity, velocity2))
        self.remove(velocity)
        self.add(velocity2)

        arrow1 = Arrow(start = velocity2[0].get_corner(DL) + DOWN + LEFT, end = velocity2[0].get_corner(DL), color = GREEN)
        arrowlabel = Text("The brackets mean `The units of v are... ''", color=GREEN).next_to(arrow1, DOWN).scale(0.5)

        self.play(GrowArrow(arrow1), Write(arrowlabel))
        self.play(Indicate(velocity2[0], color=GREEN), Indicate(velocity2[2], color=GREEN))

        self.play(FadeOut(arrow1, arrowlabel))

        velocity3 = MathTex(r"[v] = \frac{km}{hr} = \frac{miles}{hr} = \ldots", font_size = 105)

        self.play(Transform(velocity2, velocity3))

        self.play(FadeOut(velocity2))


        # Momentum

        momentum = MathTex(r"p = mass \cdot velocity", font_size = 105)

        self.play(FadeIn(momentum))

        momentun2 = MathTex(r"[p] = kg \cdot velocity", font_size = 105)

        self.play(Transform(momentum, momentun2))

        self.remove(momentum)
        self.add(momentun2)

        momentum3 = MathTex(r"[p] = kg \frac{m}{s}", font_size = 105)

        self.play(Transform(momentun2, momentum3))

        momentum4 = MathTex(r"[p] = \frac{kg \ m}{s}", font_size = 105)

        self.play(Transform(momentun2, momentum4))

        self.play(FadeOut(momentun2))

        # Newton's Law

        newton = MathTex(r"F =", r"ma", font_size = 105)

        self.play(FadeIn(newton))

        newton2 = MathTex(r"[F] =", r"kg \ a", font_size = 105)

        self.play(Transform(newton, newton2))

        newton3 = MathTex(r"[F] =", r"kg \frac{m}{s^2}", font_size = 105)

        self.play(Transform(newton, newton3))

        newton4 = MathTex(r"[F]=", r"\frac{kg \ m}{s^2}", font_size = 105)
        
        self.play(Transform(newton, newton4))
        self.remove(newton)
        self.add(newton4)

        self.play(Indicate(newton4[1], color=YELLOW))

        circ = Circle(radius=1.75, color=YELLOW).move_to(newton4[1].get_center())
        circlabel = Text("This specific collection of\nunits is called the Newton!", color=YELLOW).next_to(circ, DOWN).scale(0.6)

        self.play(DrawBorderThenFill(circ))
        self.play(Write(circlabel))

        self.wait(2)

        self.play(FadeOut(circ, circlabel))

        nunit = MathTex(r"\equiv N", font_size = 105).next_to(newton4, RIGHT)

        all_together = VGroup(newton4, nunit)

        self.play(FadeIn(nunit), all_together.animate.move_to(ORIGIN))

        self.play(FadeOut(all_together))


        # Dim Analysis

        units1 = MathTex(r"\frac{kg \ m }{s^2}", "s", font_size = 105)

        self.play(Write(units1))
        self.play(Indicate(units1[0]))

        units2 = MathTex(r"N", "s", font_size = 105)

        self.play(Transform(units1, units2))
        self.remove(units1)
        self.add(units2)

        units3 = MathTex(r"\frac{kg \ m }{s^2}", "s", font_size = 105)

        self.play(Transform(units2, units3))
        self.remove(units2)
        self.add(units3)

        line1 = Line(start=DOWN+LEFT, end=UP+RIGHT, color=RED).scale(0.3).move_to(RIGHT*1.3+DOWN*0.1)
        line2 = Line(start=DOWN+LEFT, end=UP+RIGHT, color=RED).scale(0.3).move_to(DOWN*.5)
        self.play(GrowFromCenter(line1), GrowFromCenter(line2))

        units4 = MathTex(r"\frac{kg \ m}{s}", font_size=105)

        self.play(Transform(units3, units4), FadeOut(line1, line2))

        self.remove(units3)
        self.add(units4)

        momentum = MathTex(r"= [p]", font_size = 105).next_to(units4, RIGHT)

        momtogether = VGroup(units4, momentum)

        self.play(FadeIn(momentum), momtogether.animate.move_to(ORIGIN))

        otherunit = MathTex(r" = Ns", font_size = 105).next_to(momtogether, RIGHT)
        momtogether2 = VGroup(momtogether, otherunit)

        self.play(FadeIn(otherunit), momtogether2.animate.move_to(ORIGIN))

        self.play(FadeOut(momtogether2))


        # Kinematics

        kine = MathTex(r"x_f", "=", r"x_i", "+", r"v_o t", "+", r"\frac{1}{2}a t^2", font_size = 105)

        self.play(Write(kine))

        check1 = MathTex(r"[x_f] = m", font_size = 105, color = GREEN).next_to(kine, DOWN)

        self.play(FadeIn(check1), kine[0].animate.set_color(GREEN))
        self.play(FadeOut(check1), kine[0].animate.set_color(WHITE))

        check2 = MathTex(r"[x_i] = m", font_size = 105, color = GREEN).next_to(kine, DOWN)

        self.play(FadeIn(check2), kine[2].animate.set_color(GREEN))
        self.play(FadeOut(check2), kine[2].animate.set_color(WHITE))

        check3 = MathTex(r"[v_o t] = \frac{m}{s}s", font_size=105, color = GREEN).next_to(kine, DOWN)
        check3_1 = MathTex(r"[v_o t] = m", font_size=105, color = GREEN).next_to(kine, DOWN)
        self.play(FadeIn(check3), kine[4].animate.set_color(GREEN))
        self.play(Transform(check3, check3_1))
        self.play(FadeOut(check3), kine[4].animate.set_color(WHITE))

        check4 = MathTex(r"[\frac{1}{2}at^2] = \frac{m}{s^2} s^2", font_size=105, color = GREEN).next_to(kine, DOWN)
        check4_1 = MathTex(r"[at^2] = \frac{m}{s^2} s^2", font_size=105, color = GREEN).next_to(kine, DOWN)
        check4_2 = MathTex(r"[at^2] = m", font_size=105, color = GREEN).next_to(kine, DOWN)

        self.play(FadeIn(check4), kine[6].animate.set_color(GREEN))
        self.play(Transform(check4, check4_1))
        self.play(Transform(check4, check4_2))
        self.play(FadeOut(check4), kine[6].animate.set_color(WHITE))

        finalcheck = MathTex(r"m = m + m + m", font_size=105, color = GREEN).next_to(kine, DOWN)
        self.play(FadeIn(finalcheck))
        self.play(FadeOut(finalcheck))

        kine2 = MathTex(r"x_f", "=", r"x_i", "+", r"v_o t", "+", r"\frac{1}{2}a t", font_size = 105).shift(LEFT*.2)

        self.add(kine2)
        self.play(FadeIn(kine2), FadeOut(kine))
        self.remove(kine)

        badcheck = MathTex(r"m =", "m", "+ m", r"+ \frac{m}{s}", font_size = 90, color = GREEN).next_to(kine2, DOWN, buff=0.75)

        self.play(FadeIn(badcheck[0]), kine2[0].animate.set_color(GREEN))
        self.play(FadeIn(badcheck[1]), kine2[2].animate.set_color(GREEN))
        self.play(FadeIn(badcheck[2]), kine2[4].animate.set_color(GREEN))
        self.play(FadeIn(badcheck[3]), kine2[6].animate.set_color(RED), badcheck[3].animate.set_color(RED))

        addtime = MathTex("t", font_size = 105).next_to(kine2, RIGHT)
        adds = MathTex("s", font_size=90).next_to(badcheck, RIGHT)

        self.play(GrowFromCenter(addtime), GrowFromCenter(adds))

        newterm = MathTex(r"\frac{1}{2}at^2", font_size = 105).move_to(kine2[6].get_center())
        newterm_m = MathTex(r"+ \ m", font_size = 90).move_to(badcheck[3].get_center())

        self.play(Transform(kine2[6], newterm), 
                  FadeOut(addtime, adds), 
                  Transform(badcheck[3], newterm_m))


        self.play(newterm.animate.set_color(GREEN), newterm_m.animate.set_color(GREEN))

        self.play(FadeOut(kine2, badcheck, newterm, newterm_m))


        self.wait(2)
