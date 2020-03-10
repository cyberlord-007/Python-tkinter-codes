from tkinter import *
import os
os.system("clear")

root =Tk()
root.title("Menu Bars")
root.geometry("400x400")

def fun():
	return
#toplevel menu
mymenu = Menu(root)
root.config(menu=mymenu)

#sub menu
file_menu = Menu(mymenu)
mymenu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=fun)
#adding a seperator
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

edit_menu = Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=fun)
edit_menu.add_command(label="Copy",command=fun)

root.mainloop()