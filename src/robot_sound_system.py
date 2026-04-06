from utils.sound import Sound, Song
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import threading
import time
import simpleaudio

# CONSTANTS

# -------------------- FUNCTIONS --------------------
def victory_jingle():
    song = simpleaudio.WaveObject.from_wave_file("Samsung_washing_machine.wav")
    song.play()
    time.sleep(24)



def task_jingle():
    sounds = [B5_COIN, E6_COIN]
    song = Song(sounds)
    song.compile()
    song.play()
    song.wait_done()


if __name__ == "__main__":
    victory_jingle()
    task_jingle()