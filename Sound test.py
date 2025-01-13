from tkinter import *
import pygame

def play_bg_sound(sound_file):
    vol = 0
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(sound_file))
    pygame.mixer.music.play(-1)  # -1 означает зацикленное воспроизведение
    pygame.mixer.music.set_volume(vol)

def stop_bg_sound():
    pygame.mixer.Channel(0).stop()

def click_sound(sound_file):
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(sound_file))

root = Tk()
root.geometry('400x400')
root.title('Sound test')

bg_sound_file = 'bg_sound3.mp3'
click_file = 'multi_click.mp3'
start_btn = Button(root, text = 'Run music',
                   font = ('Arial', 16),
                   fg = 'black',
                   command = lambda: play_bg_sound(bg_sound_file))
start_btn.pack()

stop_btn = Button(root, text = 'Stop music',
                  font = ('Arial', 16),
                  fg = 'black',
                  command = stop_bg_sound)
stop_btn.pack()

click_sound_btn = Button(root, text = 'Click Me',
                         font = ('Arial', 16),
                         fg = 'black',
                         command = lambda: click_sound(click_file))
click_sound_btn.pack()

root.mainloop()





