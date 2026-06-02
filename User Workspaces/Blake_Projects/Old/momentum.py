from manim import *

class Sliding_Block_GPT(Scene):
    def construct(self):
        # Define the big square
        big_sq = (
            Square(
                side_length=2.5,
                fill_color=BLUE,
                fill_opacity=0.3)
                .to_corner(DL)
        )
        # Define the small square
        small_sq = (
            Square(
                side_length=1,
                fill_color=GREEN,
                fill_opacity=0.3)
                .to_edge(DOWN)
        )
        # Title at top of screen
        title = Tex("Which vector describes the velocity of the small block after collision?").to_edge(UP)
        title.scale(0.9)

        # Text for masses
        big_text = Tex("$m_1$=2kg")
        small_text = Tex("$m_2$= 1kg")

        # Scale the big text to match the width of the big square
        big_text_width = big_text.width
        big_square_width = big_sq.width
        big_text.scale(big_square_width / big_text_width)
        # Position the big text above the big square
        big_text.next_to(big_sq, UP, buff=0.2)


        # Scale the small text to match the width of the small square
        small_text_width = small_text.width
        small_square_width = small_sq.width
        small_text.scale(small_square_width / small_text_width)
        # Position the small text above the small square
        small_text.next_to(small_sq, UP, buff=0.1)

        # Create a vector group for shapes and text so that they move together
        text_square_big = VGroup(big_sq, big_text)
        text_square_small = VGroup(small_sq, small_text)

        # Create arrows
        arrow_up = Arrow(start=DOWN, end=UP, color=RED)
        arrow_down = Arrow(start=UP, end=DOWN, color=RED)
        arrow_left = Arrow(start=RIGHT, end=LEFT, color=RED)
        arrow_right = Arrow(start=LEFT, end=RIGHT, color=RED)

        arrows = VGroup(arrow_up, arrow_down, arrow_left, arrow_right).arrange(RIGHT, buff=2)
        arrows.next_to(title, DOWN, buff=0.5)

        # Create circle around arrow_right
        circle = Circle(radius=1, color=YELLOW, stroke_width=4).move_to(arrow_right.get_center())

        self.play(Write(title))

        self.play(FadeIn(text_square_big), run_time=1)
        self.play(FadeIn(text_square_small), run_time=1)

        self.play(Create(arrows), run_time = 3)

        # Calculate the horizontal distance the big square needs to move to hit the small square
        distance_to_move = small_sq.get_left()[0] - big_sq.get_right()[0]

        # Start moving big square
        self.play(text_square_big.animate.shift(RIGHT * distance_to_move), run_time=2, rate_func = linear)

        # Collision happens here
        self.play(text_square_big.animate.shift(RIGHT * distance_to_move*0.5), text_square_small.animate.shift(RIGHT * distance_to_move*2), run_time=2, rate_func = linear)
        self.play(text_square_big.animate.shift(RIGHT * distance_to_move*0.5), text_square_small.animate.shift(RIGHT * distance_to_move*2), run_time=2, rate_func = linear)
        self.play(text_square_big.animate.shift(RIGHT * distance_to_move*0.5), Create(circle), run_time=2, rate_func = linear)
        self.play(text_square_big.animate.shift(RIGHT * distance_to_move*0.5), run_time=2, rate_func = linear)
        self.play(text_square_big.animate.shift(RIGHT * distance_to_move*0.5), run_time=2, rate_func = linear)
        self.play(text_square_big.animate.shift(RIGHT * distance_to_move*0.5), run_time=2, rate_func = linear)
        self.play(text_square_big.animate.shift(RIGHT * distance_to_move*0.5), run_time=2, rate_func = linear)





        self.wait(2)

