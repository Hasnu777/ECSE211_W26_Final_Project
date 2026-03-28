"""
Purpose of this file: testing of victory & task completion jingles, to be integrated later
"""


from utils.sound import Sound, Song
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import threading

# -------------------- CONSTANTS --------------------
VOLUME = 100

E6 = Sound(duration=0.3, pitch="E6", volume=VOLUME)
E6_HALF = Sound(duration=0.3, pitch="E6", volume=VOLUME)
E6_3HALVES = Sound(duration=0.45, pitch="E6", volume=VOLUME)
E6_3X = Sound(duration=0.9, pitch="E6", volume=VOLUME)
A7 = Sound(duration=0.3, pitch="A7", volume=VOLUME)
A7_HALF = Sound(duration=0.15, pitch="A7", volume=VOLUME)
A7_3X = Sound(duration=0.9, pitch="A7", volume=VOLUME)
A7_2X = Sound(duration=0.6, pitch="A7", volume=VOLUME)
C7 = Sound(duration=0.3, pitch="C#7", volume=VOLUME)
B7 = Sound(duration=0.3, pitch="B7", volume=VOLUME)
B7_HALF = Sound(duration=0.15, pitch="B7", volume=VOLUME)
G6 = Sound(duration=0.3, pitch="G#6", volume=VOLUME)
G6_HALF = Sound(duration=0.15, pitch="G#6", volume=VOLUME)
F6_HALF = Sound(duration=0.15, pitch="F#6", volume=VOLUME)
F6 = Sound(duration=0.3, pitch="F#6", volume=VOLUME)
D6 = Sound(duration=0.3, pitch="D#6", volume=VOLUME)
D7_HALF = Sound(duration=0.15, pitch="D#7", volume=VOLUME)

def victory_jingle():
    measure1 = [E6, A7, A7, C7, C7, A7_2X, E6, E6, E6_3HALVES, E6_HALF, B7_HALF, A7_HALF, G6_HALF, F6_HALF, E6_3X]
    measure2 = [E6, A7, A7, C7, C7, A7_2X, E6, A7, G6, F6_HALF, G6_HALF, A7, D6, E6_3X]
    measure3 = [E6, G6, G6, A7_HALF, G6_HALF, F6_HALF, G6_HALF, A7_2X, E6, A7, G6, G6, G6_HALF, D7_HALF, B7_HALF, G6_HALF, A7_3X]
    measure4 = [A7, F6, F6, F6, A7, A7_2X, E6, E6, E6_3HALVES, E6_HALF, B7, G6, A7_3X]
    measure5 = [A7, G6_HALF, F6_HALF, F6, F6_HALF, A7_HALF, G6_HALF, B7_HALF, A7_2X, E6, E6, E6_3HALVES, E6_HALF, B7, G6, A7_3X]
    song1 = Song(measure1)
    song2 = Song(measure2)
    song3 = Song(measure3)
    song4 = Song(measure4)
    song5 = Song(measure5)
    song1.compile 
    song2.compile
    song3.compile
    song4.compile
    song5.compile
    song1.play()
    song2.play()
    song3.play()
    song4.play()
    song5.play()

# def task_jingle():
#     sounds = [sound.Sound()]
#     song = sound.Song(sounds)
#     song.compile
#     song.play() 
if __name__ == "__main__":
#     tone1 = Sound(duration = 1.0, volume = 100, pitch="A3")
#     tone1.play()
    victory_jingle()