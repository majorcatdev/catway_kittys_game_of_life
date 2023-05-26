from tkinter import ttk
import tkinter as tk
from random import randint


#to advance to the next generation press enter, to make generations go brrrrrr, press space

root = tk.Tk()
WIDTH=1280
HEIGHT=800
TILESIZE=32
keyState=False
RUNNING=True
BGCOLOR="#5e5e5d"
AWAKECAT = tk.PhotoImage(file='cat1.png')
ASLEEPCAT= tk.PhotoImage(file='cat2.png')
press=False
generation=1

def randbool():
    if(randint(0,1)==1):
        return True
    return False


root.geometry(str(WIDTH)+'x'+str(HEIGHT))
root.title('catway kitty\'s game of life')

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BGCOLOR)
canvas.pack(anchor=tk.CENTER, expand=True)
 

#widget.bind(event, handler, add=None)

def keyDown(event):
    if(event.keycode==13):
        global keyState
        keyState=True
    elif(event.keycode==32):
        global press
        press=True

def keyUp(event):
    if(event.keycode==13):
        global keyState
        keyState=False
    elif(event.keycode==32):
        global press
        press=False

def window_exit():
    global RUNNING
    RUNNING=False


root.bind("<KeyPress>",keyDown)
root.bind("<KeyRelease>",keyUp)
root.protocol("WM_DELETE_WINDOW", window_exit)



#should have thought to do this in lolcode
class Tile:
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
        self.awake=randbool()
    def draw(self):
        if(self.awake):
            canvas.create_image((self.x*self.size+self.size/2, self.y*self.size+self.size/2),image=AWAKECAT)
        else:
            canvas.create_image((self.x*self.size+self.size/2, self.y*self.size+self.size/2),image=ASLEEPCAT)
    
def makeGrid():
    grid=[]
    for y in range(1,(HEIGHT//TILESIZE)):
        temp=[]
        for x in range((WIDTH//TILESIZE)):
            temp.append(Tile(x,y,TILESIZE))
        grid.append(temp)


    return grid

grid=makeGrid()

def render(grid):
    canvas.delete("all")
    canvas.create_text((WIDTH-60, 18),text="generation: "+str(generation), fill="white",font='tkDefaeultFont 12')
    for y in grid:
        for x in y:
            x.draw()



def logic(grid):
    changes=[]
    for y in range(len(grid)-1):
        for x in range(len(grid[y])-1):
            awakeNeighbours=0
            if(y>0 and grid[y-1][x].awake):
                awakeNeighbours+=1
            if(y<len(grid)-1 and grid[y+1][x].awake):
                awakeNeighbours+=1
            if(x>0 and grid[y][x-1].awake):
                awakeNeighbours+=1
            if(x<len(grid[y])-1 and grid[y][x+1].awake):
                awakeNeighbours+=1


            if(y>0 and x>0 and grid[y-1][x-1].awake):
                awakeNeighbours+=1
            if(y>0 and x<len(grid[y])-1 and grid[y-1][x+1].awake):
                awakeNeighbours+=1
            if(y<len(grid) and x>0 and grid[y+1][x-1].awake):
                awakeNeighbours+=1
            if(y<len(grid) and x<len(grid[y]) and grid[y+1][x+1].awake):
                awakeNeighbours+=1


            if(grid[y][x].awake):
                if(awakeNeighbours<2):
                    changes.append((x,y,False))
                elif(awakeNeighbours>3):
                    changes.append((x,y,False))
            elif(awakeNeighbours==3):
                changes.append((x,y,True))
    for i in changes:
        grid[i[1]][i[0]].awake=i[2]

render(grid)

#though about making the grid easily ediable via the mouse, but decided against it after looking into how much work that would entail


while RUNNING:
    if(keyState):
        press=True
    if(press and not keyState):
        press=False
        generation+=1
        logic(grid)
        render(grid)
        
        


    root.update_idletasks()
    root.update()
    if(not RUNNING):
        root.destroy()