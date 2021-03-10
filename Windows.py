from tkinter import *
from gpiozero import LED

class Windows:
    
    def __init__(self, master):
        
        self.led1 = LED(17)
        self.led2 = LED(27)
        self.led3 = LED(22)
        self.led4 = LED(10)
        master.title('A new window')
        master.geometry('400x300+700+300')
        self.var = IntVar()
        self.frame1 = Frame(master, width=200, height=150, bg='yellow')
        self.frame1.place(x=0, y=0)
        self.frame2 = Frame(master, width=200, height=300, bg='blue')
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
        self.b2 = Button(master, text='Clear LEDS', relief=SUNKEN, bg='blue', fg='yellow', command=self.clearLEDS)
        self.b2.place(x=250,y=60)
        self.l1 = Label(master)
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
        self.l1.config(text = 'All LEDS are cleared')
        
root = Tk()
window = Windows(root)
root.mainloop()
