from manim import *
import manim_physics as mp
import numpy as np

class Dynamic_Field(Scene):
    def construct(self):
        
        # Define the point charges
        pointcharge1 = mp.Charge(magnitude=1, point=np.array([-3, 0, 0]))
        pointcharge2 = mp.Charge(magnitude=2, point=np.array([2, 0, 0]))
        pointcharge3 = mp.Charge(magnitude=-1, point=np.array([0, 2, 0]))

        # Define the Electric field created by the point charges
        field = always_redraw(lambda: 
                              mp.ElectricField(pointcharge1, pointcharge2, pointcharge3))


        # Add the electric field and the point charges to the scene
        self.add(field, pointcharge1, pointcharge2, pointcharge3)

        # Add a set path for the point charge to move along
        path1 = Line(start=pointcharge1.get_center(), end=RIGHT * 3)
        path2 = Line(start=pointcharge2.get_center(), end=UP * 1)
        path3 = Line(start=pointcharge3.get_center(), end=DOWN * 3)

        # Animation time!
        self.play(MoveAlongPath(pointcharge1, path1, rate_func=linear, run_time=5),
                  MoveAlongPath(pointcharge2, path2, rate_func=linear, run_time=5),
                  MoveAlongPath(pointcharge3, path3, rate_func=linear, run_time=5))

        self.wait(1)

        
class Static_Field(Scene):
    def construct(self):
        
        # Define the point charges
        pointcharge1 = mp.Charge(magnitude=-2, point=np.array([-3, -2, 0]))
        pointcharge2 = mp.Charge(magnitude=-2, point=np.array([3, -2, 0]))
        pointcharge3 = mp.Charge(magnitude=-2, point=np.array([0, 2, 0]))

        # Define the Electric field created by the point charges
        field =  mp.ElectricField(pointcharge1, pointcharge2, pointcharge3)


        # Add the electric field and the point charges to the scene
        self.add(field, pointcharge1, pointcharge2, pointcharge3)


class Static_Field_2(Scene):
    def construct(self):
        # Define the point charges
        pointcharge1 = mp.Charge(magnitude=-1, point=np.array([-3, -2, 0]))
        pointcharge2 = mp.Charge(magnitude=-1, point=np.array([3, -2, 0]))
        pointcharge3 = mp.Charge(magnitude=-1, point=np.array([0, 2, 0]))

        # Define the Electric field function
        def efield_func(point):
            # Sum the field from each charge at the given point
            field = np.zeros(3)
            for charge in [pointcharge1, pointcharge2, pointcharge3]:
                r = point - charge.get_center()
                norm = np.linalg.norm(r)
                if norm < 0.1:
                    continue  # Avoid division by zero near the charge
                field += charge.magnitude * r / norm**3
            return field

        # Create stream lines for the field
        stream_lines = StreamLines(
            efield_func,
            x_range=[-5, 5],
            y_range=[-4, 4],
            colors=[YELLOW],
            stroke_width=2,
            max_anchors_per_line=100,
            virtual_time=3,
        )

        # Add the stream lines and the point charges to the scene
        self.add(stream_lines, pointcharge1, pointcharge2, pointcharge3)
        self.wait(2)