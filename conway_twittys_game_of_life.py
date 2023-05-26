from tkinter import *
from tkinter import ttk
import tkinter as tk
from random import randint


root = tk.Tk()
WIDTH=840
HEIGHT=680
TILESIZE=16
keysDown={}
RUNNING=True


root.geometry(str(WIDTH)+'x'+str(HEIGHT))
root.title('conway twitty\'s game of life')

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)


#widget.bind(event, handler, add=None)

def keyDown(event):
    keysDown[event]=True

def keyUp(event):
    keysDown[event]=False

def window_exit():
    global RUNNING
    RUNNING=False


root.bind("<KeyPress>",keyDown)
root.bind("<KeyRelease>",keyUp)
root.protocol("WM_DELETE_WINDOW", window_exit)



while RUNNING:
    #put main loop here


    root.update_idletasks()
    root.update()
    if(not RUNNING):
        root.destroy()