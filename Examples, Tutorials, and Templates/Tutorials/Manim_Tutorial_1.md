Here I am attempting to write a step-by-step basic tutorial for how manim animations are set up, manipulated, and called.  This is based on how I (Blake) understand the system as of late 2024.  More than likely, my process is not the most efficient, but should get us going.

I am writing this in a Jupyter notebook, which is just a file that can contain multiple blocks of different code and words (like here).  I think you should be able to open this and run chunks of code locally within the notebook.  This way, you don't need to set up extra bits of computer environment to test and learn the basics of Manim.

The first block just below this is a starter command that (I think) just checks your system to ensure you actually have manim installed.  If you don't have manim installed, this block will show an error below, saying something to the effect of "No moudle named `manim' ".  If you have manim, nothing notable should happen here.

This also shows you how we will always be loading in the manim library.  This is all done in Python, with manim just being a library of tools within python.  The * symbol means "Take every single tool from the manim box out".  Sometimes, it's more efficient to only import the tools you know you'll be using rather than the entire library, but manim is small enough that we don't care. 

```python
  from manim import *
   
  config.media_width = "75%"
  config.verbosity = "WARNING"
```

Now we begin building our scene.

In manim, all animations are generated in a class called "Scene".  Inside this scence, we will build all objects (colors, sizes, locations) and how they move (or don't move) on the screen via animations. 

All manim scripts will begin with the following:

```python
from manim import *

class SCENE_NAME(Scene):
    def construct(self):
```

Note the the top line in the block below (%%manim -qh SCENE_NAME) is only relevant here in the Jupyter notebook.  You won't be putting this line in your python script.

These first three lines set up our template, but of course, there's nothing there yet.

Let's add something.  Here, I've made a variable named "a_circle".  I can make that variable be equal to whatever I want, but here I've set it equal to a Manim object called "Circle", which is a function within manim that will create a circle of a default width, color, line stroke, and position. 

Let's run this and see what happens. 

```python
%%manim -qh SCENE_NAME1

from manim import *

class SCENE_NAME1(Scene):        # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self):        # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
        a_circle = Circle()     # Define a variable called "a_circle", which will be the MObject "Circle".  Currently, no paramenters are passed to the Circle function. 
```

![SCENE_NAME1@2024-10-15@22-51-10](https://github.com/user-attachments/assets/8ef2182f-0c53-4f77-b10f-5de1b8bc25a4)

Running this, nothing happens.  That's because we've only defined what our variable, "circle", is.  We haven't actually told the program to do anything with it.  

Let's now tell the program to actually ANIMATE the circle onto the scene. 

Here, we've added the line "self.play(Create(circle))" to the end.  

This command tells the program to play a certain type of animation, which in this case is the "Create" animation.  What thing do we want to create? The circle. 

```python
%%manim -qh SCENE_NAME2

from manim import *

class SCENE_NAME2(Scene):        # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self):        # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
        a_circle = Circle()     # Define a variable called "a_circle", which will be the MObject "Circle".  Currently, no paramenters are passed to the Circle function. 

        self.play(Create(a_circle))     # Animate the circle onto the screen using the "Create" animation
```




https://github.com/user-attachments/assets/2eea5e49-8b17-4200-9d44-0f9d4043d348

Hey look, we've made our first manim animation.  We can also see what the default parameters for the "Circle" Mobject are. 

Let's now add some more things to the scene.  Suppose we want to now add a square.  First we need to define a new variable that will be our square, and then tell manim to put it on the screen. I'll use a new kind of animation called "FadeIn", which does probably what you think it does. 

```python
%%manim -qh SCENE_NAME3

from manim import *

class SCENE_NAME3(Scene):        # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self):        # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
        a_circle = Circle()     # Define a variable called "a_circle", which will be the MObject "Circle".  Currently, no paramenters are passed to the Circle function. 

        self.play(Create(a_circle))     # Animate the circle onto the screen using the "Create" animation

        a_square = Square()     # Define a variable called "a_square" which will be the Mobject "Square"

        self.play(FadeIn(a_square))     # Animate the square onto the screen using the "FadeIn" animation

```


https://github.com/user-attachments/assets/25f10517-bf72-4642-8be6-266380392f64

So hopefully you can see from here, in order to make objects appear on the screen, we first must define what those objects are.  Then, we pass those objects to some sort of animation function, which will display the object. 

From here, I would suggest that you play around with the scence briefly.  Define 1 or 2 new variables, and have them be drawn to the screen. 

```python
%%manim -qh SCENE_NAME4

from manim import *

class SCENE_NAME4(Scene):            # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self):            # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
        a_circle = Circle()         # Define a variable called "a_circle", which will be the MObject "Circle".  Currently, no paramenters are passed to the Circle function. 

        self.play(Create(a_circle)) # Animate the circle onto the screen using the "Create" animation
        self.play(FadeOut(a_circle)) # Fade the a_circle object out

        a_square = Square()         # Define a variable called "a_square" which will be the Mobject "Square"

        self.play(FadeIn(a_square)) # Animate the square onto the screen using the "FadeIn" animation

        blue_circle = (             # Define a blue_circle, which is a circle with a blue border, and is filled with blue.
            Circle(                 # Sometimes, a function might take in several arguments, and it's notationally convienent to write the function this way for easy reading.  
                fill_color = BLUE,  # This will make the fill color BLUE.  Defeault is NULL
                fill_opacity = 0.3, # This will set the opacity. Default is 0.0
                color = BLUE,       # This will set the border color. Default is RED
                radius=2)           # This will set the radius.  Default is 1
         )                          # There are other attributes you can set as well.  Attributes all have default values they take on unless you change them. 

         # Below is the exact same thing as above, just all written to one line.  You can choose whichever you prefer. 

    # blue_circle = (Circle(fill_color = BLUE, fill_opacity = 0.3, color = BLUE, radius=2))



        self.play(Transform(a_square, blue_circle))  # This is a cool animation.  It will transfrom the first argument into the second argument. 

        self.wait(3)                # Force the movie to freeze for 3 seconds.
```



https://github.com/user-attachments/assets/5f8e269e-c91c-4d2d-bf10-beb7afe76b87

In that last piece, I've also introduced the possibility of adding arguments to the functions.  For the shape functions (such as Circle() and Square()) we can ask manim do make those shapes look a certain way.  By default, the Circle() command creates a red circle with no fill color, with a radius of 1, located at the center of the scence. You should play around with the function arguments for blue_circle and see what other circles you can.  Also try with the a_square object!

From a grand perspective, this is all manim is.  Making objects, then specifying where those objects should appear, and HOW they should appear. 

Let's complete the basics by having these objects move around.  I'm going to alter our code above so that all three objects are on the screen at once.

```python
%%manim -qh SCENE_NAME5

from manim import *

class SCENE_NAME5(Scene):            # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self):            # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
        a_circle = Circle()         # Define a variable called "a_circle", which will be the MObject "Circle".  Currently, no paramenters are passed to the Circle function. 

        a_square = Square()         # Define a variable called "a_square" which will be the Mobject "Square"

        blue_circle = (             # Define a blue_circle, which is a circle with a blue border, and is filled with blue.
            Circle(                 # Sometimes, a function might take in several arguments, and it's notationally convienent to write the function this way for easy reading.  
                fill_color = BLUE,  # This will make the fill color BLUE.  Defeault is NULL
                fill_opacity = 0.3, # This will set the opacity. Default is 0.0
                color = BLUE,       # This will set the border color. Default is RED
                radius=2)           # This will set the radius.  Default is 1
         )                          # There are other attributes you can set as well.  Attributes all have default values they take on unless you change them. 

         # Below is the exact same thing as above, just all written to one line.  You can choose whichever you prefer. 

    # blue_circle = (Circle(fill_color = BLUE, fill_opacity = 0.3, color = BLUE, radius=2))

        self.play(FadeIn(a_circle, a_square, blue_circle))


        self.wait(3)                # Force the movie to freeze for 3 seconds.
```




https://github.com/user-attachments/assets/3818ff18-1e68-4c20-922d-0c18486e90b4

Note that I was able to call all three objects with a single animation function, I just had to separate each object with a comma. 

Maybe we want these object to appear in three different locations.  There are a few ways to do that.  First, let's use some of the built in functions.

Let's say we want the big blue circle to appear in the lower right corner of the screen, the small red circle to appear in the top of the frame, and the square to appear at the far left side. 

```python
%%manim -qh SCENE_NAME6

from manim import *

class SCENE_NAME6(Scene):            # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self):            # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
        a_circle = Circle().to_edge(UP)         # Define a variable called "a_circle", which will be the MObject "Circle".  Currently, no paramenters are passed to the Circle function. 

        a_square = Square().to_edge(LEFT)         # Define a variable called "a_square" which will be the Mobject "Square"

        blue_circle = (             # Define a blue_circle, which is a circle with a blue border, and is filled with blue.
            Circle(                 # Sometimes, a function might take in several arguments, and it's notationally convienent to write the function this way for easy reading.  
                fill_color = BLUE,  # This will make the fill color BLUE.  Defeault is NULL
                fill_opacity = 0.3, # This will set the opacity. Default is 0.0
                color = BLUE,       # This will set the border color. Default is RED
                radius=2).to_corner(DR)           # This will set the radius.  Default is 1
         )                          # There are other attributes you can set as well.  Attributes all have default values they take on unless you change them. 

         # Below is the exact same thing as above, just all written to one line.  You can choose whichever you prefer. 

    # blue_circle = (Circle(fill_color = BLUE, fill_opacity = 0.3, color = BLUE, radius=2))

        self.play(FadeIn(a_circle, a_square, blue_circle))


        self.wait(3)                # Force the movie to freeze for 3 seconds.
```



https://github.com/user-attachments/assets/4360b16e-46e2-43b8-a5aa-ac69d6c0c6e6

Note that at the end of each variable definition, we've added one of the following commands:

```python
.to_edge()
.to_corner()
```

The arguments to_edge and to_corner do what it sounds like.  They will tell an object to go to a particular location.  For to_edge, the argument can be UP, DOWN, LEFT, or RIGHT.  For to_corner, the options are UL (upper left), UR (upper right), DL (down left) DR (down right). 

We can also use the `shift' command in place of the edge/corner command.  Shift is used when you want to be very specific about where you want the object.  Edge/Corner is great if you want objects in those general areas.

```python
%%manim -qh SCENE_NAME7

from manim import *

class SCENE_NAME7(Scene):            # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self):            # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
        a_circle = Circle().shift(UP*2)        # Define a variable called "a_circle", which will be the MObject "Circle".  Currently, no paramenters are passed to the Circle function. 

        a_square = Square().shift(DOWN*2+RIGHT*2)       # Define a variable called "a_square" which will be the Mobject "Square"

        blue_circle = (             # Define a blue_circle, which is a circle with a blue border, and is filled with blue.
            Circle(                 # Sometimes, a function might take in several arguments, and it's notationally convienent to write the function this way for easy reading.  
                fill_color = BLUE,  # This will make the fill color BLUE.  Defeault is NULL
                fill_opacity = 0.3, # This will set the opacity. Default is 0.0
                color = BLUE,       # This will set the border color. Default is RED
                radius=2).shift(LEFT*2)           # This will set the radius.  Default is 1
         )                          # There are other attributes you can set as well.  Attributes all have default values they take on unless you change them. 

         # Below is the exact same thing as above, just all written to one line.  You can choose whichever you prefer. 

    # blue_circle = (Circle(fill_color = BLUE, fill_opacity = 0.3, color = BLUE, radius=2))

        self.play(FadeIn(a_circle, a_square, blue_circle))


        self.wait(3)                # Force the movie to freeze for 3 seconds.
```



https://github.com/user-attachments/assets/55271df7-76bc-4554-b099-c9e1da5999ca


Notice that for .shift(), you specify how many units left/right and up/down you want the object to be shifted by.  

So this is all well and good.  We can make objects, set their color and size, then then place them onto the screen with one of several different kinds of animations. Lastly, let's see how we can make our objects move AFTER they are already drawn onto the screen.  Since this is a sort of animation, this kind of command will be attached to the self.play() enviroment, the same place we called our animations earlier. 

Here, I will use the .animate() function.

```python
%%manim -qh SCENE_NAME8

from manim import *

class SCENE_NAME8(Scene):            # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self):            # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
        a_circle = Circle().to_edge(UP)         # Define a variable called "a_circle", which will be the MObject "Circle".  Currently, no paramenters are passed to the Circle function. 

        a_square = Square().to_edge(LEFT)         # Define a variable called "a_square" which will be the Mobject "Square"

        blue_circle = (             # Define a blue_circle, which is a circle with a blue border, and is filled with blue.
            Circle(                 # Sometimes, a function might take in several arguments, and it's notationally convienent to write the function this way for easy reading.  
                fill_color = BLUE,  # This will make the fill color BLUE.  Defeault is NULL
                fill_opacity = 0.3, # This will set the opacity. Default is 0.0
                color = BLUE,       # This will set the border color. Default is RED
                radius=2).to_corner(DR)           # This will set the radius.  Default is 1
         )                          # There are other attributes you can set as well.  Attributes all have default values they take on unless you change them. 

         # Below is the exact same thing as above, just all written to one line.  You can choose whichever you prefer. 

    # blue_circle = (Circle(fill_color = BLUE, fill_opacity = 0.3, color = BLUE, radius=2))

        self.play(FadeIn(a_circle, a_square, blue_circle))

        self.play(a_circle.animate.to_corner(UL))           # Animate the circle, send it to upper left corner
        self.play(a_square.animate.to_edge(UP))             # Animate the square, send it to the top edge (will go straight up)
        self.play(blue_circle.animate.shift(UP*3 + LEFT*3)) # Animate the blue circle, shift it up by 3, left by 3


        self.wait(3)                # Force the movie to freeze for 3 seconds.
```





https://github.com/user-attachments/assets/5b9552e4-fab2-4622-b254-073b37f34214

The way we've written the animations is one after another in the code.  If we want them to happen simoultaneously, then they must be called in the same self.play function:

```python
%%manim -qh SCENE_NAME9

from manim import *

class SCENE_NAME9(Scene):            # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self):            # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
        a_circle = Circle().to_edge(UP)         # Define a variable called "a_circle", which will be the MObject "Circle".  Currently, no paramenters are passed to the Circle function. 

        a_square = Square().to_edge(LEFT)         # Define a variable called "a_square" which will be the Mobject "Square"

        blue_circle = (             # Define a blue_circle, which is a circle with a blue border, and is filled with blue.
            Circle(                 # Sometimes, a function might take in several arguments, and it's notationally convienent to write the function this way for easy reading.  
                fill_color = BLUE,  # This will make the fill color BLUE.  Defeault is NULL
                fill_opacity = 0.3, # This will set the opacity. Default is 0.0
                color = BLUE,       # This will set the border color. Default is RED
                radius=2).to_corner(DR)           # This will set the radius.  Default is 1
         )                          # There are other attributes you can set as well.  Attributes all have default values they take on unless you change them. 

         # Below is the exact same thing as above, just all written to one line.  You can choose whichever you prefer. 

    # blue_circle = (Circle(fill_color = BLUE, fill_opacity = 0.3, color = BLUE, radius=2))

        self.play(FadeIn(a_circle, a_square, blue_circle))

        self.play(a_circle.animate.to_corner(UL),a_square.animate.to_edge(UP),blue_circle.animate.shift(UP*3 + LEFT*3)) 


        self.wait(3)                # Force the movie to freeze for 3 seconds.
```



https://github.com/user-attachments/assets/86b93b31-d4f9-41de-991f-5b2f02e083f8

And I think that's enough of the very basic stuff.  I get yourself familiar with how to work with manim, I would reccomend that you make your own script with your own objects and animations.  I'd also highly reccommend you visit the manim community page to get a comprehensive list of animations and MObjects that you can play with!









