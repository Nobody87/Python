import tkinter as tk  # GUI package
import sqlite3 as sq  # For tables and database
import tkinter.font as tkFont
import tkinter.ttk as ttk
import os

customer_window = tk.Tk()
customer_window.title("Customer Entry")
customer_window.geometry('800x600+0+0')
header = tk.Label(customer_window, text="Create New Customer", font=("arial", 30, "bold"), fg="steelblue").pack()

con = sq.connect('jobcard.db')  # dB browser for sqlite needed
c = con.cursor()  # SQLite command, to connect to db so 'execute' method can be called

L1 = tk.Label(customer_window, text="Customer Name:", font=("arial", 18)).place(x=10, y=100)
L2 = tk.Label(customer_window, text="Customer Address 1:", font=("arial", 18)).place(x=10, y=150)
L3 = tk.Label(customer_window, text="Customer Address 2:", font=("arial", 18)).place(x=10, y=200)
L4 = tk.Label(customer_window, text="Name:", font=("arial", 18)).place(x=10, y=250)
L5 = tk.Label(customer_window, text="Surname:", font=("arial", 18)).place(x=10, y=300)
L6 = tk.Label(customer_window, text="Office Number:", font=("arial", 18)).place(x=10, y=350)
L7 = tk.Label(customer_window, text="Mobile Number:", font=("arial", 18)).place(x=10, y=400)
L8 = tk.Label(customer_window, text="Region:", font=("arial", 18)).place(x=10, y=450)

# Create variables for each list
cust = tk.StringVar(customer_window)  # For 1st dd
cust.set('Customers')  # Inital placeholder for field

custdb = tk.StringVar(customer_window)  # 2nd dropdown list
custdb.set('Customers')

cust_name = tk.StringVar(customer_window)
cust_add1 = tk.StringVar(customer_window)
cust_add2 = tk.StringVar(customer_window)
main_name = tk.StringVar(customer_window)
main_surname = tk.StringVar(customer_window)
main_office = tk.StringVar(customer_window)
main_mobile = tk.StringVar(customer_window)
cust_region = tk.StringVar(customer_window)

# Entry for 'input' in GUI
cust_nameE = tk.Entry(customer_window, textvariable=cust_name)
cust_nameE.place(x=250, y=105)

cust_add1E = tk.Entry(customer_window, textvariable=cust_add1)
cust_add1E.place(x=250, y=155)

cust_add2E = tk.Entry(customer_window, textvariable=cust_add2)
cust_add2E.place(x=250, y=205)

main_nameE = tk.Entry(customer_window, textvariable=main_name)
main_nameE.place(x=250, y=255)

main_surnameE = tk.Entry(customer_window, textvariable=main_surname)
main_surnameE.place(x=250, y=305)

main_officeE = tk.Entry(customer_window, textvariable=main_office)
main_officeE.place(x=250, y=355)

main_mobileE = tk.Entry(customer_window, textvariable=main_mobile)
main_mobileE.place(x=250, y=405)

cust_regionE = tk.Entry(customer_window, textvariable=cust_region)
cust_regionE.place(x=250, y=455)

# get func to isolate the text entered in the entry boxes and submit to database
def get():
    print("You have submitted a record")

    c.execute(
        'CREATE TABLE IF NOT EXISTS ' + cust.get() + ' ( cus_name TEXT, cus_add1 TEXT, cus_add2 TEXT, cus_region TEXT, main_name TEXT, main_surname TEXT, main_office_num TEXT, main_mobile_num TEXT)')  # SQL syntax


    c.execute('INSERT INTO ' + cust.get() + ' (cus_name, cus_add1, cus_add2, cus_region, main_name, main_surname, main_office_num, main_mobile_num) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
              (cust_name.get(), cust_add1.get(), cust_add2.get(), cust_region.get(), main_name.get(), main_surname.get(), main_office.get(), main_mobile.get()))  # Insert record into database.
    con.commit()

    # Reset fields after submit
    cust_name.set('')
    cust_add1.set('')
    cust_add2.set('')
    main_name.set('')
    main_surname.set('')
    main_office.set('')
    main_mobile.set('')
    cust_region.set('')


# Clear boxes when submit button is hit
def clear():
    cust_name.set('')
    cust_add1.set('')
    cust_add2.set('')
    main_name.set('')
    main_surname.set('')
    main_office.set('')
    main_mobile.set('')
    cust_region.set('')


def record():
     top = tk.Toplevel()



#    c.execute('SELECT * FROM ' + custdb.get())  # Select from which ever compound lift is selected

#    frame = Frame(customer_window)
#    frame.place(x=400, y=150)
#
#    Lb = Listbox(frame, height=20, width=100, font=("arial", 12))
#    Lb.pack(side=LEFT, fill=Y)
#
#    scroll = Scrollbar(frame, orient=VERTICAL)  # set scrollbar to list box for when entries exceed size of list box
#    scroll.config(command=Lb.yview)
#    scroll.pack(side=RIGHT, fill=Y)
#    Lb.config(yscrollcommand=scroll.set)
#
#    Lb.insert(0, 'Date, Max Weight, Reps')  # first row in listbox
#
#    data = c.fetchall()  # Gets the data from the table
#
#    for row in data:
#        Lb.insert(1, row)  # Inserts record row by row in list box
#
#    L7 = Label(customer_window, text=custdb.get() + '      ',
#               font=("arial", 16)).place(x=400, y=100)  # Title of list box, given which compound lift is chosen
#
#    L8 = Label(customer_window, text="They are ordered from most recent",
#               font=("arial", 16)).place(x=400, y=350)
#    con.commit()


button_submit = tk.Button(customer_window, text="Submit", command=get)
button_submit.place(x=100, y=500)

button_clear = tk.Button(customer_window, text="Clear", command=clear)
button_clear.place(x=180, y=500)

button_opendb = tk.Button(customer_window, text="Open DB", command=record)
button_opendb.place(x=10, y=500)

customer_window.mainloop()  # mainloop() -> make sure that window stays open