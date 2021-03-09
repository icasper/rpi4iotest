#!/usr/bin/python3

import tkinter as tk

def exitApp():
    import sys
    sys.exit()

root = tk.Tk()
root.title('Raspberry pi IO Test v0.1a')
root.geometry('400x200+700+400')
button1 = tk.Button(root, text = 'Exit', command = exitApp)
button1.pack()

# main loop

root.mainloop()

