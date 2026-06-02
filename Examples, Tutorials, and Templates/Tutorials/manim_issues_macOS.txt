(Last Updated October 13, 2024)

I work primarily on my macbook, and when attempting to install manim via the terminal, you would typically use the following command:

> pip install manim

However, I ran into an issue on the newer version of macOS where something about "externally managed" something preventing manim from being installed.  I believe this is some sort of security feature. The get around this issue and install manim, I needed the create a "virtual enviroment" within my terminal, which would allow me to install manim.  The process is detailed below:

1. Create a directory where your manim project will live, be created, and be rendered from.  
2. In the terminal, navigate to that directory.
3. Run the following command the create a virtual enviroment in that directory: "python3 -m venv .py3env --prompt=manim-env"
4. Once that runs, you can run "ls -a" to ensure the hidden file .py3env exists.
5. To activate the virtual enviroment, run the following command: "source .py3env/bin/activate"
    -note: you could probably make an alias for this command if it's something that needs to be done very often. 
6. At this step, you should be able to (if you've not done so already) install Manim with the following command: "pip install manim"
    -note: This assumes you have "pip" installed.  This is a python package installer, very useful to have for mac. 
7. Once you are inside the virtual enviroment, you should be able to render and manipulate manim files, and execute manim commands from the command line. This is primarily used for rendering the animations in 4k once everything is ready to go. 

Since this seems to be an issue tied up with the operating system, I expect this process to not work sometime in the future.  If this happens and you figure out what needs to be changed, please add those updates here. 
