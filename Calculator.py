from tkinter import *

root = Tk()
root.title("Calculator By mad_jack")
root.configure(bg="#0f0f0f")

input = Entry(root,width=35,borderwidth=5,bg="#34ebe1")
input.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def click(num):
    current = input.get()
    input.delete(0, END)
    input.insert(0,str(current)+str(num))

def clear():
    input.delete(0, END)

def add():
    first_num = input.get()
    global f_num
    global math
    math="add"
    f_num = int(first_num)
    input.delete(0,END)

def equal():
    second_num = input.get()
    input.delete(0,END)
    if math=="add":
        input.insert(0, int(f_num) + int(second_num))
    if math=="subtract":
        input.insert(0, int(f_num) - int(second_num))
    if math=="multiply":
        input.insert(0, int(f_num) * int(second_num))
    if math=="divide":
        input.insert(0, int(f_num) / int(second_num))



def subtract():
    first_num = input.get()
    global f_num
    global  math
    math = "subtract"
    f_num = int(first_num)
    input.delete(0, END)

def multiply():
    first_num = input.get()
    global f_num
    global  math
    math = "multiply"
    f_num = int(first_num)
    input.delete(0, END)

def divide():
    first_num = input.get()
    global f_num
    global  math
    math = "divide"
    f_num = int(first_num)
    input.delete(0, END)

#define buttons
button1 = Button(root,text="1",padx=40,pady=20,command=lambda: click(1),bg="#7f8787")
button2 = Button(root,text="2",padx=40,pady=20,command=lambda: click(2),bg="#7f8787")
button3 = Button(root,text="3",padx=40,pady=20,command=lambda: click(3),bg="#7f8787")
button4 = Button(root,text="4",padx=40,pady=20,command=lambda: click(4),bg="#7f8787")
button5 = Button(root,text="5",padx=40,pady=20,command=lambda: click(5),bg="#7f8787")
button6 = Button(root,text="6",padx=40,pady=20,command=lambda: click(6),bg="#7f8787")
button7 = Button(root,text="7",padx=40,pady=20,command=lambda: click(7),bg="#7f8787")
button8 = Button(root,text="8",padx=40,pady=20,command=lambda: click(8),bg="#7f8787")
button9 = Button(root,text="9",padx=40,pady=20,command=lambda: click(9),bg="#7f8787")
button0 = Button(root,text="0",padx=40,pady=20,command=lambda: click(0),bg="#7f8787")
add_button = Button(root,text="+",padx=39,pady=20,command=lambda: add(),bg="#34ebe1")
equal_button = Button(root,text="=",padx=89,pady=20,command=equal,bg="#34ebe1")
clear_button = Button(root,text="Clear",padx=79,pady=20,command=clear,bg="#34ebe1")
subtract_button = Button(root,text="-",padx=41,pady=20,command=subtract,bg="#34ebe1")
multiply_button = Button(root,text="*",padx=42,pady=20,command=multiply,bg="#34ebe1")
divide_button = Button(root,text="/",padx=42,pady=20,command=divide,bg="#34ebe1")
#putting on the screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
add_button.grid(row=5,column=0)
equal_button.grid(row=5,column=1,columnspan=2)
clear_button.grid(row=4,column=1,columnspan=2)
subtract_button.grid(row=6,column=0)
multiply_button.grid(row=6,column=1)
divide_button.grid(row=6,column=2)

root.mainloop()