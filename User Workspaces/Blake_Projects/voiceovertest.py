from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService



class MyVoiceScene(VoiceoverScene):
    def construct(self):
        #self.set_speech_service(GTTSService())
        self.set_speech_service(RecorderService())
        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            circle = Circle(radius=2, color=BLUE)
            self.play(Create(circle), run_time=tracker.duration)

        with self.voiceover(text="This square is drawn as I speak.") as tracker:
            square = Square(side_length=2, color=RED)
            self.play(Create(square), run_time=tracker.duration)

        with self.voiceover(text="This triangle is drawn as I speak.") as tracker:
            triangle = Triangle(color=GREEN)
            self.play(Create(triangle), run_time=tracker.duration)