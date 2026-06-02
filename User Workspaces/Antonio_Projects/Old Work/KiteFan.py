from manim import *
import manim_physics as mp
import numpy as np

# 3 Charges in a field with basic lines and arrows connecting them
class ThreeCharges(Scene):
     def construct(self):   
        # Create the charges and set the position
        charge1 = mp.Charge(magnitude=1, point=np.array([-4, -1, 0]))
        charge2 = mp.Charge(magnitude=1, point=np.array([4, 1, 0]))

        charge3 = mp.Charge(magnitude=-1, point=np.array([0, 3, 0]))

        # Add to the scene
        self.add(charge1, charge2, charge3)

        # Create the lines that connect the charges
        line1 = Line(start = charge1.get_center(), end=charge3.get_center())
        line2 = Line(start = charge1.get_center(), end=charge2.get_center())
        line3 = Line(start = charge2.get_center(), end=charge3.get_center())

        # Add to the scene
        self.add(line1, line2, line3)

        # Create the Force arrows
        # Charge 1 arrows
        q1_f1_arrow = LabeledArrow(MathTex("\\vec{F_1}"), start=charge1.get_center(), end=charge3.get_center(), color=GREEN)
        
        # Reverse the direction of q1_f2_arrow while keeping the same magnitude
        q1_f2_start = charge1.get_center()
        q1_f2_end = charge2.get_center()
        q1_f2_magnitude = q1_f2_end - q1_f2_start
        reversed_q1_f2_end = q1_f2_start - q1_f2_magnitude
        q1_f2_arrow = LabeledArrow(MathTex("\\vec{F_2}"), start=charge1.get_center(), end=reversed_q1_f2_end, color=GREEN)

        q1_f1_arrow.scale(0.25, about_point=q1_f1_arrow.get_start())
        q1_f2_arrow.scale(0.25, about_point=q1_f2_arrow.get_start())

        # Charge 2 arrows
        q2_f3_arrow = LabeledArrow(MathTex("\\vec{F_3}"), start=charge2.get_center(), end=charge3.get_center(), color=GREEN)
        
        # Reverse the direction of q2_f2_arrow while keeping the same magnitude
        q2_f2_start = charge2.get_center()
        q2_f2_end = charge1.get_center()
        q2_f2_magnitude = q2_f2_end - q2_f2_start
        reversed_q2_f2_end = q2_f2_start - q2_f2_magnitude
        q2_f2_arrow = LabeledArrow(MathTex("\\vec{F_2}"), start=charge2.get_center(), end=reversed_q2_f2_end, color=GREEN)

        q2_f3_arrow.scale(0.25, about_point=q2_f3_arrow.get_start())
        q2_f2_arrow.scale(0.25, about_point=q2_f2_arrow.get_start())

        # Charge 3 arrows
        q3_f1_arrow = LabeledArrow(MathTex("\\vec{F_1}"), start=charge3.get_center(), end=charge1.get_center(), color=GREEN)
        q3_f3_arrow = LabeledArrow(MathTex("\\vec{F_3}"), start=charge3.get_center(), end=charge2.get_center(), color=GREEN)

        q3_f1_arrow.scale(0.25, about_point=q3_f1_arrow.get_start())
        q3_f3_arrow.scale(0.25, about_point=q3_f3_arrow.get_start())

        # Add the arrows to the Scene
        self.add(q1_f1_arrow, q1_f2_arrow, q2_f2_arrow, q2_f3_arrow, q3_f1_arrow, q3_f3_arrow)

        # Equation time
        equation = MathTex(
            "\\vec{F_c}", "=", "k_c", "{q_1", "q_2", "\\over", "r^2}", "\\hat{r}"
        )
        equation.move_to(DOWN*1.5)

        #Add the equation
        self.add(equation)

# Basic 3 charges in an E Field
class ThreeChargesElectricField(Scene):
     def construct(self):
        # Create the charges and set the position
        charge1 = mp.Charge(magnitude=1, point=np.array([-4, -1, 0]))
        charge2 = mp.Charge(magnitude=1, point=np.array([4, 1, 0]))

        charge3 = mp.Charge(magnitude=-1, point=np.array([0, 3, 0]))

        # Create the ELectric Field
        field =mp.ElectricField(charge1, charge2, charge3)

        # Create the scene
        self.add(field, charge1, charge2, charge3)

