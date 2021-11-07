from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry('640x480')

btn1 = Button(root,padx=5,pady=5, text='f16')
btn2 = Button(root,padx=5,pady=5, text='f17')
btn3 = Button(root,padx=5,pady=5, text='f18')
btn4 = Button(root,padx=5,pady=5, text='f19')
btn5 = Button(root,padx=5,pady=5, text='clear')
btn6 = Button(root,padx=5,pady=5, text='zz')
btn7 = Button(root,padx=5,pady=5, text='/')
btn8 = Button(root,padx=5,pady=5, text='*')
btn9 = Button(root,padx=5,pady=5, text='7')
btn10 = Button(root,padx=5,pady=5, text='8')
btn11 = Button(root,padx=5,pady=5, text='9')
btn12 = Button(root,padx=5,pady=5, text='-')
btn13 = Button(root,padx=5,pady=5, text='4')
btn14 = Button(root,padx=5,pady=5, text='5')
btn15 = Button(root,padx=5,pady=5, text='6')
btn16 = Button(root,padx=5,pady=5, text='+')

button_lists = [btn1, btn2, btn3, btn4, btn5, btn6, btn7,btn8, btn9, 
btn10, btn11,btn12, btn13, btn14, btn15, btn16,]

idx=0
for i in range(0,4):
    for j in range(0,4):
        button_lists[idx].grid(row=i,column=j,sticky=N+E+W+S,padx=10, pady=10)
        print(i,j)
        idx+=1


 


root.mainloop()