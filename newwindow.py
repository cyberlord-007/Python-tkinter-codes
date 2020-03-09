from tkinter import*

root=Tk()
root.title("Original Window")
root.iconbitmap("C:/Users/CyberLord/PycharmProjects/tkinter/icon.ico")
def open():
    global img
    top = Toplevel()
    top.title("New Window")
    img = PhotoImage(file="C:/Users/CyberLord/Downloads/Clip.png")
    mylabel = Label(top, image=img).pack()
    button2 = Button(top, text="Close the new window", command=top.destroy).pack()

button = Button(root,text="Open a new window",command=open).pack()

root.mainloop()