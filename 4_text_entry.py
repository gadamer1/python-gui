from tkinter import*

root = Tk()
root.title('Nado GUI')

txt = Text(root,width=30,height=5)
txt.pack()

txt.insert(END,'글자를 입력하세요')

e= Entry(root, width=30)
e.pack()
e.insert(0,'한줄만')

def btncmd():
    print(txt.get("1.0",END)) #라인 1, index 0부터
    print(e.get())

    txt.delete("1.0",END) 
    e.delete(0,END)

btn1 = Button(root, text="클릭",command=btncmd)
btn1.pack()
root.mainloop()