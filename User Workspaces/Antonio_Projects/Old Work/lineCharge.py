from manim import *
import manim_physics as mp
import numpy as np
import math

class lineCharge(Scene):
    def construct(self):
        ncharges = 25 # Set number of charges
        #Creating the line charge made up of point charges using this VGroup function
        line1 = VGroup(*[
            mp.Charge(magnitude=1, point=np.array([(i-ncharges//2), 0, 0]), add_glow=False) # Added a floor division operator to dynamically center line of charges (that's the // symbol)
                      for i in range(ncharges)
        ])

        #Create the Electric Field
        field1 = mp.ElectricField(*line1)

        #Creating the scene
        self.add(field1, *line1)
        #self.play(FadeIn(*line1))
        #self.play(FadeIn(field1))
        self.wait()

        #This code has the charges spaced out a bit but the electric field looks nice

# Blake added this one
class lineCharge_circle(Scene):
    def construct(self):
        #circ = Circle(RED)
        ncharges = 10 # Set number of charges
        r = 1 # Set radius of circle
        #Creating the line charge made up of point charges using this VGroup function
        line1 = VGroup(*[
            mp.Charge(magnitude=1, point=np.array([r*math.cos(2*PI*i/ncharges), r*math.sin(2*PI*i/ncharges), 0]), add_glow=False) # Added a floor division operator to dynamically center line of charges (that's the // symbol)
                      for i in range(ncharges)
        ])

        #Create the Electric Field
        field1 = mp.ElectricField(*line1)
        
        ncharges = 25
        line2 = VGroup(*[
            mp.Charge(magnitude=1, point=np.array([r*math.cos(2*PI*i/ncharges), r*math.sin(2*PI*i/ncharges), 0]), add_glow=False) # Added a floor division operator to dynamically center line of charges (that's the // symbol)
                      for i in range(ncharges)
        ])

        #Create the Electric Field
        field2 = mp.ElectricField(*line2)

        ncharges = 50
        line3 = VGroup(*[
            mp.Charge(magnitude=1, point=np.array([r*math.cos(2*PI*i/ncharges), r*math.sin(2*PI*i/ncharges), 0]), add_glow=False) # Added a floor division operator to dynamically center line of charges (that's the // symbol)
                      for i in range(ncharges)
        ])

        #Create the Electric Field
        field3 = mp.ElectricField(*line3)

        #Creating the scene
        self.play(FadeIn(*line1))
        self.play(FadeIn(field1))
        self.wait()
        self.play(FadeOut(line1, field1), FadeIn(line2, field2))
        self.play(FadeOut(line2, field2), FadeIn(line3, field3))

class lineChargeClose(Scene):
    def construct(self):
        #Creating the line charge made up of point charges using this VGroup function
        line1 = VGroup(*[
            mp.Charge(magnitude=1/10, point=np.array([(i - 5)*0.05, 0, 0]), add_glow=False)
                      for i in range(100)
        ])
        # Remove the opacity of the line charges and just throw in a physical line

        #Create the Electric Field
        field1 = mp.ElectricField(*line1)

        #Creating the scene
        self.add(field1, *line1)

        self.wait()

        #This code has the line being an actual line but the spread is much closer

#New class that adds a charge at a time to the line charge distribution

# class addingCharge(Scene):
#     def construct(self):
#         # Start with a single charge
#         charge1 = mp.Charge(magnitude=1, point=np.array([0, 0, 0])), add_glow=False)