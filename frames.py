from tkinter import*

root=Tk()
root.title("Frames")
root.iconbitmap("C:/Users/CyberLord/PycharmProjects/tkinter/icon.ico")
frame = LabelFrame(root,text="This is a frame.",padx=5,pady=5)
frame.pack(padx=10,pady=10)
#pack and grid don't work together generally but in case of frames you can use grid
#to position objects inside of a frame
button = Button(frame,text="Click Me!")
button.pack()
#or
#button.grid(row=0,column=0)
root.mainloop()