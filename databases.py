from tkinter import *

import sqlite3

root = Tk()
root.title("Dropdown Menus")
root.geometry("500x500")
# connect database or create one
connect = sqlite3.connect("address_book.db")
# create cursor (cursor goes to the database and does all operation for us)
cursor = connect.cursor()
'''cursor.execute("""CREATE TABLE addresses(
first_name text,
last_name text,
address text,
city text,
state text,
zipcode integer)""")'''
def delete():
    connect = sqlite3.connect("address_book.db")
    cursor = connect.cursor()

    cursor.execute("DELETE FROM addresses WHERE oid=" + delt.get())
    delt.delete(0,END)

    connect.commit()
    connect.close()

def submit():
    connect = sqlite3.connect("address_book.db")
    cursor = connect.cursor()


    cursor.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
    {
    "f_name" : f_name.get(),
    "l_name": l_name.get(),
    "address": address.get(),
    "city": city.get(),
    "state": state.get(),
    "zipcode": zipcode.get(),
    })

    connect.commit()
    connect.close()
# clear data
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    connect = sqlite3.connect("address_book.db")
    cursor = connect.cursor()
    cursor.execute("SELECT *,oid FROM addresses")
    records = cursor.fetchall()
    print_rec = ""
    for rec in records:
        print_rec += str(rec[0]) + " " + str(rec[1]) + " " + "\t"+str(rec[6])+ "\n"

    query_label = Label(root,text=print_rec)
    query_label.grid(row=8,column=0,columnspan=2)

    connect.commit()
    connect.close()


# creating entry boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20,pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delt = Entry(root,width=30)
delt.grid(row=8,column=1,padx=20,pady=5)

# creating field labels
f_label = Label(root, text="First Name")
f_label.grid(row=0, column=0,pady=(10,0))

l_label = Label(root, text="Last Name")
l_label.grid(row=1, column=0)

a_label = Label(root, text="Address")
a_label.grid(row=2, column=0)

c_label = Label(root, text="City")
c_label.grid(row=3, column=0)

s_label = Label(root, text="State")
s_label.grid(row=4, column=0)

z_label = Label(root, text="Zipcode")
z_label.grid(row=5, column=0)

d_label = Label(root,text="Delete ID")
d_label.grid(row=8,column=0,pady=10)
# create a submit button
btn = Button(root, text="Add To Database", command=submit)
btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

querybtn = Button(root,text="Show Records",command=query)
querybtn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=140)

deletbtn = Button(root,text="Delete record",command=delete)
deletbtn.grid(row=9,column=0,columnspan=2,padx=10,pady=10,ipadx=140)
# changes should be reflected in our database,for that commit()
connect.commit()
connect.close()

root.mainloop()