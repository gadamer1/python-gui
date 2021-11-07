from tkinter import*

root = Tk()
root.title('Nado GUI')

label1= Label(root,text="메뉴를 선택하세요")
label1.pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root,text="burger",value=1,variable=burger_var)
btn_burger2 = Radiobutton(root,text="burger2",value=2,variable=burger_var)
btn_burger3 = Radiobutton(root,text="burger3",value=3,variable=burger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


def btncmd():
    print(burger_var.get()) #0체크 해제, 1 체크

btn = Button(root,text="버튼",command=btncmd)
btn.pack()

root.mainloop() 