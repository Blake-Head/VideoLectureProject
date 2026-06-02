from manim import *
import random
import numpy as np
from scipy.spatial import Delaunay

class BackgroundTestingStatic_GPT(Scene):
    def construct(self):
        # Set number of random points
        num_points = random.randint(50, 50)  # You can change this range as needed

        # Define the four corners of the scene
        corners = [
            np.array([-config.frame_width / 2, -config.frame_height / 2, 0]),
            np.array([config.frame_width / 2, -config.frame_height / 2, 0]),
            np.array([-config.frame_width / 2, config.frame_height / 2, 0]),
            np.array([config.frame_width / 2, config.frame_height / 2, 0])
        ]

        # Generate random points with smaller size, spread across the entire scene
        points = [
            Dot(
                point=np.array([
                    random.uniform(-config.frame_width / 2, config.frame_width / 2),
                    random.uniform(-config.frame_height / 2, config.frame_height / 2),
                    0
                ]),
                radius=0.1,
                color=GOLD
            )
            for _ in range(num_points)
        ]

        # Add the corner points as dots
        corner_dots = [Dot(point=corner, radius=0.03, color=RED) for corner in corners]
        points.extend(corner_dots)

        self.add(*points)

        # Extract point coordinates (add z=0 to ensure 3D points)
        point_coords = np.array([point.get_center()[:2] + [0] for point in points])  # Ensure z=0

        # Perform Delaunay triangulation
        tri = Delaunay(point_coords[:, :2])

        # Draw filled triangles based on Delaunay triangulation
        triangles = []
        for simplex in tri.simplices:
            p1, p2, p3 = [point_coords[i] for i in simplex]
            triangle = Polygon(
                p1, p2, p3,
                fill_opacity=0.4,  # Adjust the opacity of the fill
                stroke_color=DARK_BLUE,  # Color of the border
                stroke_width=2
            )
            # Apply a gradient fill (You can adjust colors as needed)
            triangle.set_fill(gradient=BLUE, color=BLUE_D)
            triangles.append(triangle)

        triangles_group = VGroup(*triangles)
        self.add(triangles_group)

class background_testing_static(Scene):
    def construct(self):
        # Set number of random points
        num_points = random.randint(5000, 5000)  # You can change this range as needed

        # Define the four corners of the scene
        corners = [
            np.array([-config.frame_width / 2, -config.frame_height / 2, 0]),
            np.array([config.frame_width / 2, -config.frame_height / 2, 0]),
            np.array([-config.frame_width / 2, config.frame_height / 2, 0]),
            np.array([config.frame_width / 2, config.frame_height / 2, 0])
        ]

        # Generate random points with smaller size, spread across the entire scene
        points = [
            Dot(
                point=np.array([
                    random.uniform(-config.frame_width / 2, config.frame_width / 2),
                    random.uniform(-config.frame_height / 2, config.frame_height / 2),
                    0
                ]),
                radius=0.0000001,
                color=BLACK
            )
            for _ in range(num_points)
        ]

        # Add the corner points as dots
        corner_dots = [Dot(point=corner, radius=0.03) for corner in corners]
        points.extend(corner_dots)

        #self.add(*points)

        # Extract point coordinates
        point_coords = np.array([point.get_center()[:2] for point in points])  # Extract only x and y

        # Perform Delaunay triangulation
        tri = Delaunay(point_coords)

        # Draw lines based on Delaunay triangulation
        stwdt = 2
        opat = 0.1
        clr1 = DARK_BLUE
        clr2 = DARK_BLUE
        clr3 = DARK_BLUE
        lines = []
        for simplex in tri.simplices:
            p1, p2, p3 = simplex
            lines.append(Line(points[p1].get_center(), points[p2].get_center(), stroke_width = stwdt, color=clr1).set_opacity(opat))
            lines.append(Line(points[p2].get_center(), points[p3].get_center(), stroke_width = stwdt, color=clr2).set_opacity(opat))
            lines.append(Line(points[p3].get_center(), points[p1].get_center(), stroke_width = stwdt, color=clr3).set_opacity(opat))

        unique_lines = list(set(lines))
        lines_group = VGroup(*unique_lines)
        self.add(lines_group)

        self.play(lines_group.animate.set_color(BLUE))
        self.play(lines_group.animate.set_color(DARK_BLUE))

