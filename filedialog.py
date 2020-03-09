from tkinter import  *
from tkinter import filedialog
from PIL import ImageTk,Image
root = Tk()
root.title("File Dialog Box")
root.iconbitmap("C:/Users/CyberLord/PycharmProjects/tkinter/icon.ico")
'''file=filedialog.askopenfilename(initialdir="C:/Users/CyberLord/PycharmProjects/tkinter",title="Select A File",filetype=(("Icon Files","*.ico"),("All Files","*.*")))
mylabel = Label(root,text=file).pack()
myimage = ImageTk.PhotoImage(Image.open(file))
imglabel = Label(root,image=myimage).pack()'''

#or we can create a button to open file
#always remember filedialog box doesn't open a file it just returns the location
def open():
	global myimage
	file=filedialog.askopenfilename(initialdir="C:/Users/CyberLord/PycharmProjects/tkinter",title="Select A File",filetype=(("Icon Files","*.ico"),("All Files","*.*")))
	mylabel=Label(root,text=file).pack()
	myimage=ImageTk.PhotoImage(Image.open(file))
	imglabel=Label(root,image=myimage).pack()


btn = Button(root,text="Open File",command=open).pack()

root.mainloop()