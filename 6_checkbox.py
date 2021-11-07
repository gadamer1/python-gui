from tkinter import*

root = Tk()
root.title('Nado GUI')

listbox = Listbox(root,selectmode='extended',height=3)

chkvar = IntVar()
checkbox = Checkbutton(root,text="오늘 하루 보지  않기",variable=chkvar)
checkbox.pack()
chkvar2 = IntVar()
checkbox2 = Checkbutton(root,text="오늘 하루 보지  않기",variable=chkvar2)
checkbox2.pack()

def btncmd():
    print(chkvar.get()) #0체크 해제, 1 체크

btn = Button(root,text="버튼",command=btncmd)
btn.pack()

root.mainloop() 