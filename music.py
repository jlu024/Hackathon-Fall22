import pygame
import os

MAIN_SONG = '8 - Regalia - The Worlds of Time.mid'

def load():
    music_path = os.path.join("music", MAIN_SONG)
    pygame.mixer.music.load(music_path)




def play(music_name):
    pygame.mixer.music.play()
