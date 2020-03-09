from tkinter import *

root = Tk()
input = Entry(root,width=30,bg="white",fg="blue",borderwidth=5)
#to get info in input field
input.pack()
input.insert(0,"Name")
def my_click():
    my_label = Label(root,text="Hello! " + input.get())
    my_label.pack()

my_button = Button(root,text="Enter Your Name",padx=5,pady=5,command=my_click,fg="white",bg="blue")
my_button.pack()

root.mainloop()