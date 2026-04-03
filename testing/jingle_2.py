"""
Purpose of this file: testing of victory & task completion jingles, to be integrated later
"""


from utils.sound import Sound, Song
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import threading
import time
import simpleaudio

song = simpleaudio.WaveObject.from_wave_file("Samsung_washing_machine.wav")

def play_jingle():
    song.PlayObject()
    song.wait_done()

if __name__ == "__main__":
    play_jingle
    