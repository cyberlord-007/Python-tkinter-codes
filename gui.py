from tkinter import*

root = Tk()
#creating label Widget
my_label1 = Label(root,text="Hello! World")
my_label2 = Label(root,text="This is my first GuI.")
#putting it on to the screen
my_label1.grid(row=0,column=0)
my_label2.grid(row=1,column=1)
#invent loop
root.mainloop()








