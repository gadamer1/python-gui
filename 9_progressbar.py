import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

p_var = DoubleVar()
progressbar = ttk.Progressbar(root,maximum=100, length=150,variable=p_var,mode="determinate")
progressbar.pack()

def btncmd():
    for i in range(101):
        time.sleep(0.01)
        p_var.set(i)
        progressbar.update()

btn1 = Button(root,text="클릭",command=btncmd)
btn1.pack() 
root.mainloop()