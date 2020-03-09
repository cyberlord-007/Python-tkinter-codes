from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("Message boxes")
root.iconbitmap("C:/Users/CyberLord/PycharmProjects/tkinter/icon.ico")
'''types of message boxes-
-showinfo
-showerror
-showwarning
-askquestion(returns yes or no)
-askokcancel(returns 1 or 0)
-askyesno(returns 1 or 0)'''
def click():
    response = messagebox.askyesno("You hit me :(","I'm gonna scare the hell outta you.")
    #Label(root,text=response).pack()
    if response==1:
        Label(root, text="Ready to go").pack()
    else:
        Label(root, text="Wait! Stop there sparky").pack()

Button(root,text="Hit Me!",command=click).pack()

root.mainloop()