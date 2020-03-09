from tkinter import*

root=Tk()
root.title("Radio Buttons")
root.iconbitmap("C:/Users/CyberLord/PycharmProjects/tkinter/icon.ico")
#r=IntVar()
r=StringVar()
r.set(0)
Prices = [
    ("Pizza","100/-"),
    ("Sandwich","45/-"),
    ("Pastries","95/-"),
    ("Pasta","110/-"),
]

for item, price in Prices:
    Radiobutton(root,text=item,variable=r,value=price).pack(anchor=W)

def click(value):
    mylabel = Label(root, text=value)
    mylabel.pack()

#Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda: click(r.get())).pack()
#Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda: click(r.get())).pack()

button = Button(root,text="Know Price",command=lambda: click(r.get()))
button.pack()
#mylabel = Label(root,text=r.get())
#mylabel.pack()

root.mainloop()