class background_testing_animated(Scene):
    def construct(self):
        # Set number of random points
        num_points = random.randint(20, 20)  # You can change this range as needed

        # Define the four corners of the scene
        corners = [
            np.array([-config.frame_width / 2, -config.frame_height / 2, 0]),
            np.array([config.frame_width / 2, -config.frame_height / 2, 0]),
            np.array([-config.frame_width / 2, config.frame_height / 2, 0]),
            np.array([config.frame_width / 2, config.frame_height / 2, 0])
        ]

        # Generate random points with smaller size, spread across the entire scene
        points = [
            Dot(
                point=np.array([
                    random.uniform(-config.frame_width / 2, config.frame_width / 2),
                    random.uniform(-config.frame_height / 2, config.frame_height / 2),
                    0
                ]),
                radius=0.01,
                color=BLACK
            )
            for _ in range(num_points)
        ]

        # Add the corner points as dots
        corner_dots = [Dot(point=corner, radius=0.03) for corner in corners]
        points.extend(corner_dots)

        #self.add(*points)

        # Extract point coordinates
        point_coords = np.array([point.get_center()[:2] for point in points])  # Extract only x and y

        # Perform Delaunay triangulation
        tri = Delaunay(point_coords)

        # Draw lines based on Delaunay triangulation
        stwdt = 3
        clr1 = DARK_BLUE
        clr2 = DARK_BLUE
        clr3 = DARK_BLUE
        lines = []
        #for simplex in tri.simplices:
            #p1, p2, p3 = simplex
            #lines.append(Line(points[p1].get_center(), points[p2].get_center(), stroke_width = 0, color=BLACK))
            #lines.append(Line(points[p2].get_center(), points[p3].get_center(), stroke_width = 0, color=BLACK))
            #lines.append(Line(points[p3].get_center(), points[p1].get_center(), stroke_width = 0, color=BLACK))

        for simplex in tri.simplices:
            p1, p2, p3 = simplex
            lines.append(Line(points[p1].get_center(), points[p2].get_center(), stroke_width = 0, color=DARK_BLUE))
            lines.append(Line(points[p2].get_center(), points[p3].get_center(), stroke_width = 0, color=BLACK))
            lines.append(Line(points[p3].get_center(), points[p1].get_center(), stroke_width = 0, color=BLACK))

        unique_lines = list(set(lines))
        lines_group = VGroup(*unique_lines)
        #self.add(lines_group)

        # Function to update the position of points and lines
        def update_points_and_lines(mob, dt):
            # Update points positions
            for point in points:
                if point not in corner_dots:  # Don't move corner points
                    new_x = point.get_center()[0] + random.uniform(-0.02, 0.02)
                    new_y = point.get_center()[1] + random.uniform(-0.02, 0.02)
                    point.move_to([new_x, new_y, 0])


            # Extract updated coordinates
            updated_coords = np.array([point.get_center()[:2] for point in points])

            # Recompute Delaunay triangulation
            tri = Delaunay(updated_coords)

            mob.submobjects = []

            stwdt = 3
            clr = DARK_BLUE

            new_lines = []
            for simplex in tri.simplices:
                p1, p2, p3 = simplex
                new_lines.append(Line(points[p1].get_center(), points[p2].get_center(), stroke_width = stwdt, color=clr))
                new_lines.append(Line(points[p2].get_center(), points[p3].get_center(), stroke_width = stwdt, color=clr))
                new_lines.append(Line(points[p3].get_center(), points[p1].get_center(), stroke_width = stwdt, color=clr))

            unique_new_lines = list(set(new_lines))
            mob.add(*unique_new_lines)

        # Create an updater for the lines
        lines_group.add_updater(update_points_and_lines)
        self.add(lines_group)

        # Keep the animation on screen for a while
        self.wait(5)