from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

def create_new_file():
    print("새 파일을 만듭니다")

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New window", command=create_new_file)
menu_file.add_separator()
menu_file.add_command(label="New open file", command=create_new_file)
menu_file.add_separator() 
menu_file.add_command(label="Save all", state="disable")
menu_file.add_separator()
menu_file.add_command(label="exit", command=root.quit)
menu.add_cascade(label="file", menu=menu_file)

# edit menu
menu_edit = Menu(menu,tearoff=0)
menu.add_cascade(label="Edit",menu = menu_edit)

root.config(menu=menu)
root.mainloop()