# Basic scene of the kite and the fan in one scene together
    # No streamlines
class OffKiteFan(Scene):
    def construct(self):
        # Create the fan center
        fan_center = Dot(radius=0.15, color=WHITE)
        fan_body = Circle(radius = 1.2, color=WHITE)
        fan_base = Ellipse(width = 1.8, height= 0.2, color=WHITE).shift(DOWN*3)
        fan_stand = Line(start=fan_body.get_bottom(), end=fan_base.get_top(), color=WHITE)
        
        # Create the fan blades
        blade1 = Polygon(
            ORIGIN, 
            [0.3, 0.3, 0], 
            [0.8, 0, 0], 
            [-0.3, -0.3, 0],
            color=WHITE,
            fill_opacity=0.6
        ).shift(UP * 0.6).rotate(PI / 6)

        # Clone blades and position them
        blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=ORIGIN)
        blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=ORIGIN)

        corner_cover1 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*5+RIGHT*7)
        corner_cover2 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*-5+RIGHT*7)

        # Group the blades and center
        fan_blades = VGroup(blade1, blade2, blade3)
        fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3) 

        # Create the kite
        kite_top = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).scale(2).shift(LEFT*3)
                
        # Create the string 
        kite_string = VMobject() 
        kite_string.set_points_as_corners( [[-0.6, -1, 0], 
                                            [-0.7, -1.1, 0], 
                                            [-0.5, -1.2, 0], 
                                            [-0.6, -1.3, 0], 
                                            [-0.5, -1.4, 0], 
                                            [-0.6, -1.5, 0]] 
                                        ).scale(3).shift(LEFT*3) 
        
        kite = VGroup(kite_top, kite_string)
        
        # Animate the fan spinning
        self.play(FadeIn(fan))
        self.play(FadeIn(kite))

# Basic scene of the kite, fan, and streamlines
class OnKiteFan(Scene):
    def construct(self):
        # Create the fan center
        fan_center = Dot(radius=0.15, color=WHITE)
        fan_body = Circle(radius = 1.2, color=WHITE)
        fan_base = Ellipse(width = 1.8, height= 0.2, color=WHITE).shift(DOWN*3)
        fan_stand = Line(start=fan_body.get_bottom(), end=fan_base.get_top(), color=WHITE)
        
        # Create the fan blades
        blade1 = Polygon(
            ORIGIN, 
            [0.3, 0.3, 0], 
            [0.8, 0, 0], 
            [-0.3, -0.3, 0],
            color=WHITE,
            fill_opacity=0.6
        ).shift(UP * 0.6).rotate(PI / 6)

        # Clone blades and position them
        blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=ORIGIN)
        blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=ORIGIN)

        corner_cover1 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*5+RIGHT*7)
        corner_cover2 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*-5+RIGHT*7)

        # Group the blades and center
        fan_blades = VGroup(blade1, blade2, blade3)
        fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3)  
        
        # Animate the fan spinning
        self.play(FadeIn(fan))

        # Use an `always_rotate` or run the animation in the background
        fan_blades.add_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )
        def wind_field(point):
                x, y, _ = point
                x -= 1  # Fan origin in x-axis
                y -= 0   # Fan origin in y-axis
                
                # Compute the magnitude and direction of airflow
                distance = np.sqrt(x**2 + y**2)
                if distance == 0:
                    return np.array([0, 0, 0])
                
                # Magnitude decreases with distance from the fan
                magnitude = 1 / (1 + 0.2 * distance)
                
                # Flow primarily in x-direction with some spreading in y-direction
                direction = np.array([-1, y / (distance + 0.1), 0])
                
                # Normalize and scale with magnitude
                return magnitude * direction
            
        # Create streamlines from the vector field
        stream_lines = StreamLines(
            wind_field,
            stroke_width=3,
            max_anchors_per_line=30,
            virtual_time=4
        )

                # Create the kite
        kite_top = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).scale(2).shift(LEFT)
                
        # Create the string 
        kite_string = VMobject() 
        kite_string.set_points_as_corners( [[-0.6, -1, 0], 
                                            [-0.7, -1.1, 0], 
                                            [-0.5, -1.2, 0], 
                                            [-0.6, -1.3, 0], 
                                            [-0.5, -1.4, 0], 
                                            [-0.6, -1.5, 0]] 
                                        ).scale(3).shift(LEFT) 
        
        kite = VGroup(kite_top, kite_string)
                
        # Add to the scene
        self.add(stream_lines)
        self.add(corner_cover1, corner_cover2)
        self.add(fan_base,fan_stand)
        self.add(kite)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

        #Make the kite move with the wind
        self.play(kite.animate.shift(LEFT*3), run_time=5)

        # Keep the animation running for display
        self.wait(5)

        # Use an `always_rotate` or run the animation in the background
        fan_blades.remove_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )

        self.wait(2)

