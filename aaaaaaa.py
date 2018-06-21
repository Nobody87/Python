import tkinter as tk  # python3.x
import time
from tkinter import messagebox

# import Tkinter as tk #python2.x
from tkinter import *
import pyodbc
import datetime

# Set Up App Window & defaults
root = tk.Tk()
root.option_add("*Font", "Verdana")
root.geometry('1450x705')  # Size WxH
root.title("News Indexing Contributor Analysis App")

# get current date
Dt = datetime.date.today()

# create RecordID
time_string = time.strftime('%H%M%S')

y = str(time_string)

# Get USERNAME
import getpass

USER = Label(root, text="User: " + getpass.getuser().upper())
USER.grid(row=0, column=3, sticky="e")
# Convert to string and get first 4 characters
UName = str(getpass.getuser().upper())
partial = UName[:4]

# z.grid(row=1, column = 4)
RecordID = partial + y
RecordIDx = Label(root, text="Record ID: " + RecordID)
RecordIDx.grid(row=1, column=3, sticky="e")

# Create the dropdown/OptionMenus
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
variable3 = tk.StringVar(root)
variable4 = tk.StringVar(root)
variable5 = tk.StringVar(root)
variable6 = tk.StringVar(root)
variable7 = tk.StringVar(root)
variable8 = tk.StringVar(root)
variable9 = tk.StringVar(root)
variable10 = tk.StringVar(root)
variable11 = tk.StringVar(root)
variable12 = tk.StringVar(root)
variable13 = tk.StringVar(root)
variable14 = tk.StringVar(root)
variable15 = tk.StringVar(root)

# Extra Space added to help align menuoption widgets
optionsx = ["Please Select a Category                        ", "ACTION Correctly Assigned", "ACTION Correctly Derived",
            "ACTION Incorrectly Assigned", "ACTION Incorrectly Derived", "ACTION Not Assigned Or Derived",
            "ANALYST Correctly Assigned", "ANALYST Correctly Derived", "ANALYST Incorrectly Assigned",
            "ANALYST Incorrectly Derived", "ANALYST Not Assigned Or Derived", "BIO BUT NO PPLM", "NO BIO ON TERMINAL",
            "PRIMARY TICKER Correctly Assigned", "PRIMARY TICKER Correctly Derived",
            "PRIMARY TICKER Incorrectly Assigned", "PRIMARY TICKER Incorrectly Derived",
            "PRIMARY TICKER Not Assigned Or Derived", "RATING Correctly Assigned", "RATING Correctly Derived",
            "RATING Incorrectly Assigned", "RATING Incorrectly Derived", "RATING Not Assigned Or Derived",
            "TOPIC Correctly Assigned", "TOPIC Correctly Derived", "TOPIC Incorrectly Assigned",
            "TOPIC Incorrectly Derived", "TOPIC Not Assigned Or Derived"]

variable1.set(optionsx[0])
variable2.set(optionsx[0])
variable3.set(optionsx[0])
variable4.set(optionsx[0])
variable5.set(optionsx[0])
variable6.set(optionsx[0])
variable7.set(optionsx[0])
variable8.set(optionsx[0])
variable9.set(optionsx[0])
variable10.set(optionsx[0])
variable11.set(optionsx[0])
variable12.set(optionsx[0])
variable13.set(optionsx[0])
variable14.set(optionsx[0])
variable15.set(optionsx[0])

# splitsup the list of options
s = [a for a in optionsx]

C1 = OptionMenu(*(root, variable1) + tuple(optionsx))
C2 = OptionMenu(*(root, variable2) + tuple(optionsx))
C3 = OptionMenu(*(root, variable3) + tuple(optionsx))
C4 = OptionMenu(*(root, variable4) + tuple(optionsx))
C5 = OptionMenu(*(root, variable5) + tuple(optionsx))
C6 = OptionMenu(*(root, variable6) + tuple(optionsx))
C7 = OptionMenu(*(root, variable7) + tuple(optionsx))
C8 = OptionMenu(*(root, variable8) + tuple(optionsx))
C9 = OptionMenu(*(root, variable9) + tuple(optionsx))
C10 = OptionMenu(*(root, variable10) + tuple(optionsx))
C11 = OptionMenu(*(root, variable11) + tuple(optionsx))
C12 = OptionMenu(*(root, variable12) + tuple(optionsx))
C13 = OptionMenu(*(root, variable13) + tuple(optionsx))
C14 = OptionMenu(*(root, variable14) + tuple(optionsx))
C15 = OptionMenu(*(root, variable15) + tuple(optionsx))

