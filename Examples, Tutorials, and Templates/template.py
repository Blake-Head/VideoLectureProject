from manim import *   # This line imports the entire manim library, allows manim functions to be called.

class SCENE_NAME(Scene): # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self): # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
            
            # Define a circle and a square, then draw them to the screen
            circ = Circle() # Make a Circle called "circ"
            sqr = Square() # Make a Square called "sqr"

            self.play(Create(circ)) # Use the animation "Create" to put circ on the screen
            self.play(FadeIn(sqr)) # Use the animation "FadeIn" to put sqr on the screen

            self.wait(3) # Make the animation wait 3 secons before ending

# To render this scence and watch it, run the following in the command line:

# manim -pql template.py SCENE_NAME

# Here's what that command does:
#   'manim' says "use the manim function with the following parameters"
#   '-pql' these are flags for the manim function. 'p' means "open the mp4 file after rendering", 'ql' means "quality low" meaning it will render the video at low quality.  Good for testing.
#   "template.py" is the same of the python script where your scene is
#   "SCENE_NAME" the individual scence you want to be rendered inside the python file you just called. 
# 
# Inside the folder where your python script is saved, you will see now that 2 new folders have been created: "__pycache__" and "media".  
# The pycache folder caches animations to make rendering faster.
# The media folder is where all the mp4's and pngs rendered from your scenes will be stored. If you want to watch a video you've already rendered, you will find it here.  
    # The file name for the movie will name named after whatever you named the scene. 