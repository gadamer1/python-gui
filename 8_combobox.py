import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

values = [str(i) for i in range(1,32)]
combobox = ttk.Combobox(root,height=5,values=values,state="readonly")
combobox.pack()
combobox.current(10)

def btncmd():
    print("카드결제일",combobox.get())

btn1 = Button(root, text="클릭",command=btncmd)
btn1.pack()
root.mainloop()