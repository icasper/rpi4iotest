#!/usr/bin/python3
from tkinter import *
from gpiozero import LED

class Windows:
    
    def __init__(self, master):
        
        self.e=0
        self.led1 = LED(17)
        self.led2 = LED(27)
        self.led3 = LED(22)
        self.led4 = LED(10)
        master.title('A new window')
        master.geometry('430x300+700+300')
        self.var = IntVar()
        self.frame1 = Frame(master, width=200, height=150, bg='yellow')
        self.frame1.place(x=0, y=0)
        self.frame2 = Frame(master, width=230, height=300, bg='blue')
        self.frame2.place(x=200, y=0)
        self.frame3 = Frame(master, width=200, height=150, bg='red')
        self.frame3.place(x=0, y=150)        
        self.r1 = Radiobutton(self.frame1, text='    Red LED', bg='yellow', fg='blue', variable=self.var, value=1, command=self.ledSwitch)
        self.r1.place(x=0, y=0)
        self.r2 = Radiobutton(self.frame1, text=' Green LED', bg='yellow', fg='blue', variable=self.var, value=2, command=self.ledSwitch)
        self.r2.place(x=0, y=20)
        self.r3 = Radiobutton(self.frame1, text='   Blue LED', bg='yellow', fg='blue', variable=self.var, value=3, command=self.ledSwitch)
        self.r3.place(x=0, y=40)
        self.r4 = Radiobutton(self.frame1, text='Yellow LED', bg='yellow', fg='blue', variable=self.var, value=4, command=self.ledSwitch)
        self.r4.place(x=0, y=60)
        self.b1 = Button(self.frame3, text='Exit', relief=SUNKEN, bg='grey', fg='white', command=master.destroy)
        self.b1.place(x=70,y=60)
        self.b3 = Button(master, text='Flash LEDS', width = 13, relief=SUNKEN, bg='grey', fg='white', command=self.flashLEDS)
        self.b3.place(x=250,y=130)
        self.b4 = Button(master, text='All LEDS On', width = 13, relief = SUNKEN, bg='grey', fg='white', command=self.allLEDSOn)
        self.b4.place(x=250,y=95)
        self.b5 = Button(master, text='Clear LEDS', width = 13, relief=SUNKEN, bg='grey', fg='white', command=self.clearFlashLEDS)
        self.b5.place(x=250,y=200)
        self.b6 = Button(master, text = 'Cycle LEDS', width = 13, relief= SUNKEN, bg = 'grey', fg = 'white', command = self.cycleLEDS)
        self.b6.place(x = 250, y = 165)
        self.l1 = Label(master, width=16)
        self.l1.place(x=250,y=20)
        
    def ledSwitch(self):
        if self.var.get()==1:
            self.clearLEDS() 
            self.led1.on()
            self.selection = "Red LED is on" 
            self.l1.config(text = self.selection)
        elif self.var.get()==2:     
            self.clearLEDS()
            self.led2.on()
            self.selection = 'Green LED is on'
            self.l1.config(text = self.selection)
        elif self.var.get()==3:
            self.clearLEDS()
            self.led3.on()
            self.selection = 'Blue LED is on'
            self.l1.config(text = self.selection)
        elif self.var.get()==4:
            self.clearLEDS()
            self.led4.on()
            self.selection = 'Yellow LED is on'
            self.l1.config(text = self.selection)
            
    def clearLEDS(self):
        self.led1.off()
        self.led2.off()
        self.led3.off()
        self.led4.off()
        self.l1.config(text = 'All LEDS are cleared')
        
    def flashLEDS(self):
        self.b1.configure(state = 'disabled')
        self.b3.configure(state = 'disabled')
        self.b4.configure(state = 'disabled')
        self.b6.configure(state = 'disabled')
        self.l1.config(text = 'All LEDS are flashing')
        self.e = 0
        while self.e != 1:
            self.clearLEDS()
            self.frame1.after(500)
            self.allLEDSOn()
            self.l1.config(text = 'All LEDS are flashing')
            self.frame1.after(500)
            self.b1.update()
        
    
    def allLEDSOn(self):
        self.clearLEDS()
        self.led1.on()
        self.led2.on()
        self.led3.on()
        self.led4.on()
        self.l1.config(text = 'All LEDS are on')
        
    def clearFlashLEDS(self):
        self.e=1
        self.clearLEDS()
        self.b1.configure(state = 'normal')
        self.b3.configure(state = 'normal')
        self.b4.configure(state = 'normal')
        self.b6.configure(state = 'normal')
                      
    def cycleLEDS(self):
        self.clearLEDS()
        self.e = 0
        self.b1.configure(state = 'disabled')
        self.b3.configure(state = 'disabled')
        self.b4.configure(state = 'disabled')
        self.b6.configure(state = 'disabled')
        self.l1.config(text = 'All LEDS are cycling')
        while self.e != 1:
            self.led1.on()
            self.frame1.after(125)
            self.led2.on()
            self.frame1.after(125)
            self.led3.on()
            self.frame1.after(125)
            self.led4.on()
            self.frame1.after(125)
            self.led4.off()
            self.frame1.after(125)
            self.led3.off()
            self.frame1.after(125)
            self.led2.off()
            self.frame1.after(125)
            self.led1.off()
            self.frame1.after(125)
            self.b1.update()
        
        
        
root = Tk()
window = Windows(root)
root.mainloop()
