import tkinter as tk
 
window_main = tk.Tk()
window_main.geometry("400x200")
 
frame_1 = tk.Frame(window_main, bg='blue', width=200, height=200)
frame_1.pack(side='left')
frame_1.pack_propagate(0)
label = tk.Label(frame_1,text='hello', bg='blue',fg='yellow')
label.place(x=0,y=0)

