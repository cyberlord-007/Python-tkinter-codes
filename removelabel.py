from tkinter import*
from PIL import ImageTk,ImageTk
root = Tk()
root.title("Dropdown Menus")
root.geometry("400x400")

def remove():
	mylabel.destroy()

def submit():
	val = "Hello! " + e.get()
	global mylabel
	mylabel = Label(root,text=val)
	e.delete(0,END)
	mylabel.pack(pady=10)
	

e = Entry(root,width=50)
e.pack(padx=10,pady=10)

btn = Button(root,text="Submit",command=submit)
btn.pack(pady=10)

dbtn = Button(root,text="Delete",command=remove)
dbtn.pack(pady=10)


root.mainloop()