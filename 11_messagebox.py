from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title('Nado GUI')
root.geometry('640x480')

def info():
    msgbox.showinfo('알림','정상적으로 예매 완료했습니다')

def warn():
    msgbox.showwarning('경고',' 예매 매진되었습니다')

def error():
    msgbox.askretrycancel('경고',' 예매 매진되었습니다')

Button(root,command=info,text='알림').pack()
Button(root,command=warn,text='경고').pack()
Button(root,command=error,text='에러').pack()



root.mainloop()