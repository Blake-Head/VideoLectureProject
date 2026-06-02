from manim import *
import random
import numpy as np
from scipy.spatial import Delaunay



class AnimatedTriangularMesh(Scene):
    def construct(self):
        # Set number of random points
        num_points = random.randint(5, 10)  # You can change this range as needed

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
                radius=0.03
            )
            for _ in range(num_points)
        ]

        # Add the corner points as dots
        corner_dots = [Dot(point=corner, radius=0.03) for corner in corners]
        points.extend(corner_dots)

        # Add points to the scene
        self.add(*points)

        # Function to update the position of points and lines
        def update_points_and_lines(mob, dt):
            # Update points positions
            for point in points:
                if point not in corner_dots:  # Don't move corner points
                    new_x = point.get_center()[0] + random.uniform(-0.01, 0.01)
                    new_y = point.get_center()[1] + random.uniform(-0.01, 0.01)
                    point.move_to([new_x, new_y, 0])

            # Extract updated coordinates
            updated_coords = np.array([point.get_center()[:2] for point in points])

            # Recompute Delaunay triangulation
            tri = Delaunay(updated_coords)

            # Remove old lines
            self.remove(*mob.submobjects)

            # Create new lines
            new_lines = []
            for simplex in tri.simplices:
                p1, p2, p3 = simplex
                new_lines.append(Line(points[p1].get_center(), points[p2].get_center()))
                new_lines.append(Line(points[p2].get_center(), points[p3].get_center()))
                new_lines.append(Line(points[p3].get_center(), points[p1].get_center()))

            unique_new_lines = list(set(new_lines))
            mob.add(*unique_new_lines)

        # Extract point coordinates
        point_coords = np.array([point.get_center()[:2] for point in points])  # Extract only x and y

        # Perform Delaunay triangulation
        tri = Delaunay(point_coords)

        # Draw initial lines based on Delaunay triangulation
        lines = []
        for simplex in tri.simplices:
            p1, p2, p3 = simplex
            lines.append(Line(points[p1].get_center(), points[p2].get_center()))
            lines.append(Line(points[p2].get_center(), points[p3].get_center()))
            lines.append(Line(points[p3].get_center(), points[p1].get_center()))

        lines_group = VGroup(*lines)
        self.add(lines_group)

        # Create an updater for the lines
        lines_group.add_updater(update_points_and_lines)

        # Keep the animation on screen for a while
        self.wait(10)

class AnimatedTriangularMesh_SAVED_v1(Scene):
    def construct(self):
        # Set number of random points
        num_points = random.randint(25, 35)  # You can change this range as needed

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
                radius=0.03,
            )
            for _ in range(num_points)
        ]

        # Add the corner points as dots
        corner_dots = [Dot(point=corner, radius=0.03) for corner in corners]
        points.extend(corner_dots)

        # Add points to the scene
        self.add(*points)

        # Extract point coordinates
        point_coords = np.array([point.get_center()[:2] for point in points])  # Extract only x and y

        # Perform Delaunay triangulation
        tri = Delaunay(point_coords)

        # Draw lines based on Delaunay triangulation
        lines = []
        for simplex in tri.simplices:
            p1, p2, p3 = simplex
            lines.append(Line(points[p1].get_center(), points[p2].get_center()))
            lines.append(Line(points[p2].get_center(), points[p3].get_center()))
            lines.append(Line(points[p3].get_center(), points[p1].get_center()))

        unique_lines = list(set(lines))
        lines_group = VGroup(*unique_lines)
        self.add(lines_group)

        # Function to update the position of points and lines
        def update_points_and_lines(mob, dt):
            # Update points positions
            for point in points:
                if point not in corner_dots:  # Don't move corner points
                    new_x = point.get_center()[0] + random.uniform(-0.01, 0.01)
                    new_y = point.get_center()[1] + random.uniform(-0.01, 0.01)
                    point.move_to([new_x, new_y, 0])

            # Extract updated coordinates
            updated_coords = np.array([point.get_center()[:2] for point in points])

            # Recompute Delaunay triangulation
            tri = Delaunay(updated_coords)

            # Clear and redraw lines
            mob.submobjects = []
            #self.remove(*points, *lines)

            new_lines = []
            for simplex in tri.simplices:
                p1, p2, p3 = simplex
                new_lines.append(Line(points[p1].get_center(), points[p2].get_center()))
                new_lines.append(Line(points[p2].get_center(), points[p3].get_center()))
                new_lines.append(Line(points[p3].get_center(), points[p1].get_center()))

            unique_new_lines = list(set(new_lines))
            mob.add(*unique_new_lines)

        # Create an updater for the lines
        lines_group.add_updater(update_points_and_lines)
        self.add(lines_group)

        # Keep the animation on screen for a while
        self.wait(10)

class TriangularMesh_SAVED_v2(Scene):
    def construct(self):
        # Set number of random points
        num_points = random.randint(30, 35)  # You can change this range as needed

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
                radius=0.075
            )
            for _ in range(num_points)
        ]

        # Add the corner points as dots
        corner_dots = [Dot(point=corner, radius=0.075) for corner in corners]
        points.extend(corner_dots)

        # Add points to the scene
        self.play(*[Create(point) for point in points])

        # Extract point coordinates
        point_coords = np.array([point.get_center()[:2] for point in points])  # Extract only x and y

        # Perform Delaunay triangulation
        tri = Delaunay(point_coords)

        # Draw lines based on Delaunay triangulation
        lines = []
        for simplex in tri.simplices:
            p1, p2, p3 = simplex
            lines.append(Line(points[p1].get_center(), points[p2].get_center()))
            lines.append(Line(points[p2].get_center(), points[p3].get_center()))
            lines.append(Line(points[p3].get_center(), points[p1].get_center()))

        # Remove duplicate lines
        unique_lines = list(set(lines))

        # Draw connections
        self.play(*[Create(line) for line in unique_lines])

        # Keep the animation on screen for a while
        self.wait(2)

class TriangularMesh_SAVED_v1(Scene):
    def construct(self):
        # Set number of points
        num_points = random.randint(20, 30)  # You can change this range as needed

        # Generate random points with smaller size, spread across the entire scene
        points = [
            Dot(
                point=np.array([
                    random.uniform(-config.frame_width / 2, config.frame_width / 2),
                    random.uniform(-config.frame_height / 2, config.frame_height / 2),
                    0
                ]),
                radius=0.03
            )
            for _ in range(num_points)
        ]

        # Add points to the scene
        self.play(*[Create(point) for point in points])

        # Extract point coordinates
        point_coords = np.array([point.get_center()[:2] for point in points])  # Extract only x and y

        # Perform Delaunay triangulation
        tri = Delaunay(point_coords)

        # Draw lines based on Delaunay triangulation
        lines = []
        for simplex in tri.simplices:
            p1, p2, p3 = simplex
            lines.append(Line(points[p1].get_center(), points[p2].get_center()))
            lines.append(Line(points[p2].get_center(), points[p3].get_center()))
            lines.append(Line(points[p3].get_center(), points[p1].get_center()))

        # Remove duplicate lines
        unique_lines = list(set(lines))

        # Draw connections
        self.play(*[Create(line) for line in unique_lines])

        # Keep the animation on screen for a while
        self.wait(2)
