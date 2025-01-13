from tkinter import *
from tkinter import Tk, Button
import pygame

window = Tk()
window.title("Cat Clicker")
window.geometry('600x600')
window.resizable(False, False)

bg = PhotoImage(file="fon.png")
bg2 = PhotoImage(file='fon1.png')

#audio_system = winsound.PlaySound("bg_sound.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

# Create Canvas
canvas = Canvas(window, width=600, height=600)
canvas.pack(fill="both", expand=True)

# Display image
canvas.create_image(0, 0, image=bg,
                     anchor="nw")

start_img = PhotoImage(file = 'start_btn1.png')
start_img2 = PhotoImage(file = 'start_btn2.png')

sound_file = "bg_sound.mp3"

def play_bg_sound(sound_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)  # -1 означает зацикленное воспроизведение
def stop_bg_sound():
    pygame.mixer.music.stop()


def bg_anim():
    if canvas['image'] == bg:
        canvas['image'] = bg2
    canvas.after(800, bg_animation)

def start_button_press(event):
    start_button.config(image=start_img2)
def start_button_release(event):
    start_button.config(image=start_img)

current_img = 0
def bg_animation():
    global current_img

    if current_img == 0:
        canvas.itemconfig(image_on_canvas, image = bg2)
        current_img = 1
    else:
        canvas.itemconfig(image_on_canvas, image=bg)
        current_img = 0

    # Планируем следующий переключатель изображения через 500 миллисекунд
    canvas.after(500, bg_animation)


start_button = Button(canvas, width=320, height=96,
                      image = start_img,
                      command = lambda: (play_bg_sound(sound_file)),
                      borderwidth=0,
                      highlightthickness=0)
start_button.bind("<Button-1>", start_button_press)
start_button.bind("<ButtonRelease-1>", start_button_release)
start_button.place(x = 140, y = 252)


image_on_canvas = canvas.create_image(0, 0, image=bg,
                     anchor="nw")

bg_animation()

window.mainloop()