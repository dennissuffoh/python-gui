from tkinter import *
from tkinter import ttk
import os

class Root (Tk):
    def __init__ (self):
        super(Root, self).__init__()
        self.title("Tkinter Window")
        self.minsize(640,500)
        self.configure(background = '#4d4d4d')
        self.wm_iconbitmap('icon1.ico')
        self.createWidget()

    
    

    def createWidget(self):
        label = Label(self, text ="fire alarmo")
        label.grid(column = 4, row = 0)
        label.configure(background = '#4d4d4d')
        label.configure(foreground = 'white')
        button = ttk.Button(self, text = 'click lana')
        button.grid(column = 1, row = 0)
        




root = Root()
root.mainloop()        

