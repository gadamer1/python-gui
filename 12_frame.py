from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry('640x480')

Label(root,text="메뉴를 선택해주세요").pack(side='top')
Button(root,text='주문하기').pack(side='bottom')

frame_burger = Frame(root,relief="solid",bd=1)
frame_burger.pack(side="left",fill="both",expand=True)

Button(frame_burger,text="횀벅").pack()
Button(frame_burger,text="횀벅2").pack()
Button(frame_burger,text="횀벅3").pack()

frame_drink = Frame(root,relief="solid",bd=1)
frame_drink.pack(side='right',fill='both',expand=True)

Button(frame_drink,text="횀벅").pack()
Button(frame_drink,text="횀벅2").pack()
Button(frame_drink,text="횀벅3").pack()

root.mainloop()