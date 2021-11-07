from tkinter import*

root = Tk()
root.title('Nado GUI')

btn1 = Button(root,text='BUTTON')
btn1.pack()
btn2 = Button(root,padx=5, pady=10,text='BUTTON2')
btn2.pack()
btn3 = Button(root,padx=10, pady=5,text='BUTTON2')
btn3.pack()

btn4 = Button(root,width=10, height=5,text='BUTTON2')
btn4.pack()
def btncmd():
    print("버튼 클릭됨")
btn5 = Button(root,fg='red',bg='yellow',padx=10, pady=5,text='BUTTON2',command=btncmd)
btn5.pack()


root.mainloop()