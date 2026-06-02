from manim import *
import manim_physics as mp
import numpy as np

# Globals

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


    def construct(self):        
        #Create the Fan VGroup
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
        blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=fan_center.get_center())
        blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=fan_center.get_center())

        # Group the blades and center
        fan_blades = VGroup(blade1, blade2, blade3)
        fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3)

        # Play the fan spinning
        self.play(FadeIn(fan))

        # Use an `always_rotate` or run the animation in the background
        fan_blades.add_updater(
            lambda mob, dt: mob.rotate(angle=-dt*PI, about_point=fan_center.get_center())  # Adjust rotation speed with `dt`
        )

        # Growing and shrinkning the fan
        self.play(fan.animate.scale(2), run_time=5)

        #Make the fan shrink
        self.play(fan.animate.scale(0.25), run_time=5)

    def construct(self):

        speed_tracker = ValueTracker(1.0)
        center_dot = Dot(ORIGIN, color=BLUE)
        self.add(center_dot)
        center_circle = Circle(radius=.5, color=RED)
        blade1 = Square(side_length=0.5).shift(UP * 2)
        blade2 = blade1.copy().rotate(PI*2/3, about_point=ORIGIN)
        blade3 = blade1.copy().rotate(-PI*2/3, about_point=ORIGIN)
        blades = VGroup(blade1, blade2, blade3, center_circle)
        self.play(Rotate(
                blades,
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
            )
            )
        
        # Use an `always_rotate` or run the animation in the background
        blades.add_updater(
            lambda mob, dt: mob.rotate(angle=dt*PI, about_point=ORIGIN)  # Adjust rotation speed with `dt`
        )

        self.play(blades.animate.scale(2), run_time=5)

class WindField(Scene):
        def construct(self):

# First, create all of the visual elements we will be using later on
# We will make:
    # (1) A fan with rotating blades
    # (2) A kite
    # (3) Up above this scene is the wind_field vector field
    # (4) Some 'corner covers' to cheat at making vectors fields.
    # (5) Create 'StreamLine' objects, which will be the lines of moving wind.
    # (6) Defining a force vector that will point away from the fan at all times, attached to our kite.

    # Here, we make the fan object.

            #Create the Fan VGroup
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
            blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=fan_center.get_center())
            blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=fan_center.get_center())

            # Group the blades and center
            fan_blades = VGroup(blade1, blade2, blade3)
            fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3)

    # Here we make the kite object.    

            #Create the kite
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

    #Add the Fan and Kite to the scene
            self.play(FadeIn(fan, kite))

    #Create the corner covers (hard coded)

            corner_cover1 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*5+RIGHT*7)
            corner_cover2 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*-5+RIGHT*7)


    # Create streamlines from the vector field
    # I define 3 different streamlines that will represent a slow/medium/fast fan speed.
    # I also slightly adjust the virtual_time variable for each, making it a bit larger for faster fields.

            # If things in the animation look a little bad, try changing the 'virtual time' paramenter by a couple.

            stream_lines_slow = StreamLines(
                wind_field,
                stroke_width=2, # Make the lines wider
                max_anchors_per_line=30,
                virtual_time=2 # 
            )

            stream_lines_med = StreamLines(
                wind_field,
                stroke_width=2, # Make the lines wider
                max_anchors_per_line=30,
                virtual_time=8 # 
            )

            stream_lines_fast = StreamLines(
                wind_field,
                stroke_width=2, # Make the lines wider
                max_anchors_per_line=30,
                virtual_time=12 # 
            )

            # This line adds an updater to the fan blades so that they will continue to rotate
            # throughout the animations.  
            # Multiplying the angle by 'speed' allows us to adjust the speed of the fan below.
            fan_blades.add_updater(lambda mob, dt: mob.rotate(angle=speed*dt*PI, 
                                                            about_point=fan_center.get_center())
                                )

    # Here we create the force vector that will illustrate the wind force.
    # Set vector parameters here:
            vec_color = PURE_GREEN
            vec_magnitude = 5
    # Function to compute vector direction and inverse distance magnitude
            def get_vector():
                direction = kite_top.get_center() - fan.get_center()  # Direction from red to blue
                distance = np.linalg.norm(direction)  # Compute distance
                
                if distance == 0:  # Avoid division by zero
                    return Vector([0, 0, 0]).set_color(vec_color)

                unit_direction = direction / distance  # Normalize direction
                magnitude = vec_magnitude / distance  # Inverse proportionality (scaled factor for visibility)

                return Vector(unit_direction * magnitude).set_color(vec_color).move_to(kite_top.get_center()).shift(unit_direction * magnitude / 2)  # Shift for proper positioning

            # Create initial vector
            vec = get_vector()
            
            # Updater to dynamically adjust vector direction and magnitude
            def update_vector(mob):
                new_vec = get_vector()
                mob.put_start_and_end_on(new_vec.get_start(), new_vec.get_end())

            vec.add_updater(update_vector)

    # Start animations

            # Medium Wind Field

            speed = 1 # Change this to make the fan spin faster or slower
            vec_magnitude = 5 # Change this to update the base size of the force vector to account for wind strength.
            # Add in all scene elements
            self.add(stream_lines_med, corner_cover1, corner_cover2)
            self.add(fan_base,fan_stand)
            self.add(vec)
            # Start the StreamLines animation bit
            # Flow speed determines how quickly the stream lines will move
            stream_lines_med.start_animation(warm_up=False, flow_speed=1.5)
            # Wait a moment until moving on
            self.wait(3)
            self.play(kite.animate.move_to(RIGHT*2+DOWN*1), run_time=3)
            self.play(kite.animate.move_to(LEFT*2+UP*1), run_time = 3)

            # Slow Wind field
            speed = 0.5
            vec_magnitude = 2
            self.remove(stream_lines_med)
            self.add(stream_lines_slow,fan)
            self.add(corner_cover1, corner_cover2)
            self.add(fan_base,fan_stand, fan)
            stream_lines_slow.start_animation(warm_up=False, flow_speed=.5)
            self.wait(3)

            # Fast Wind field
            speed = 2.0
            vec_magnitude = 8
            self.remove(stream_lines_slow)
            self.add(stream_lines_fast,fan)
            self.add(corner_cover1, corner_cover2)
            self.add(fan_base,fan_stand)
            stream_lines_fast.start_animation(warm_up=False, flow_speed=3.5)
            self.wait(3)

