from tkinter import  *

root = Tk()
root.title("Sliders")
root.geometry("400x400")
def check():
    mylabel = Label(root, text=var.get()).pack()

var = StringVar()
c = Checkbutton(root,text="Select Me!",variable=var,onvalue="Checked",offvalue="Unchecked")
c.deselect()
c.pack()


mybtn = Button(root,text="Show",command=check).pack()
root.mainloop()