import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 as sq

LARGE_FONT = ("Verdana", 12)


class JobCardSystem(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="JE.ico")
        tk.Tk.wm_title(self, "Jabil Job Card System")
        container = tk.Frame(self, height=1080, width=1920, relief='raised', borderwidth=5)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, CustomerDB, NewCustomerPage, CreateJob, JobsDB):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def hello():
    print("hello!")


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.root.columnconfigure(0, weight=0)
        self.root.rowconfigure(0, weight=0)

        menubar = tk.Menu(self.root)

        # create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Create a New Customer", command=lambda: controller.show_frame(NewCustomerPage))
        filemenu.add_command(label="View Customers Database", command=lambda: controller.show_frame(CustomerDB))
        filemenu.add_command(label="Create New Job", command=lambda: controller.show_frame(CreateJob))
        filemenu.add_command(label="View Jobs Database", command=lambda: controller.show_frame(JobsDB))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=print('NO!'))
        menubar.add_cascade(label="Help", menu=helpmenu)

        # display the menu
        main_frame = tk.Frame(self, width=1600, height=800)
        main_frame.columnconfigure(0, weight=0)
        main_frame.rowconfigure(0, weight=0)
        main_frame.grid(row=0, column=0)
        controller.config(menu=menubar)

        photo1 = tk.PhotoImage(file="Jabil.gif")
        label1 = tk.Label(self, image=photo1)
        label1.image = photo1
        label1.grid(row=0, column=0)


class CustomerDB(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PageOne", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        tree = ttk.Treeview(self, column=("column1", "column2", "column3", "column4", "column5", "column6",
                                          "column7", "column8", "column9"), show='headings')
        tree.heading("#1", text="Customer ID")
        tree.heading("#2", text="Customer name")
        tree.heading("#3", text="Address 1")
        tree.heading("#4", text="Address 2")
        tree.heading("#5", text="Region")
        tree.heading("#6", text="Contact Name")
        tree.heading("#7", text="Contact Surname")
        tree.heading("#8", text="Office Number")
        tree.heading("#9", text="Mobile Number")
        tree.pack(fill='both', expand=True)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="CustomerDB", command=lambda: controller.show_frame(CustomerDB))
        button2.pack()
        button3 = ttk.Button(self, text="Create New Customer", command=lambda: controller.show_frame(NewCustomerPage))
        button3.pack()
        button4 = ttk.Button(self, text="Create New Job", command=lambda: controller.show_frame(CreateJob))
        button4.pack()

        con = sq.connect("jobcard.db")
        c = con.cursor()
        c.execute("SELECT * FROM Customers")
        rows = c.fetchall()
        for row in rows:
            #print(row)  # it print all records in the database
            tree.insert("", tk.END, values=row)
            #row_number = rows[0][0]
            #print(row_number)
        con.close()


class JobsDB(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="JobsDB", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        tree = ttk.Treeview(self, column=("column1", "column2", "column3", "column4", "column5", "column6",
                                          "column7", "column8", "column9"), show='headings')
        tree.heading("#1", text="Customer Name")
        tree.heading("#2", text="Unit")
        tree.heading("#3", text="Customer Region")
        tree.heading("#4", text="Parts")
        tree.heading("#5", text="Jab Start Date")
        tree.heading("#6", text="Job ETA Date")
        tree.heading("#7", text="Job Fault Description")
        tree.heading("#8", text="Job Notes")
        tree.pack(fill='both', expand=True)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="CustomerDB", command=lambda: controller.show_frame(CustomerDB))
        button2.pack()
        button3 = ttk.Button(self, text="Create New Customer", command=lambda: controller.show_frame(NewCustomerPage))
        button3.pack()
        button4 = ttk.Button(self, text="Create New Job", command=lambda: controller.show_frame(CreateJob))
        button4.pack()

        con = sq.connect("jobcard.db")
        c = con.cursor()
        c.execute("SELECT * FROM Jobs")
        rows = c.fetchall()
        i = 0
        for row in rows:
            #print(row)  # it print all records in the database
            tree.insert("", tk.END, values=row)
            customers_id = rows[i]
        #print(customers_id[i])
        i = i + 1
        con.close()

class NewCustomerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Customer Entry", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        con = sq.connect('jobcard.db')  # dB browser for sqlite needed
        c = con.cursor()  # SQLite command, to connect to db so 'execute' method can be called

        l1 = tk.Label(self, text="Customer Name:", font=("arial", 18))
        l1.place(x=10, y=100)
        l2 = tk.Label(self, text="Customer Address 1:", font=("arial", 18))
        l2.place(x=10, y=150)
        l3 = tk.Label(self, text="Customer Address 2:", font=("arial", 18))
        l3.place(x=10, y=200)
        l4 = tk.Label(self, text="Name:", font=("arial", 18))
        l4.place(x=10, y=250)
        l5 = tk.Label(self, text="Surname:", font=("arial", 18))
        l5.place(x=10, y=300)
        l6 = tk.Label(self, text="Office Number:", font=("arial", 18))
        l6.place(x=10, y=350)
        l7 = tk.Label(self, text="Mobile Number:", font=("arial", 18))
        l7.place(x=10, y=450)
        l8 = tk.Label(self, text="Region:", font=("arial", 18))
        l8.place(x=10, y=450)

        # Create variables for each list
        cust = tk.StringVar(self)  # For 1st dd
        cust.set('Customers')  # Inital placeholder for field

        custdb = tk.StringVar(self)  # 2nd dropdown list
        custdb.set('Customers')

        cust_name = tk.StringVar(self)
        cust_add1 = tk.StringVar(self)
        cust_add2 = tk.StringVar(self)
        main_name = tk.StringVar(self)
        main_surname = tk.StringVar(self)
        main_office = tk.StringVar(self)
        main_mobile = tk.StringVar(self)
        cust_region = tk.StringVar(self)

        # Entry for 'input' in GUI
        cust_name_e = tk.Entry(self, textvariable=cust_name)
        cust_name_e.place(x=250, y=105)

        cust_add1_e = tk.Entry(self, textvariable=cust_add1)
        cust_add1_e.place(x=250, y=155)

        cust_add2_e = tk.Entry(self, textvariable=cust_add2)
        cust_add2_e.place(x=250, y=205)

        main_name_e = tk.Entry(self, textvariable=main_name)
        main_name_e.place(x=250, y=255)

        main_surname_e = tk.Entry(self, textvariable=main_surname)
        main_surname_e.place(x=250, y=305)

        main_office_e = tk.Entry(self, textvariable=main_office)
        main_office_e.place(x=250, y=355)

        main_mobile_e = tk.Entry(self, textvariable=main_mobile)
        main_mobile_e.place(x=250, y=405)

        cust_region_e = tk.Entry(self, textvariable=cust_region)
        cust_region_e.place(x=250, y=455)

        # get func to isolate the text entered in the entry boxes and submit to database
        def get():
            print("You have submitted a record")

            c.execute(
                'CREATE TABLE IF NOT EXISTS ' + cust.get() + '( cus_name TEXT, cus_add1 TEXT, cus_add2 TEXT, '
                                                             'cus_region TEXT, main_name TEXT, main_surname TEXT, '
                                                             'main_office_num TEXT, main_mobile_num TEXT)')  # SQL
            # syntax

            c.execute(
                'INSERT INTO ' + cust.get() + '(cus_name, cus_add1, cus_add2, cus_region, main_name, main_surname, '
                                              'main_office_num, main_mobile_num) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (cust_name.get(), cust_add1.get(), cust_add2.get(), cust_region.get(), main_name.get(),
                 main_surname.get(), main_office.get(), main_mobile.get()))  # Insert record into database.
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

        button_submit = ttk.Button(self, text="Submit", command=get)
        button_submit.place(x=100, y=500)

        button_clear = ttk.Button(self, text="Clear", command=clear)
        button_clear.place(x=180, y=500)

        button_opendb = ttk.Button(self, text="Open DB", command=lambda: controller.show_frame(CustomerDB))
        button_opendb.place(x=10, y=500)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.place(x=250, y=500)


