import tkinter as tk
from tkinter import *
from tkinter import ttk

#structure and layout

window = tk.Tk()
window.title("Registration")
window.geometry("750x450")

style = ttk.Style(window)
style.configure('lefttab.TNotebook',tabposition='wn')

#tab layout
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

# Add Tabs to Notebook
tab_control.add(tab1, text =f'{"Home":^20s}')
tab_control.add(tab2, text = f'{"View":^20s}')
tab_control.add(tab3, text = f'{"Search":^20s}')
tab_control.add(tab4, text = f'{"Export":^20s}')
tab_control.add(tab5, text = f'{"About":^20s}')


tab_control.pack(expand=1, fill ='both')

label1 = Label(tab1, text ='Home',padx=10,pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text ='View',padx=10,pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text ='Search',padx=10,pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab4, text ='Export',padx=10,pady=5)
label4.grid(column=0, row=0)

label5 = Label(tab5, text ='About',padx=10,pady=5)
label5.grid(column=0, row=0)

#Home
l1 = Label(tab1, text='First Name',padx=5,pady=5).grid(column=0,row=1)
fname_raw = StringVar()
fname_entry = Entry(tab1,textvariable=fname_raw,width=50).grid(row=1,column=1)

l2 = Label(tab1, text='Last Name',padx=5,pady=5).grid(column=0,row=2)
lname_raw = StringVar()
lname_entry = Entry(tab1,textvariable=lname_raw,width=50).grid(row=2,column=1)

l3 = Label(tab1, text='EC Number',padx=5,pady=5).grid(column=0,row=3)
ecnum_raw = IntVar()
ecnum_entry = Entry(tab1,textvariable=ecnum_raw,width=50).grid(row=3,column=1)

l4 = Label(tab1, text='e-mail Address',padx=5,pady=5).grid(column=0,row=4)
email_raw = StringVar()
email_entry = Entry(tab1,textvariable=email_raw,width=50).grid(row=4,column=1)

l5 = Label(tab1, text='Address',padx=5,pady=5).grid(column=0,row=5)
address_raw = StringVar()
address_entry = Entry(tab1,textvariable=address_raw,width=50).grid(row=5,column=1)

l6 = Label(tab1, text='Phone Number(s)',padx=5,pady=5).grid(column=0,row=6)
phone_raw = IntVar()
phone2_raw = IntVar()
phone_entry = Entry(tab1,textvariable=phone_raw,width=50).grid(row=6,column=1)
phone2_entry = Entry(tab1,textvariable=phone2_raw,width=50).grid(row=7,column=1)

b1 = ttk.Button(tab1, text='Add',width=12).grid(column=0,row=8)
b2 = ttk.Button(tab1, text='Clear',width=12).grid(column=1,row=8)

#View

#Search

#Export

#About
window.mainloop()