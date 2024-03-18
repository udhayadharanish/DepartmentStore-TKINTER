from tkinter import *

import pandas

import backend_dept

window =Tk()

bill = pandas.DataFrame(columns=["Item","Quantity","Price"])


window.wm_title("Department Store")
cart = []
s =0

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def view_cart():
    global total
    item_list =[]
    qty_list =[]
    price_list =[]
    total=0
    list1.delete(0,END)
    list1.insert(0,"CART:")
    for item in cart:
        list1.insert(END,item)
        total += float(item[2])*int(item[3])
        item_list.append(item[0])
        price_list.append(item[2])
        qty_list.append(item[3])
    list1.insert(END,f"Total price =  {total}")

    bill["Item"] = item_list
    bill["Quantity"] = qty_list
    bill["Price"] = price_list


def close_command():
    print(bill)
    print("Total = ",total)
    window.destroy()

def selecting(event):
    try:
        global selected
        index = list1.curselection()[0]
        selected = backend_dept.view()[index]
        e1.delete(0,END)
        e1.insert(END,selected[1])
        e2.delete(0, END)
        e2.insert(END, selected[3])
        e3.delete(0, END)
        e3.insert(END, selected[2])
        e4.delete(0, END)
        e4.insert(END, selected[4])
    except:
        pass


def view_command():
    list1.delete(0,END)
    for row in backend_dept.view():
        list1.insert(END,row)

def add_command():
    backend_dept.insert(item=item_text.get(),price=price_text.get(),expirydate=expiry_text.get(),quantity=quantity_text.get())

def delete_command():
    backend_dept.delete(selected[0])
    list1.delete(0,END)
    list1.insert(END,"item deleted")
def update_command():
    backend_dept.update(item=item_text.get(),price=price_text.get(),expirydate=expiry_text.get(),quantity=quantity_text.get(),id=selected[0])
    list1.delete(0,END)
    list1.insert(END,(item_text.get(),expiry_text.get(),price_text.get(),quantity_text.get()))
def buy_command():
    try:
        if selected[4] >= int(quantity_text.get()):
            backend_dept.buy(item=item_text.get(),price=price_text.get(),expirydate=expiry_text.get(),quantity=quantity_text.get(),id=selected[0])
            list1.delete(0,END)
            list1.insert(END,f"addedtocart: {item_text.get(),expiry_text.get(),price_text.get(),quantity_text.get()}")
            cart.append((item_text.get(),expiry_text.get(),price_text.get(),quantity_text.get()))

        if selected[4] < int(quantity_text.get()):
            list1.delete(0,END)
            list1.insert(END,"Item out of stock")
    except NameError:
        list1.delete(0,END)
        list1.insert(END,"please select any item (view item -> select ->Enter the quantity-> buy item)")

def search_command():
    list1.delete(0,END)
    for row in backend_dept.search(item=item_text.get(),price=price_text.get(),expirydate=expiry_text.get(),quantity=quantity_text.get()):
        list1.insert(END,row)

#labels

l1 = Label(window,text="Item Name")
l1.grid(row=1,column=0,pady=3,padx=3)

l2 = Label(window,text="Expiry Date")
l2.grid(row=1,column=2,padx=3,pady=3)

l3 = Label(window,text="Price")
l3.grid(row=2,column=0,padx=3,pady=3)

l4 = Label(window,text="Quantity")
l4.grid(row=2,column=2,padx=3,pady=3)

l5 = Label(window,text="Info")
l5.grid(row=3,column=0,columnspan=2,padx=3,pady=3)

l6 = Label(window,text="Select or Enter the informations before action ",font=3)
l6.grid(row=0,column=0,columnspan=5,pady=5)


#Entries


item_text = StringVar()
e1 = Entry(window,textvariable=item_text)
e1.grid(row=1,column=1,padx=3,pady=3)

price_text = StringVar()
e2 = Entry(window,textvariable=price_text)
e2.grid(row=2,column=1,padx=3,pady=3)

expiry_text = StringVar()
e3 = Entry(window,textvariable=expiry_text)
e3.grid(row=1,column=3,padx=3,pady=3)

quantity_text = StringVar()
e4 = Entry(window,textvariable=quantity_text)
e4.grid(row=2,column=3,padx=3,pady=3)

#ListBox

list1 = Listbox(window,width=55,height=15)
list1.grid(row=4,column=0,columnspan=2,rowspan=10,padx=5)
list1.delete(0,END)
for row in backend_dept.view():
    list1.insert(END,row)

list1.bind("<<ListboxSelect>>",selecting)

#ScrollBar

sb1 = Scrollbar(window,orient="vertical")
sb1.grid(row=4,column=2,rowspan=8)

sb2 = Scrollbar(window,orient="horizontal")
sb2.grid(row=16,column=0,columnspan=2)

list1.configure(yscrollcommand=sb1.set,xscrollcommand=sb2.set)
sb1.configure(command=list1.yview)
sb2.configure(command=list1.xview)

#Buttons

b1 = Button(window,text="Add item",width=12,command=add_command)
b1.grid(row=4,column=3,padx=1,pady=1)

b2 = Button(window,text="Buy item",width=12,command=buy_command)
b2.grid(row=5,column=3,padx=1,pady=1)

b3 = Button(window,text="Delete item",width=12,command=delete_command)
b3.grid(row=6,column=3,padx=1,pady=1)

b4 = Button(window,text="View item",width=12,command=view_command)
b4.grid(row=7,column=3,padx=1,pady=1)

b5 = Button(window,text="Search item",width=12,command=search_command)
b5.grid(row=8,column=3,padx=1,pady=1)

b6 = Button(window,text="Update item",width=12,command=update_command)
b6.grid(row=9,column=3,padx=1,pady=1)

b7 = Button(window,text="cart",width=12,command=view_cart)
b7.grid(row=10,column=3,padx=1,pady=1)

b8 = Button(window,text="Close",width=12,command=close_command)
b8.grid(row=11,column=3,pady=1,padx=1)

b9= Button(window,text="Clear Entries",command=clear)
b9.grid(row=1,column=4,rowspan=2,padx=5)


window.mainloop()