# Fan and vector field
class vectorField(Scene):
    def construct(self):
    # Here, we make the fan object.

            #Create the Fan VGroup
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
            blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=fan_center.get_center())
            blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=fan_center.get_center())

            # Group the blades and center
            fan_blades = VGroup(blade1, blade2, blade3)
            fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3)

            self.play(FadeIn(fan))

        # Create a line of large arrows on the left side of the fan
            left_arrows = VGroup()
            left_num_arrows = 6
            right_num_arrows = 2
            arrow_length = 1
            spacing = arrow_length + 0.5  # Adjust spacing based on arrow size
            for i in range(left_num_arrows):
                start_point = LEFT * (i * spacing) + fan_center.get_center() + LEFT * 1.5 # Position on the left
                end_point = start_point + LEFT * arrow_length
                arrow = Arrow(start=start_point, end=end_point, color=GREEN).scale(2)
                left_arrows.add(arrow)

        # Create a line of large arrows on the right side of the fan
            right_arrows = VGroup()
            for i in range(right_num_arrows):
                start_point = RIGHT * (i * spacing) + fan_center.get_center() + RIGHT * 2.35  # Position on the right
                end_point = start_point + LEFT * arrow_length
                arrow = Arrow(start=start_point, end=end_point, color=GREEN).scale(2)
                right_arrows.add(arrow)

        # Create a ring of arrows centered above the fan
            up_arrows = VGroup()
            num_arrows = 10  # Number of arrows in the ring
            radius = 4  # Radius of the ring
            for i in range(num_arrows):
                if i == 8: # Skips creating the 8th arrow (the one inside the fan)
                    continue
                angle = i * TAU / num_arrows
                start_point = np.array([radius * np.cos(angle), radius * np.sin(angle), 0]) + fan_center.get_center() + UP * radius
                end_point = np.array([radius * np.cos(angle - PI/6), radius * np.sin(angle - PI/6), 0]) + fan_center.get_center() + UP * radius
                arrow = Arrow(start=start_point, end=end_point, color=GREEN).scale(0.65)
                up_arrows.add(arrow)

        # Create a ring of arrows centered below the fan
            down_arrows = VGroup()
            for i in range(num_arrows):
                if i == 2: # Skipping the arrow in the fan
                    continue
                angle = i * TAU / num_arrows
                start_point = np.array([radius * np.cos(angle), radius * np.sin(angle), 0]) + fan_center.get_center() + DOWN * radius
                end_point = np.array([radius * np.cos(angle + PI/6), radius * np.sin(angle + PI/6), 0]) + fan_center.get_center() + DOWN * radius
                arrow = Arrow(start=start_point, end=end_point, color=GREEN).scale(0.65)
                down_arrows.add(arrow)

            #Create arrow Vgroup for them all to play at once
            all_arrows = VGroup(left_arrows, right_arrows)
            self.play(FadeIn(all_arrows,
                            up_arrows,
                            down_arrows
            ))
            

            self.wait(2.5)
            
    # Start grabbing the position to put the kite at
            left_arrow_kite = left_arrows[3]
            right_arrow_kite = right_arrows[1]
            up_arrow_kite = up_arrows[6]
            
            # Create the kites and move them to their respective arrows
            left_kite = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).move_to(left_arrow_kite.get_center())
            
            right_kite = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).move_to(right_arrow_kite.get_center())
            
            up_kite = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).move_to(up_arrow_kite.get_center())
            
        # Add arrows to the kites
            left_kite_arrow = Arrow(start=left_kite.get_center(), end=left_kite.get_center() + LEFT * 2, color=YELLOW, stroke_width=6)
            right_kite_arrow = Arrow(start=right_kite.get_center(), end=right_kite.get_center() + LEFT * 2, color=YELLOW, stroke_width=6)
            up_kite_arrow = Arrow(start=up_kite.get_center(), end=up_kite.get_center() + UP * 1.5 + LEFT * 0.5, color=YELLOW, stroke_width=6)

        # Create VGroups for each kite and arrow
            left_kite_group = VGroup(left_kite, left_kite_arrow)
            right_kite_group = VGroup(right_kite, right_kite_arrow)
            up_kite_group = VGroup(up_kite, up_kite_arrow)

        # Animate the VGroups
            self.play(FadeIn(left_kite_group, right_kite_group, up_kite_group))

            self.wait(2.5)
