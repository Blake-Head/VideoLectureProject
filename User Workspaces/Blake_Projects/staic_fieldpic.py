from manim import *
import manim_physics as mp


class StaticFieldPic(Scene):
    def construct(self):
        # Create a grid of points
        grid = mp.Grid(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            stroke_color=GRAY,
            stroke_width=1,
        )

        # Create a charge
        charge = mp.Charge(
            pos=ORIGIN,
            charge=1,
        )

        # Add the grid, field, and charge to the scene
        self.add(grid,charge)