class CreateJob(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Create a New Job", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        con = sq.connect('jobcard.db')  # dB browser for sqlite needed
        c = con.cursor()  # SQLite command, to connect to db so 'execute' method can be called
        c.execute("PRAGMA foreign_keys = ON")

        l1 = tk.Label(self, text="Customer Name:", font=("arial", 18))
        l1.place(x=10, y=100)
        l2 = tk.Label(self, text="Unit:", font=("arial", 18))
        l2.place(x=10, y=150)
        l3 = tk.Label(self, text="Region:", font=("arial", 18))
        l3.place(x=10, y=200)
        l4 = tk.Label(self, text="Parts:", font=("arial", 18))
        l4.place(x=10, y=250)
        l5 = tk.Label(self, text="Job Start Date:", font=("arial", 18))
        l5.place(x=10, y=300)
        l6 = tk.Label(self, text="ETA Date:", font=("arial", 18))
        l6.place(x=10, y=350)
        l7 = tk.Label(self, text="Fault Description:", font=("arial", 18))
        l7.place(x=10, y=400)
        l8 = tk.Label(self, text="Additional Notes:", font=("arial", 18))
        l8.place(x=10, y=450)

        def callback(c_name):
            con = sq.connect('jobcard.db')  # dB browser for sqlite needed
            c = con.cursor()  # SQLite command, to connect to db so 'execute' method can be called
            cn = str(c_name)
            c.execute("SELECT * FROM Customers WHERE cus_name=?", (cn,))
            c_num = c.fetchall()
            print(c_name)
            print(c_num)


        # Create variables for each list
        jobs = tk.StringVar(self)  # For Job Table
        jobs.set('Jobs')
        cust = tk.StringVar(self)  # For 1st dd
        cust.set('Customers')  # Inital placeholder for field
        c.execute("SELECT cus_name FROM Customers")
        custdb = c.fetchall()

        cust_name = tk.StringVar(self)
        job_unit = tk.StringVar(self)
        job__region = tk.StringVar(self)
        job__parts = tk.StringVar(self)
        job__start = tk.StringVar(self)
        job__e_t_a = tk.StringVar(self)
        job__fault = tk.StringVar(self)
        job__notes = tk.StringVar(self)

        # Entry for 'input' in GUI
        cust_name_e = tk.OptionMenu(self, cust, *custdb, command=callback)
        cust_name_e.place(x=250, y=105)

        job_unit_e = tk.Entry(self, textvariable=job_unit)
        job_unit_e.place(x=250, y=155)

        job__region_e = tk.Entry(self, textvariable=job__region)
        job__region_e.place(x=250, y=205)

        job_parts_e = tk.Entry(self, textvariable=job__parts)
        job_parts_e.place(x=250, y=255)

        job_start_e = tk.Entry(self, textvariable=job__start)
        job_start_e.place(x=250, y=305)

        job_eta_e = tk.Entry(self, textvariable=job__e_t_a)
        job_eta_e.place(x=250, y=355)

        job_fault_e = tk.Entry(self, textvariable=job__fault)
        job_fault_e.place(x=250, y=405)

        job_notes_e = tk.Entry(self, textvariable=job__notes)
        job_notes_e.place(x=250, y=455)

        # get func to isolate the text entered in the entry boxes and submit to database
        def get():
            print("You have submitted a record")

            c.execute(
                'CREATE TABLE IF NOT EXISTS ' + jobs.get() + '( cus_name TEXT NOT NULL, job_unit TEXT NOT NULL, '
                                                             'job__region TEXT NOT NULL, job__parts TEXT,'' job__start '
                                                             'TEXT NOT NULL, job__e_t_a TEXT NOT NULL, job__fault TEXT '
                                                             'NOT NULL, job__notes TEXT,'' FOREIGN KEY(cus_name) '
                                                             'REFERENCES Customers(cus_id) ON DELETE CASCADE)')

            c.execute(
                'INSERT INTO ' + jobs.get() + '(cus_name, job_unit, job__region, job__parts, job__start, job__e_t_a, '
                                              'job__fault, job__notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (cust_name.get(), job_unit.get(), job__region.get(), job__parts.get(), job__start.get(),
                 job__e_t_a.get(), job__fault.get(), job__notes.get()))  # Insert record into database.
            con.commit()

            # Reset fields after submit
            cust_name.set('')
            job_unit.set('')
            job__region.set('')
            job__parts.set('')
            job__start.set('')
            job__e_t_a.set('')
            job__fault.set('')
            job__notes.set('')

        # Clear boxes when submit button is hit
        def clear():
            cust_name.set('')
            job_unit.set('')
            job__region.set('')
            job__parts.set('')
            job__start.set('')
            job__e_t_a.set('')
            job__fault.set('')
            job__notes.set('')

        button_submit = ttk.Button(self, text="Submit", command=get)
        button_submit.place(x=100, y=500)

        button_clear = ttk.Button(self, text="Clear", command=clear)
        button_clear.place(x=180, y=500)

        button_opendb = ttk.Button(self, text="Open DB", command=lambda: controller.show_frame(JobsDB))
        button_opendb.place(x=10, y=500)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.place(x=250, y=500)


app = JobCardSystem()
app.mainloop()