# Kite, with a growing fan and streamline
    # Need to fix the blades attaching to the center of the fan
    # Need to fix the starting point of the streamline
class KiteBigFan(Scene):
    def construct(self):
        # Create the fan center
        fan_center = Dot(radius=0.15, color=WHITE)
        fan_body = Circle(radius = 1.2, color=WHITE)
        fan_base = Ellipse(width = 1.8, height= 0.2, color=WHITE).shift(DOWN*3)
        fan_stand = Line(start=fan_body.get_bottom(), end=fan_base.get_top(), color=WHITE)
        
        # Create the fan blades
        blade1 = Polygon(
            fan_center.get_center(), 
            [1.2 * np.cos(PI / 6), 1.2 * np.sin(PI / 6), 0], 
            [1.2 * np.cos(-PI / 6), 1.2 * np.sin(-PI / 6), 0],
            fan_center.get_center(),
            color=WHITE,
            fill_opacity=0.6
        ).rotate(PI / 6, about_point=fan_center.get_center())

        # Clone blades and position them
        blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=fan_center.get_center())
        blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=fan_center.get_center())

        corner_cover1 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*5+RIGHT*7)
        corner_cover2 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*-5+RIGHT*7)

        # Group the blades and center
        fan_blades = VGroup(blade1, blade2, blade3)
        fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3)  
        
        #Add an updater to keep the fans rotating around the center point
        def rotate_blades(mob, dt):
            mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())
        
        fan_blades.add_updater(rotate_blades)

        # Animate the fan spinning
        self.play(FadeIn(fan))

        # Use an `always_rotate` or run the animation in the background
        fan_blades.add_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )
        def wind_field(point):
                x, y, _ = point
                x -= 1  # Fan origin in x-axis
                y -= 0   # Fan origin in y-axis
                
                # Compute the magnitude and direction of airflow
                distance = np.sqrt(x**2 + y**2)
                if distance == 0:
                    return np.array([0, 0, 0])
                
                # Magnitude decreases with distance from the fan
                magnitude = 1 / (1 + 0.2 * distance)
                
                # Flow primarily in x-direction with some spreading in y-direction
                direction = np.array([-1, y / (distance + 0.1), 0])
                
                # Normalize and scale with magnitude
                return magnitude * direction
            
        # Create streamlines from the vector field
        stream_lines = StreamLines(
            wind_field,
            stroke_width=3,
            max_anchors_per_line=30,
            virtual_time=4
        )

                # Create the kite
        kite_top = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).scale(2).shift(LEFT)
                
        # Create the string 
        kite_string = VMobject() 
        kite_string.set_points_as_corners( [[-0.6, -1, 0], 
                                            [-0.7, -1.1, 0], 
                                            [-0.5, -1.2, 0], 
                                            [-0.6, -1.3, 0], 
                                            [-0.5, -1.4, 0], 
                                            [-0.6, -1.5, 0]] 
                                        ).scale(3).shift(LEFT) 
        
        kite = VGroup(kite_top, kite_string)
        
        # Add animated streamlines
        
        # Add to the scene
        self.add(stream_lines)
        self.add(corner_cover1, corner_cover2)
        self.add(fan_base,fan_stand)
        self.add(kite)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

        #Grow the fan
        self.play(fan.animate.scale(1.5), # Adjust the scale factor as needed 
             run_time=5 )
        
        #Move the kite
        self.play( kite.animate.shift(LEFT*3), run_time=2.5)
        
        # Keep the animation running for display
        self.wait(5)

        # Use an `always_rotate` or run the animation in the background
        fan_blades.remove_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )

        self.wait(2)

