import tkinter as tk

class Raspiio(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500+700+400')
        self.title('Raspberry Pi I/O v0.1a')
        
raspiio = Raspiio()
raspiio.mainloop()