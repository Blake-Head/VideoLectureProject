from manim import *
import manim_physics as mp
import numpy as np

class RotatingSphere(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        sphere = Sphere(radius=2, color=BLUE)
        xyz = ThreeDAxes()
        self.add(xyz, sphere)
        
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(10)  # Adjust the duration to how long you want the rotation to last.
        self.stop_ambient_camera_rotation()
        # Here is a change



class GaussBlob(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()  # Add the XYZ coordinate axes

        # Add labels to the axes
        x_label = axes.get_x_axis_label("X")
        y_label = axes.get_y_axis_label("Y")
        z_label = axes.get_z_axis_label("Z")

        # Define the blob-like shape
        blob = Surface(
            lambda u, v: np.array([
                3 * np.sin(u) * np.cos(v) * (1 + 0.3 * np.sin(3 * u) * np.cos(3 * v)),
                2 * np.sin(u) * np.sin(v) * (1 + 0.3 * np.sin(3 * u) * np.cos(3 * v)),
                2 * np.cos(u) * (1 + 0.3 * np.sin(3 * u) * np.cos(3 * v))
            ]),
            u_range=[0, PI],
            v_range=[0, TAU],
            checkerboard_colors=[BLUE, GREEN]
        )

        self.add(axes, blob, x_label, y_label, z_label)
        
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(10)  # Adjust the duration to how long you want the rotation to last.
        self.stop_ambient_camera_rotation()

class GaussCube(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()  # Add the XYZ coordinate axes

        # Add labels to the axes
        x_label = axes.get_x_axis_label("X")
        y_label = axes.get_y_axis_label("Y")
        z_label = axes.get_z_axis_label("Z")

        # Create the cube
        cube = Cube(side_length=2, fill_opacity=0.75, fill_color=BLUE, stroke_width=1)

        self.add(axes, cube, x_label, y_label, z_label)
        
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(10)  # Adjust the duration to how long you want the rotation to last.
        self.stop_ambient_camera_rotation()

class GaussCylinder(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()  # Add the XYZ coordinate axes

        # Add labels to the axes
        x_label = axes.get_x_axis_label("X")
        y_label = axes.get_y_axis_label("Y")
        z_label = axes.get_z_axis_label("Z")

        # Create the cube
        cylinder = Cylinder(radius=1, height=3, fill_opacity=0.75, fill_color=BLUE, stroke_width=1)

        self.add(axes, cylinder, x_label, y_label, z_label)
        
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(10)  # Adjust the duration to how long you want the rotation to last.
        self.stop_ambient_camera_rotation()

class ChargedGauss(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()  # Add the XYZ coordinate axes

        # Add labels to the axes
        x_label = axes.get_x_axis_label("X")
        y_label = axes.get_y_axis_label("Y")
        z_label = axes.get_z_axis_label("Z")

        # Create the cube
        cube = Cube(side_length=2, fill_opacity=0.25, fill_color=BLUE, stroke_width=1)

        # Create a sphere of charge inside the cube
        charge = Dot3D(point=ORIGIN, radius=0.1, color=RED)

        # Create the electric field vector arrows around the cube
        arrows = VGroup()
        directions = [RIGHT, LEFT, UP, DOWN, OUT, IN, UR, UL, DR, DL]
        for dir in directions:
            arrow = Arrow3D(start=cube.get_center() + dir, end=cube.get_center() + dir*2, color=YELLOW)
            arrows.add(arrow)

        # Add everything to the scene
        self.add(axes, x_label, y_label, z_label,
                 cube, charge, arrows)

        # Play the scene
        # self.begin_ambient_camera_rotation(rate=0.5)
        # self.wait(5)  # Adjust the duration to how long you want the rotation to last.
        # self.stop_ambient_camera_rotation()

class NewChargedGauss(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()  # Add the XYZ coordinate axes

        # Add labels to the axes
        x_label = axes.get_x_axis_label("X")
        y_label = axes.get_y_axis_label("Y")
        z_label = axes.get_z_axis_label("Z")

        # Create the cube
        cube = Cube(side_length=2, fill_opacity=0.25, fill_color=BLUE, stroke_width=1)

        # Create a sphere of charge inside the cube
        charge = Dot3D(point=ORIGIN, radius=0.1, color=RED)

        # Create the electric field vector arrows around the cube
        center_point = cube.get_center()
        num_lines = 8
        radius = 3

        arrows = VGroup()
        for i in range(num_lines):
            for j in range(num_lines):
                theta = i * (TAU / num_lines)
                phi = j * (PI / num_lines)
                end_point = radius * np.array([
                    np.sin(phi) * np.cos(theta),
                    np.sin(phi) * np.sin(theta),
                    np.cos(phi)
                ])
                arrow = Arrow3D(center_point, end_point)
                arrows.add(arrow)

        # Add everything to the scene
        self.add(axes, x_label, y_label, z_label,
                 cube, charge, arrows)

        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(2.5)  # Adjust the duration to how long you want the rotation to last.
        self.stop_ambient_camera_rotation()