from manim import *

class Momentum(Scene):
    def construct(self):

        rec1 = Rectangle(height=3, width=2, fill_opacity=0.2).shift(DOWN*.5)
        rec2 = Rectangle(height=2, width=3, fill_opacity=0.2).shift(DOWN*1+RIGHT*2.5)
        rec3 = Rectangle(height=4, width=1, fill_opacity=0.2).shift(RIGHT*4.5)
        layer1 = VGroup(rec1, rec2, rec3)
        layer1b = layer1.shift(RIGHT*7)
        layer2 = VGroup(layer1, layer1b)
        self.add(layer2)
        path = Line(start=[10,0,0], end=[-10,0,0])


        blue_sq = Square(side_length=2, color=BLUE, fill_opacity=0.6).shift(DOWN*1)
        self.add(blue_sq)
        ground = Line(start=[-10,-2,0], end=[10,-2,0])
        self.add(ground)
        mass_txt = Text("m", font_size=75).shift(DOWN*1)
        self.add(mass_txt)
        arr = Arrow(start=[.75,-1,0], end=[4,-1,0], color=GREEN)
        self.add(arr)
        vel_txt=Tex(r"$\vec{\mathrm{v}}$").move_to(arr.get_top()).scale(1.5).shift(UP*0.3)
        self.add(vel_txt)

        self.play(MoveAlongPath(layer2, path), function="linear", run_time=4)


from manim import *
import random

from manim import *
import random

class ParallaxBuildings(Scene):
    def construct(self):
        # Frame width for creating layers
        frame_width = config.frame_width

        # Helper function to create a row of buildings
        def create_buildings(num_buildings, height_range, y_offset):
            buildings = VGroup()
            x_start = -frame_width / 2
            for _ in range(num_buildings):
                # Random height and width for the building
                height = random.uniform(*height_range)
                width = random.uniform(2, 3)
                building = Rectangle(
                    width=width, height=height, color=WHITE, fill_opacity=.9
                ).align_to([x_start, y_offset, 0], LEFT)
                buildings.add(building)
                # Add some space between buildings
                x_start += width + random.uniform(4, 5)
            return buildings

        # Create foreground (layer 1) buildings
        layer1 = create_buildings(20, height_range=(1, 2), y_offset=-1)
        layer1_copy = layer1.copy().shift(RIGHT * frame_width)

        # Create background (layer 2) buildings
        layer2 = create_buildings(15, height_range=(0.5, 1.5), y_offset=-2)
        layer2_copy = layer2.copy().shift(RIGHT * frame_width)

        # Add layers to the scene
        self.add(layer2, layer2_copy, layer1, layer1_copy)

        # Calculate the time for one full loop
        loop_time = 10

        # Create animations for seamless looping
        layer1_anim = AnimationGroup(
            layer1.animate.shift(LEFT * frame_width),
            layer1_copy.animate.shift(LEFT * frame_width),
            lag_ratio=0,
            rate_func=linear
        )
        layer2_anim = AnimationGroup(
            layer2.animate.shift(LEFT * frame_width / 2),  # Slower speed for parallax
            layer2_copy.animate.shift(LEFT * frame_width / 2),
            lag_ratio=0,
            rate_func=linear
        )

        # Play the animations for one full loop
        self.play(layer1_anim, layer2_anim, run_time=loop_time, rate_func=linear)

        # Pause to hold the scene after animation
        self.wait()
