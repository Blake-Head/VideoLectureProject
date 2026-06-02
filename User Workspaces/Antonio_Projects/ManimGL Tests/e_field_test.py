from manim import *
import manim_physics as mp
import numpy as np

class PointChargeInElectricField_Dynamic(Scene):
    def construct(self):
        # Create the point charge
        pointCharge = mp.Charge(magnitude=1, point=np.array([-3, 0, 0]))
        field = always_redraw(lambda:
                              mp.ElectricField(pointCharge))

        # Add the electric field and the point charge to the scene
        self.add(field, pointCharge)

        # Add a set path for the point charge to move along
        path = Line(start=pointCharge.get_center(), end=RIGHT * 3)

        # Animation time!
        self.play(MoveAlongPath(pointCharge, path, rate_func=linear, run_time=5))

        self.wait(1)

class DynanmicElectricField(Scene):
    def construct(self):
        # Create the charges and set the position
        charge1 = mp.Charge(magnitude=1, point=np.array([-3, -1, 0]))
        charge2 = mp.Charge(magnitude=-1, point=np.array([3, 1, 0]))
        
        # Creating the super cool dynamic field
        field = always_redraw(lambda:
                              mp.ElectricField(charge1, charge2))

        # Add the electric field and the charges to the scene
        self.add(field, charge1, charge2)

        # Moving the charges
        path1 = Line(start=charge1.get_center(), end=RIGHT * 3)
        path2 = Line(start=charge2.get_center(), end=LEFT * 3)

        # Animation time!
        self.play(MoveAlongPath(charge1, path1, rate_func=linear, run_time=5),
                    MoveAlongPath(charge2, path2, rate_func=linear, run_time=5))

        self.wait(1)