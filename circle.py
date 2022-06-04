import tkinter
from tkinter import *

master = tkinter.Tk()


for i in range(30):
    for b in range(30):   
        color = 'white'
        radius = 5
        if (i-15)**2+(b-15)**2<= ((radius+1)**2):
            color = "blue"
        q=Label(master, fg='white', bg=color,  width=2, height=1,borderwidth=1, relief="groove")                

        q.grid(row=i,column=b)
        
mainloop()