# Kite, with a shrinking fan and streamline
    # Need to fix the blades attaching to the center of the fan
    # Need to fix the starting point of the streamline
class KiteSmallFan(Scene):
    def construct(self):
        # Create the fan center
        fan_center = Dot(radius=0.15, color=WHITE)
        fan_body = Circle(radius = 1.2, color=WHITE)
        fan_base = Ellipse(width = 1.8, height= 0.2, color=WHITE).shift(DOWN*3)
        fan_stand = Line(start=fan_body.get_bottom(), end=fan_base.get_top(), color=WHITE)
        
        # Create the fan blades
        blade1 = Polygon(
            ORIGIN, 
            [0.3, 0.3, 0], 
            [0.8, 0, 0], 
            [-0.3, -0.3, 0],
            color=WHITE,
            fill_opacity=0.6
        ).shift(UP * 0.6).rotate(PI / 6)

        # Clone blades and position them
        blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=ORIGIN)
        blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=ORIGIN)

        corner_cover1 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*5+RIGHT*7)
        corner_cover2 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*-5+RIGHT*7)

        # Group the blades and center
        fan_blades = VGroup(blade1, blade2, blade3)
        fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3)  
        
        # Animate the fan spinning
        self.play(FadeIn(fan))

        # Use an `always_rotate` or run the animation in the background
        fan_blades.add_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )
        def wind_field(point):
                x, y, _ = point
                x -= 1  # Fan origin in x-axis
                y -= 0   # Fan origin in y-axis
                
                # Compute the magnitude and direction of airflow
                distance = np.sqrt(x**2 + y**2)
                if distance == 0:
                    return np.array([0, 0, 0])
                
                # Magnitude decreases with distance from the fan
                magnitude = 1 / (1 + 0.2 * distance)
                
                # Flow primarily in x-direction with some spreading in y-direction
                direction = np.array([-1, y / (distance + 0.1), 0])
                
                # Normalize and scale with magnitude
                return magnitude * direction
            
        # Create streamlines from the vector field
        stream_lines = StreamLines(
            wind_field,
            stroke_width=3,
            max_anchors_per_line=30,
            virtual_time=4
        )

                # Create the kite
        kite_top = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).scale(2).shift(LEFT)
                
        # Create the string 
        kite_string = VMobject() 
        kite_string.set_points_as_corners( [[-0.6, -1, 0], 
                                            [-0.7, -1.1, 0], 
                                            [-0.5, -1.2, 0], 
                                            [-0.6, -1.3, 0], 
                                            [-0.5, -1.4, 0], 
                                            [-0.6, -1.5, 0]] 
                                        ).scale(3).shift(LEFT) 
        
        kite = VGroup(kite_top, kite_string)
        
        # Add animated streamlines
        
        # Add to the scene
        self.add(stream_lines)
        self.add(corner_cover1, corner_cover2)
        self.add(fan_base,fan_stand)
        self.add(kite)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

        #Grow the fan
        self.play(fan.animate.scale(0.5), # Adjust the scale factor as needed 
             run_time=5 )
        
        #Move the kite
        self.play( kite.animate.shift(LEFT*3), run_time=2.5)
        
        # Keep the animation running for display
        self.wait(5)

        # Use an `always_rotate` or run the animation in the background
        fan_blades.remove_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )

        self.wait(2)

