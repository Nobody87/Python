from tkinter import ttk
import tkinter as tk
import sqlite3


def connect():
    conn = sqlite3.connect("jobcard.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profile(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
    conn.commit()
    conn.close()


def View():
    conn = sqlite3.connect("jobcard.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Customers")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()


connect()  #  this to create the db

root = tk.Tk()
root.geometry("1200x400")

tree = ttk.Treeview(column=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9"), show='headings')
tree.heading("#1", text="Customer ID")
tree.heading("#2", text="Customer name")
tree.heading("#3", text="Address 1")
tree.heading("#4", text="Address 2")
tree.heading("#5", text="Region")
tree.heading("#6", text="Contact Name")
tree.heading("#7", text="Contact Surname")
tree.heading("#8", text="Office Number")
tree.heading("#9", text="Mobile Number")
tree.pack()

b2 = tk.Button(text="view data", command=View)
b2.pack()

root.mainloop()