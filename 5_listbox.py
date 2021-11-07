from tkinter import*

root = Tk()
root.title('Nado GUI')

listbox = Listbox(root,selectmode='extended',height=3)
listbox.insert(0,'사과')
listbox.insert(1,'수박')
listbox.insert(2,'딸기')
listbox.insert(END,'포토')

listbox.pack()

def btncmd():
    print('리스트에는',listbox.size(),'개가 있다.')

    print("1번째부터 3번째 항목 : ",listbox.get(0,2))

    print("선택된 항목 : ",listbox.curselection())

btn = Button(root,text="버튼",command=btncmd)
btn.pack()

root.mainloop()