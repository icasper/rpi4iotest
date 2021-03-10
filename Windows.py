from tkinter import *

class Windows:
    
    def __init__(self, master):
        
        master.title('A new window')
        master.geometry('400x300+700+300')
        self.var = IntVar()
        self.frame1 = Frame(master, width=200, height=150, bg='yellow')
        self.frame1.place(x=0, y=0)
        self.frame2 = Frame(master, width=200, height=300, bg='blue')
        self.frame2.place(x=200, y=0)
        self.frame3 = Frame(master, width=200, height=150, bg='red')
        self.frame3.place(x=0, y=150)        
        self.r1 = Radiobutton(self.frame1, text='    Red LED', bg='yellow', fg='blue', variable=self.var, value=1)
        self.r1.place(x=0, y=0)
        self.r2 = Radiobutton(self.frame1, text=' Green LED', bg='yellow', fg='blue', variable=self.var, value=2)
        self.r2.place(x=0, y=20)
        self.r3 = Radiobutton(self.frame1, text='   Blue LED', bg='yellow', fg='blue', variable=self.var, value=3)
        self.r3.place(x=0, y=40)
        self.r4 = Radiobutton(self.frame1, text='Yellow LED', bg='yellow', fg='blue', variable=self.var, value=4)
        self.r4.place(x=0, y=60)
        self.b1 = Button(self.frame3, text='Exit', relief=SUNKEN, bg='grey', fg='white', command=master.destroy)
        self.b1.place(x=70,y=60)
        

        
    
        
        

                    
        
root = Tk()
window = Windows(root)
