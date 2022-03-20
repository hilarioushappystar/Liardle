# try another driver

from tkinter import *  

import tkinter as tk
import os.path
from gamestate import Gamestate
import copy
import numpy as np
import time 

class UI:
    def __init__(self, parent):
        
        parent.title('LIARDLE')
        parent.geometry('1000x700')
        frame = tk.Frame(parent)
        frame.pack()
        
        self.gs = Gamestate()
        self.gs.init()

        self.canvas = tk.Canvas(parent, width=1000, height=700, bg = '#afeeee')
        self.name_label = tk.Label(parent, text = 'Guess', font=('calibre',10, 'bold'))
        self.canvas.create_window(100, 30, window=self.name_label)
        self.entry1 = tk.Entry(parent) 
        self.canvas.create_window(200, 30, window=self.entry1)
        self.gameover = False
       
        self.canvas.pack()
        self.button1 = tk.Button(frame,
                   text="SUBMIT GUESS",
                   command=self.submit_guess)
        self.button1.pack(side=tk.LEFT)

        self.button2 = tk.Button(frame,
                   text="NEW GAME",
                   command=self.new_game)
        self.button2.pack(side=tk.LEFT)      
      
       
        self.button5 = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
        self.button5.pack(side=tk.LEFT)

    # read the current gamestate and display the information to screen
    def submit_guess(self):        
        if( self.gameover):
            return 
        mystr = self.entry1.get()    
      
        self.gs.add_guess(mystr)
        
        # now print the game state to the canvas 
        self.images = []
        for foo in range (len(self.gs.guesses)):
            theguess = self.gs.guesses[foo]
            self.canvas.create_text(100,100 + 50 * foo,text=theguess,fill='blue',font='Courier 22',tag='some_tag')
      
            colours = self.gs.results[foo] 
            for bar in range(5):
                file = 'IMAGES\\black_blob.png'
                if(colours[bar] == 'g'):
                    file = 'IMAGES\\green_blob.png'
                if(colours[bar] == 'y'):
                    file = 'IMAGES\\yellow_blob.png'
        
                self.images.append( PhotoImage(file=file))
                self.canvas.create_image(200 + 40*bar,100 + 50 * foo, anchor=tk.CENTER, image=self.images[-1],tag='some_tag')

            if(theguess == self.gs.targetword):
                self.images.append( PhotoImage(file='IMAGES\\victory_image.png'))
                self.canvas.create_image(600,300,image=self.images[-1],tag='some_tag')
                self.gameover = True

        if( len(self.gs.guesses) >= 10 and (theguess != self.gs.targetword)):
            self.images.append( PhotoImage(file='IMAGES\\defeat_image.png'))
            self.canvas.create_image(600,300,image=self.images[-1],tag='some_tag')
            print('THE TARGET WORD WAS', self.gs.targetword)
            self.gameover=True
        
    def new_game(self):
        self.gs.init()
        self.canvas.delete("some_tag")
        self.gameover=False
   

if __name__ == "__main__":
    root = tk.Tk()
    ui = UI(root)
    root.mainloop()