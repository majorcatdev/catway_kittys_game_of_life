from tkinter import *
from tkinter import ttk
import tkinter as tk
from random import randint


root = tk.Tk()
WIDTH=800
HEIGHT=600
TILESIZE=32
keysDown={}
RUNNING=True
AWAKECAT = tk.PhotoImage(file='cat1.png')
ASLEEPCAT= tk.PhotoImage(file='cat2.png')


def randbool():
    if(randint(0,1)==1):
        return True
    return False


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

class Tile:
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
        self.awake=False
    def draw(self):
        if(self.awake):
            canvas.create_image((self.x*self.size+self.size/2, self.y*self.size+self.size/2+1),image=AWAKECAT)
        else:
            canvas.create_image((self.x*self.size+self.size/2, self.y*self.size+self.size/2+1),image=ASLEEPCAT)
    
def makeGrid():
    grid=[]
    for y in range((HEIGHT//TILESIZE)):
        temp=[]
        for x in range((WIDTH//TILESIZE)):
            temp.append(Tile(x,y,TILESIZE))
        grid.append(temp)
    return grid
grid=makeGrid()

def render(grid):
    canvas.create_rectangle((0, 0), (WIDTH, HEIGHT), fill='white')
    for y in grid:
        for x in y:
            x.draw()

render(grid)


while RUNNING:
    #put main loop here


    root.update_idletasks()
    root.update()
    if(not RUNNING):
        root.destroy()