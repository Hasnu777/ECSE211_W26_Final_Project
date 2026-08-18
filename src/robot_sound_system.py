from utils.sound import Sound, Song
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import threading
import time
import simpleaudio

# CONSTANTS
VOLUME = 70
B5_COIN = Sound(duration=0.1, pitch="B5", volume=VOLUME, amp_f = 5, amp_ka = 0.1, amp_ac = 0.9)  # Task Complete Note 1
E6_COIN = Sound(duration=0.3, pitch="E6", volume=VOLUME, amp_f = 5, amp_ka = 0.1, amp_ac = 0.9)  # Task Complete Note 2

# -------------------- FUNCTIONS --------------------
def victory_jingle():
    song = simpleaudio.WaveObject.from_wave_file("Samsung_washing_machine.wav")  # Local file holding the sound data
    song.play()
    time.sleep(24.5)



def task_jingle():
    sounds = [B5_COIN, E6_COIN]  # Compilation of the two notes for task complete notification
    song = Song(sounds)
    song.compile()
    song.play()
    song.wait_done()


if __name__ == "__main__":
    victory_jingle()
    task_jingle()