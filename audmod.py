from pygame import *
class audiopiece:
    mixer.init()
    def __init__(self,name):
        self.name=name
        mixer.music.load(name)
        self.l=mixer.Sound(name).get_length()
        self.relpos=0.0
        mixer.music.play()
    def done(self):
        return not mixer.music.get_busy
    def pause(self):
        mixer.music.pause()
    def resume(self):
        mixer.music.unpause()
    def stop(self):
        mixer.music.stop()
        mixer.music.unload()
