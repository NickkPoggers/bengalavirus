import tkinter as tk
from PIL import Image, ImageTk
from plyer import notification
import pygame



def jumpscare():
    jumpscareWindow = tk.Tk()
    jumpscareWindow.attributes("-fullscreen", True)


    kidImgPIL = Image.open("assets/bengalajumpscareimg.jpg")
    kidImgPIL = kidImgPIL.resize((jumpscareWindow.winfo_screenwidth(), jumpscareWindow.winfo_screenheight()))
    kidImg = ImageTk.PhotoImage(kidImgPIL)
    labelImg = tk.Label(jumpscareWindow, image=kidImg)
    labelImg.pack()

    pygame.init()
    pygame.mixer.init
    pygame.mixer.music.load("assets/KidJumpscareSound.mp3")
    pygame.mixer.music.play()

    jumpscareWindow.after(1000, jumpscareWindow.destroy)
    jumpscareWindow.mainloop()

def floatingWindow():
    window = tk.Tk()

def notifications():
    print(0)
    notification.notify(
        title="teste",
        message="teste2"
    )