# Moving kite in the streamline following an arc from the top to the bottom of the scene
class MovingKite(Scene):
    def construct(self):
        # Create the fan center
        fan_center = Dot(radius=0.15, color=WHITE)
        fan_body = Circle(radius = 1.2, color=WHITE)
        fan_base = Ellipse(width = 1.8, height= 0.2, color=WHITE).shift(DOWN*3)
        fan_stand = Line(start=fan_body.get_bottom(), end=fan_base.get_top(), color=WHITE)
        
        # Create the fan blades
        blade1 = Polygon(
            ORIGIN, 
            [0.3, 0.3, 0], 
            [0.8, 0, 0], 
            [-0.3, -0.3, 0],
            color=WHITE,
            fill_opacity=0.6
        ).shift(UP * 0.6).rotate(PI / 6)

        # Clone blades and position them
        blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=ORIGIN)
        blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=ORIGIN)

        corner_cover1 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*5+RIGHT*7)
        corner_cover2 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*-5+RIGHT*7)

        # Group the blades and center
        fan_blades = VGroup(blade1, blade2, blade3)
        fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3)  
        
        # Animate the fan spinning
        self.play(FadeIn(fan))

        # Use an `always_rotate` or run the animation in the background
        fan_blades.add_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )
        def wind_field(point):
                x, y, _ = point
                x -= 1  # Fan origin in x-axis
                y -= 0   # Fan origin in y-axis
                
                # Compute the magnitude and direction of airflow
                distance = np.sqrt(x**2 + y**2)
                if distance == 0:
                    return np.array([0, 0, 0])
                
                # Magnitude decreases with distance from the fan
                magnitude = 1 / (1 + 0.2 * distance)
                
                # Flow primarily in x-direction with some spreading in y-direction
                direction = np.array([-1, y / (distance + 0.1), 0])
                
                # Normalize and scale with magnitude
                return magnitude * direction
            
        # Create streamlines from the vector field
        stream_lines = StreamLines(
            wind_field,
            stroke_width=3,
            max_anchors_per_line=30,
            virtual_time=4
        )

                # Create the kite
        kite_top = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).scale(2).shift(LEFT)
                
        # Create the string 
        kite_string = VMobject() 
        kite_string.set_points_as_corners( [[-0.6, -1, 0], 
                                            [-0.7, -1.1, 0], 
                                            [-0.5, -1.2, 0], 
                                            [-0.6, -1.3, 0], 
                                            [-0.5, -1.4, 0], 
                                            [-0.6, -1.5, 0]] 
                                        ).scale(3).shift(LEFT) 
        
        kite = VGroup(kite_top, kite_string)
        
        # Add animated streamlines
        
        # Add to the scene
        self.add(stream_lines)
        self.add(corner_cover1, corner_cover2)
        self.add(fan_base,fan_stand)
        self.add(kite)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

        # Animate the kite moving in a semi-circle around the origin 
        radius = 3
        angle = PI # Semi-circle
        path = Arc(radius=radius, angle=angle, start_angle=PI/2).shift(kite.get_center()) 
        self.play(MoveAlongPath(kite, path), run_time=10)



        # Use an `always_rotate` or run the animation in the background
        fan_blades.remove_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )

        self.wait(2)

