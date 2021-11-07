from tkinter import*

root = Tk()
root.title('Nado GUI')
root.geometry('640x480')
label1= Label(root, text='안녕하세요')
label1.pack()

def change():
    label1.config(text="아년ㅇ")

btn1 = Button(root, text="클릭",command=change)
btn1.pack()

root.mainloop()