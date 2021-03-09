#!/usr/bin/python3

import gpiozero
from tkinter import *

class Raspiio:
    def __init__(self, win):
        self.var = IntVar()
        self.button1 = Button(win,text='Exit',relief=SUNKEN, command=self.exitNow)
        self.button1.place(x = 165, y = 250)
        self.r1 = Radiobutton(win,text='Red LED', variable=self.var, value=1, command=self.rl)
        self.r2 = Radiobutton(win,text='Green LED', variable=self.var, value=2, command=self.rl)
        self.r3 = Radiobutton(win,text='Blue LED',variable=self.var, value=3, command=self.rl) 
        self.r1.place(x=10,y=10)
        self.r2.place(x=10,y=30)
        self.r3.place(x=10,y=50)
        self.label = Label(win)
        self.label.pack(side='bottom')
        
        
    def rl(self):
       selection = "You selected the option " + str(self.var.get())
       self.label.config(text = selection)
        
        
    def exitNow(self):
        import sys
        sys.exit()
        

root=Tk()
raspiio=Raspiio(root)
root.title('Raspberry Pi I/O v0.1a')
root.geometry("400x300+700+300")
root.mainloop()
