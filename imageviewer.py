from tkinter import *

root = Tk()

root.title("MadViewer")
root.iconbitmap("C:/Users/CyberLord/PycharmProjects/tkinter/icon.ico")

img1 = PhotoImage(file="C:/Users/CyberLord/Downloads/Clip.png")
img2 = PhotoImage(file="C:/Users/CyberLord/Downloads/d1.png")
img3 = PhotoImage(file="C:/Users/CyberLord/Downloads/d2.png")
img4 = PhotoImage(file="C:/Users/CyberLord/Downloads/d3.png")
img5 = PhotoImage(file="C:/Users/CyberLord/Downloads/d4.png")

img_list = [img1,img2,img3,img4,img5]

mylabel = Label(root,image=img1)
mylabel.grid(row=0,column=0,columnspan=3)
def forward(img_num):
    global mylabel
    global forward_button
    global back_button
    mylabel.grid_forget()
    mylabel=Label(image=img_list[img_num-1])
    forward_button = Button(root, text=">>", command=lambda: forward(img_num + 1))
    back_button = Button(root, text="<<",command=lambda: back(img_num-1))

    if img_num==5:
        forward_button = Button(root, text=">>",state=DISABLED)

    mylabel.grid(row=0,column=0,columnspan=3)
    forward_button.grid(row=1, column=2)
    back_button.grid(row=1,column=0)

def back(img_num):
    global mylabel
    global forward_button
    global back_button
    mylabel.grid_forget()
    mylabel = Label(image=img_list[img_num - 1])
    forward_button = Button(root, text=">>", command=lambda: forward(img_num + 1))
    back_button = Button(root, text="<<", command=lambda: back(img_num - 1))
    if img_num==1:
        back_button = Button(root, text="<<",state=DISABLED)

    mylabel.grid(row=0, column=0, columnspan=3)
    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)

exit_button = Button(root,text="Exit",command=root.quit)
forward_button = Button(root,text=">>",command=lambda: forward(2))
back_button = Button(root,text="<<")

back_button.grid(row=1,column=0)
exit_button.grid(row=1,column=1)
forward_button.grid(row=1,column=2)

root.mainloop()