# Kite grows and shrinks with a red color to represent the cross-sectional area
class ChangingKiteFan(Scene):
    def construct(self):
        # Create the fan center
        fan_center = Dot(radius=0.15, color=WHITE)
        fan_body = Circle(radius = 1.2, color=WHITE)
        fan_base = Ellipse(width = 1.8, height= 0.2, color=WHITE).shift(DOWN*3)
        fan_stand = Line(start=fan_body.get_bottom(), end=fan_base.get_top(), color=WHITE)
        
        # Create the fan blades
        blade1 = Polygon(
            ORIGIN, 
            [0.3, 0.3, 0], 
            [0.8, 0, 0], 
            [-0.3, -0.3, 0],
            color=WHITE,
            fill_opacity=0.6
        ).shift(UP * 0.6).rotate(PI / 6)

        # Clone blades and position them
        blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=ORIGIN)
        blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=ORIGIN)

        corner_cover1 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*5+RIGHT*7)
        corner_cover2 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*-5+RIGHT*7)

        # Group the blades and center
        fan_blades = VGroup(blade1, blade2, blade3)
        fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3)  
        
        # Animate the fan spinning
        self.play(FadeIn(fan))

        # Use an `always_rotate` or run the animation in the background
        fan_blades.add_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )
        def wind_field(point):
                x, y, _ = point
                x -= 1  # Fan origin in x-axis
                y -= 0   # Fan origin in y-axis
                
                # Compute the magnitude and direction of airflow
                distance = np.sqrt(x**2 + y**2)
                if distance == 0:
                    return np.array([0, 0, 0])
                
                # Magnitude decreases with distance from the fan
                magnitude = 1 / (1 + 0.2 * distance)
                
                # Flow primarily in x-direction with some spreading in y-direction
                direction = np.array([-1, y / (distance + 0.1), 0])
                
                # Normalize and scale with magnitude
                return magnitude * direction
            
        # Create streamlines from the vector field
        stream_lines = StreamLines(
            wind_field,
            stroke_width=3,
            max_anchors_per_line=30,
            virtual_time=4
        )

                # Create the kite
        kite_top = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=RED, 
                           fill_opacity=0.6
                        ).scale(2).shift(LEFT)
                
        # Create the string 
        kite_string = VMobject() 
        kite_string.set_points_as_corners( [[-0.6, -1, 0], 
                                            [-0.7, -1.1, 0], 
                                            [-0.5, -1.2, 0], 
                                            [-0.6, -1.3, 0], 
                                            [-0.5, -1.4, 0], 
                                            [-0.6, -1.5, 0]] 
                                        ).scale(3).shift(LEFT) 
        
        kite = VGroup(kite_top, kite_string)
        
        # Add to the scene
        self.add(stream_lines)
        self.add(corner_cover1, corner_cover2)
        self.add(fan_base,fan_stand)
        self.add(kite)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

        #Make the kite grow
        self.play(kite.animate.scale(2), run_time=5)

        #Make the kite shrink
        self.play(kite.animate.scale(0.25), run_time=5)

        # Keep the animation running for display
        self.wait(5)

        # Use an `always_rotate` or run the animation in the background
        fan_blades.remove_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )

        self.wait(2)

# Transition Scene where the Kite and Fan turn into charges
class ChargeTransition(Scene):
     def construct(self):
        # Create the fan center
        fan_center = Dot(radius=0.15, color=WHITE)
        fan_body = Circle(radius = 1.2, color=WHITE)
        fan_base = Ellipse(width = 1.8, height= 0.2, color=WHITE).shift(DOWN*3)
        fan_stand = Line(start=fan_body.get_bottom(), end=fan_base.get_top(), color=WHITE)
        
        # Create the fan blades
        blade1 = Polygon(
            ORIGIN, 
            [0.3, 0.3, 0], 
            [0.8, 0, 0], 
            [-0.3, -0.3, 0],
            color=WHITE,
            fill_opacity=0.6
        ).shift(UP * 0.6).rotate(PI / 6)

        # Clone blades and position them
        blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=ORIGIN)
        blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=ORIGIN)

        # Group the blades and center
        fan_blades = VGroup(blade1, blade2, blade3)
        fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3) 

        # Create the kite
        kite_top = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).scale(2).shift(LEFT*3)
                
        # Create the string 
        kite_string = VMobject() 
        kite_string.set_points_as_corners( [[-0.6, -1, 0], 
                                            [-0.7, -1.1, 0], 
                                            [-0.5, -1.2, 0], 
                                            [-0.6, -1.3, 0], 
                                            [-0.5, -1.4, 0], 
                                            [-0.6, -1.5, 0]] 
                                        ).scale(3).shift(LEFT*3) 
        
        kite = VGroup(kite_top, kite_string)

        # Create the objects to transition to
        kite_charge = mp.Charge(magnitude=1, point=kite.get_center())
        fan_charge = mp.Charge(magnitude=5, point=fan_blades.get_center())

        # Transform!
        self.add(kite)
        self.add(fan)
        self.wait(2)

        self.play(Transform(kite, kite_charge))
        self.play(Transform(fan, fan_charge))
        self.wait(2)

        # Label the new charges
        q = MathTex("q").next_to(kite_charge, UP+5)
        Q = MathTex("Q").next_to(fan_charge, UP+5)
        self.play(Write(q))
        self.play(Write(Q))