C1.configure(bg="Light Yellow")
C2.configure(bg="Light Yellow")
C3.configure(bg="Light Yellow")
C4.configure(bg="Light Yellow")
C5.configure(bg="Light Yellow")
C6.configure(bg="Light Yellow")
C7.configure(bg="Light Yellow")
C8.configure(bg="Light Yellow")
C9.configure(bg="Light Yellow")
C10.configure(bg="Light Yellow")
C11.configure(bg="Light Yellow")
C12.configure(bg="Light Yellow")
C13.configure(bg="Light Yellow")
C14.configure(bg="Light Yellow")
C15.configure(bg="Light Yellow")

# create labels and entry boxes
SUIDL = Label(root, text="SUID")
SUIDE = Entry(root)
CONTRIBL = Label(root, text="Contributor")
CONTRIBE = Entry(root)
WCL = Label(root, text="Wire")
WCE = Entry(root, width="5")

T1 = Text(root, height=1, width=70)
T2 = Text(root, height=1, width=70)
T3 = Text(root, height=1, width=70)
T4 = Text(root, height=1, width=70)
T5 = Text(root, height=1, width=70)
T6 = Text(root, height=1, width=70)
T7 = Text(root, height=1, width=70)
T8 = Text(root, height=1, width=70)
T9 = Text(root, height=1, width=70)
T10 = Text(root, height=1, width=70)
T11 = Text(root, height=1, width=70)
T12 = Text(root, height=1, width=70)
T13 = Text(root, height=1, width=70)
T14 = Text(root, height=1, width=70)
T15 = Text(root, height=1, width=70)

L1 = Label(root, text="NI Code 1  ")
L2 = Label(root, text="NI Code 2  ")
L3 = Label(root, text="NI Code 3  ")
L4 = Label(root, text="NI Code 4  ")
L5 = Label(root, text="NI Code 5  ")
L6 = Label(root, text="NI Code 6  ")
L7 = Label(root, text="NI Code 7  ")
L8 = Label(root, text="NI Code 8  ")
L9 = Label(root, text="NI Code 9  ")
L10 = Label(root, text="NI Code 10 ")
L11 = Label(root, text="NI Code 11 ")
L12 = Label(root, text="NI Code 12 ")
L13 = Label(root, text="NI Code 13 ")
L14 = Label(root, text="NI Code 14 ")
L15 = Label(root, text="NI Code 15 ")
LNotes = Label(root, text="Notes - OPTIONAL")

E1 = Entry(root)
E2 = Entry(root)
E3 = Entry(root)
E4 = Entry(root)
E5 = Entry(root)
E6 = Entry(root)
E7 = Entry(root)
E8 = Entry(root)
E9 = Entry(root)
E10 = Entry(root)
E11 = Entry(root)
E12 = Entry(root)
E13 = Entry(root)
E14 = Entry(root)
E15 = Entry(root)

# Add the widgets to the screen via GRID controls
# A little space at top
Spacer1 = Label(root, text="")
Spacer2 = Label(root, text="")
Spacer1.grid(row=0, column=0)

SUIDL.grid(row=1, column=0, sticky='e')
SUIDE.grid(row=1, column=1)
CONTRIBL.grid(row=2, column=0, sticky='e')
CONTRIBE.grid(row=2, column=1)
WCL.grid(row=3, column=0, sticky='e')
WCE.grid(row=3, column=1, sticky='w')

Spacer2.grid(row=3, column=0)
LNotes.grid(row=3, column=3, sticky="ew")

L1.grid(row=4, column=0)
E1.grid(row=4, column=1)
C1.grid(row=4, column=2, sticky="w")
T1.grid(row=4, column=3)

