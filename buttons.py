from tkinter import *

root = Tk()
def my_click():
    my_label = Label(root,text="Hey! You just clicked me.")
    my_label.pack()

my_button = Button(root,text="Click Me",padx=10,pady=10,command=my_click,fg="white",bg="blue")
my_button.pack()

root.mainloop()