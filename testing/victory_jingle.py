from utils.sound import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import threading

def victory_jingle():
    sounds = [sound.Sound()]
    song = sound.Song(sounds)
    song.compile 
    song.play()

def task_jingle():
    sounds = [sound.Sound()]
    song = sound.Song(sounds)
    song.compile
    song.play() 

if __name__ == '__main__':
    task_jingle()
    victory_jingle()