# Transition Scene of Streamlines to Arrows
class StreamlineToArrows(Scene):
    def construct(self):
        # Create the fan center
        fan_center = Dot(radius=0.15, color=WHITE)
        fan_body = Circle(radius = 1.2, color=WHITE)
        fan_base = Ellipse(width = 1.8, height= 0.2, color=WHITE).shift(DOWN*3)
        fan_stand = Line(start=fan_body.get_bottom(), end=fan_base.get_top(), color=WHITE)
        
        # Create the fan blades
        blade1 = Polygon(
            ORIGIN, 
            [0.3, 0.3, 0], 
            [0.8, 0, 0], 
            [-0.3, -0.3, 0],
            color=WHITE,
            fill_opacity=0.6
        ).shift(UP * 0.6).rotate(PI / 6)

        # Clone blades and position them
        blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=ORIGIN)
        blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=ORIGIN)

        corner_cover1 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*5+RIGHT*7)
        corner_cover2 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*-5+RIGHT*7)

        # Group the blades and center
        fan_blades = VGroup(blade1, blade2, blade3)
        fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3)  
        
        # Animate the fan spinning
        self.play(FadeIn(fan))

        # Use an `always_rotate` or run the animation in the background
        fan_blades.add_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )
        def wind_field(point):
                x, y, _ = point
                x -= 1  # Fan origin in x-axis
                y -= 0   # Fan origin in y-axis
                
                # Compute the magnitude and direction of airflow
                distance = np.sqrt(x**2 + y**2)
                if distance == 0:
                    return np.array([0, 0, 0])
                
                # Magnitude decreases with distance from the fan
                magnitude = 1 / (1 + 0.2 * distance)
                
                # Flow primarily in x-direction with some spreading in y-direction
                direction = np.array([-1, y / (distance + 0.1), 0])
                
                # Normalize and scale with magnitude
                return magnitude * direction
            
        # Create streamlines from the vector field
        stream_lines = StreamLines(
            wind_field,
            stroke_width=3,
            max_anchors_per_line=30,
            virtual_time=4
        )
                
        # Add to the scene
        self.add(stream_lines)
        self.add(corner_cover1, corner_cover2)
        self.add(fan_base,fan_stand)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

        # Keep the animation running for display
        self.wait(5)

        # Use an `always_rotate` or run the animation in the background
        fan_blades.remove_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )

        self.wait(2)

        #Create the top arrow Vgroup
        top_arrows_group = VGroup()

        # Parameters for the semicircle path
        radius = 3
        num_arrows = 10
        angle_step = PI / (num_arrows - 1)
        
        # Generate arrows following a semicircle path
        for i in range(num_arrows):
            angle = i * angle_step
            start_point = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            end_point = ORIGIN
            arrow = Arrow(start=start_point, end=end_point)
            top_arrows_group.add(arrow)
        
        # Position the VGroup in the scene
        top_arrows_group.move_to(fan_body.get_center())


        # Create the bottom arrows
        bottom_arrows_group = VGroup()

        # Parameters for the semicircle path
        radius = 3
        num_arrows = 10
        angle_step = PI / (num_arrows - 1)
        
        # Generate arrows following a semicircle path
        for i in range(num_arrows):
            angle = i * angle_step
            start_point = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            end_point = 2 * start_point - ORIGIN
            arrow = Arrow(start=start_point, end=end_point)
            bottom_arrows_group.add(arrow)
        
        # Position the VGroup in the scene
        bottom_arrows_group.move_to(fan_body.get_center())

        # Create the arrow vgroup
        arrow_group= VGroup(top_arrows_group, bottom_arrows_group)

        # Transform!
        self.play(Transform(stream_lines, arrow_group))
        self.wait(2)
