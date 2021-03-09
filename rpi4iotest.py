#!/usr/bin/python3

import tkinter as tk

def exitApp():
    import sys
    sys.exit()
    
def executeApp():
    pass

root = tk.Tk()
root.title('Raspberry pi IO Test v0.1a')
root.geometry('400x200+700+400')
button1 = tk.Button(root, text = 'Exit', command = exitApp)
button1.grid(row = 3, column = 1, sticky = tk.W)
button2 = tk.Button(root, text = 'Execute', command = executeApp)
button2.grid(row = 2, column = 1, sticky = tk.W)

# main loop

root.mainloop()

