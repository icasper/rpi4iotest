import gpiozero
from tkinter import *

class Raspiio:
    def __init__(self, win):
        self.button1 = Button(win,text='Exit',command=self.exitNow)
        self.button1.place(x = 165, y = 250)
        
    def exitNow(self):
        import sys
        sys.exit()
        

root=Tk()
raspiio=Raspiio(root)
root.title('Raspberry Pi I/O')
root.geometry("400x300+700+300")
root.mainloop()