class Momentum_Transfer(Scene):
    def construct(self):

                # Define the big square
        big_sq = (
            Square(
                side_length=3,
                fill_color=BLUE,
                fill_opacity=0.4)
                .to_edge(LEFT, buff = 3)
        )
        # Define the small square
        small_sq = (
            Square(
                side_length=3,
                fill_color=GREEN,
                fill_opacity=0.4)
                .to_edge(RIGHT, buff = 3)
        )
               
        # Arrow for showing positive x-direction
        arrow_right = Arrow(start=LEFT, end=RIGHT, color=RED, buff=0.5).to_corner(UL)
        x_dirc = Tex("+x").next_to(arrow_right, DOWN, buff=0.1).scale(0.7)

        # Text for masses
        big_text = Tex("$m_1$ = $2$ kg")
        small_text = Tex("$m_2$ = $1$ kg")
        big_vel = Tex("$\\vec{v}_1$ = $2$ $\\frac{\\text{m}}{\\text{s}}$ $\\hat{x}$")
        small_vel = Tex("$\\vec{v}_2$ = $0$ $\\frac{\\text{m}}{\\text{s}}$")

        # Scale the big text to match the width of the big square
        big_text_width = big_text.width
        big_square_width = big_sq.width
        big_text.scale(big_square_width / big_text_width)
        big_vel.scale(big_square_width/big_text_width)
        # Position the big text above the big square
        big_text.next_to(big_sq, UP, buff=0.2)
        big_vel.next_to(big_text, UP, buff=0.2)


        # Scale the small text to match the width of the small square
        small_text_width = small_text.width
        small_square_width = small_sq.width
        small_text.scale(small_square_width / small_text_width)
        small_vel.scale(small_square_width/small_text_width)
        # Position the small text above the small square
        small_text.next_to(small_sq, UP, buff=0.2)
        small_text.next_to(small_sq, UP, buff=0.2)
        small_vel.next_to(small_text, UP, buff=0.2)

        # Create a vector group for shapes and text so that they move together
        text_square_big = VGroup(big_sq, big_text, big_vel)
        text_square_small = VGroup(small_sq, small_text, small_vel)

        mom = MathTex("\\vec{p} = m\\vec{v}").to_edge(DOWN, buff = 1).scale(2)
        mom2 = MathTex("\\vec{p} = ","m_1 \\vec{v}_1", "+", "m_2 \\vec{v}_2").to_edge(DOWN, buff = 1).scale(2)
        mom3 = MathTex("\\vec{p} = ","m_1 \\vec{v}_1", "+", "m_2 \\ 0 \\frac{\\text{m}}{\\text{s}}").to_edge(DOWN, buff = 1).scale(2)
        mom4 = MathTex("\\vec{p} = ","m_1 \\vec{v}_1").to_edge(DOWN, buff = 1).scale(2)
        blue_mom = MathTex("\\vec{p} = (2 kg)(2 \\frac{m}{s} \\hat{x})").to_edge(DOWN, buff = .9).scale(2)
        blue_mom_val = MathTex("\\vec{p} = 4 \\frac{kg \ m}{s} \\hat{x}").to_edge(DOWN, buff = .9).scale(2)
        blue_mom_val2 = MathTex("\\vec{p} = 4 \ \\text{Ns} \ \\hat{x}").to_edge(DOWN, buff = .9).scale(2)

        # Draw the Squares and text to screen, as well as p=mv equation
        self.play(FadeIn(text_square_big, text_square_small, mom, arrow_right, x_dirc))
        self.wait(1)
        # Transform general p=mv into total system momentum
        self.play(Transform(mom, mom2))
        self.wait(1)
        # Change color of each term for each square
        self.play(mom[1].animate.set_color(BLUE), mom[3].animate.set_color(GREEN))
        self.wait(3)
        # Transform general p=mv into total system momentum
        self.play(Transform(mom, mom3))
        self.wait(1)
       # Transform general p=mv into total system momentum
        self.play(Transform(mom, mom4))
        self.wait(1)
        # Shift
        self.play(Transform(mom, blue_mom))
        self.wait(1)
        
        self.play(Transform(mom, blue_mom_val))
        self.wait(1)
        
        self.play(Transform(mom, blue_mom_val2)) 
        self.wait(1)

        self.play(mom.animate.scale(.5), run_time=1)
        self.play(mom.animate.move_to(big_sq.get_center()), run_time = 2)

        self.wait(3)