L2.grid(row=5, column=0)
E2.grid(row=5, column=1)
C2.grid(row=5, column=2, sticky="w")
T2.grid(row=5, column=3)

L3.grid(row=6, column=0)
E3.grid(row=6, column=1)
C3.grid(row=6, column=2, sticky="w")
T3.grid(row=6, column=3)

L4.grid(row=7, column=0)
E4.grid(row=7, column=1)
C4.grid(row=7, column=2, sticky="w")
T4.grid(row=7, column=3)

L5.grid(row=8, column=0)
E5.grid(row=8, column=1)
C5.grid(row=8, column=2, sticky="w")
T5.grid(row=8, column=3)

L6.grid(row=9, column=0)
E6.grid(row=9, column=1)
C6.grid(row=9, column=2, sticky="w")
T6.grid(row=9, column=3)

L7.grid(row=10, column=0)
E7.grid(row=10, column=1)
C7.grid(row=10, column=2, sticky="w")
T7.grid(row=10, column=3)

L8.grid(row=11, column=0)
E8.grid(row=11, column=1)
C8.grid(row=11, column=2, sticky="w")
T8.grid(row=11, column=3)

L9.grid(row=12, column=0)
E9.grid(row=12, column=1)
C9.grid(row=12, column=2, sticky="w")
T9.grid(row=12, column=3)

L10.grid(row=13, column=0)
E10.grid(row=13, column=1)
C10.grid(row=13, column=2, sticky="w")
T10.grid(row=13, column=3)

L11.grid(row=14, column=0)
E11.grid(row=14, column=1)
C11.grid(row=14, column=2, sticky="w")
T11.grid(row=14, column=3)

L12.grid(row=15, column=0)
E12.grid(row=15, column=1)
C12.grid(row=15, column=2, sticky="w")
T12.grid(row=15, column=3)

L13.grid(row=16, column=0)
E13.grid(row=16, column=1)
C13.grid(row=16, column=2, sticky="w")
T13.grid(row=16, column=3)

L14.grid(row=17, column=0)
E14.grid(row=17, column=1)
C14.grid(row=17, column=2, sticky="w")
T14.grid(row=17, column=3)

L15.grid(row=18, column=0)
E15.grid(row=18, column=1)
C15.grid(row=18, column=2, sticky="w")
T15.grid(row=18, column=3)


def close_window():
    root.destroy()


def get_sql_data(SQLstr):
    try:
        connstring = 'DRIVER={SQL Server};SERVER=myserver;DATABASE=mydatabase;UID=xxxyyyzzz;PWD=aaabbbccc'
        conn = pyodbc.connect(connstring)
        cursor = conn.cursor()
        cursor.execute(SQLstr)
        fileData = cursor.fetchall()
        cursor.close()
        return fileData
    except:
        return False


# NEED TO SET UP AS VARIABLES AND DETERMINE HOW TO LOOP THROUGH ONLY ITEMS WITH DATA
def send_sql_data():
    if E1.get() != "":
        myRecordID = RecordID
        myDate = Dt
        myRep = UName
        MyContrib = CONTRIBE.get()
        myWire = WCE.get()
        mySUID = SUIDE.get()
        connstring = 'DRIVER={SQL Server};SERVER=myserver;DATABASE=mydatabase;UID=xxxyyyzzz;PWD=aaabbbccc'
        SQLstr = "INSERT INTO [DCollection].[dbo].[Contribs] (RecordID, Date, Rep, Contrib, Wire, SUID, NICode, Category, Notes) VALUES ('111222333','2017-09-22','JP','NOMURA','122','asdfa32133923','MARTIAL','ThisCategory','Blah Notes');"
        conn = pyodbc.connect(connstring)
        cursor = conn.cursor()
        cursor.execute(SQLstr)
        cursor.close()
        conn.commit()


SubmitButton = Button(root, text="Submit", command=send_sql_data)
QuitButton = Button(root, text="Quit", command=close_window)
ClearButton = Button(root, text="ClearContent", command="")
# Place Buttons on Window
SubmitButton.place(x=1200, y=620)
QuitButton.place(x=10, y=620)
ClearButton.place(x=1285, y=620)

root.mainloop()