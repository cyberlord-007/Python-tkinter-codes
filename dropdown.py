from tkinter import*
from PIL import ImageTk,ImageTk

root = Tk()
root.title("Dropdown Menus")
root.geometry("500x500")

def show():
	mylabel = Label(root,text=var.get()).pack()


var=StringVar()
var.set("Pizza")
dd = OptionMenu(root,var,"Pizza","Hamburger","Hotdogs","Pie")#if you want to add a list put an aseterisk befor list_name
dd.pack()

mybtn = Button(root,text="Confirm",command=show).pack()

root.mainloop()