import tkinter as tk
import pymysql as sql
from tkinter import messagebox
from tkinter import ttk

def insert():
    k = e1.get()
    k2 = int(e2.get())
    k3 = int(e3.get())
    k4 = int(e4.get())

    db = sql.connect(host='localhost', user='root', password='zuber@2002', db='ConnectionTest')
    cursor = db.cursor()

    s = "INSERT INTO emp (name, age, salary, phone) VALUES (%s, %s, %s, %s)"
    row = cursor.execute(s, (k, k2, k3, k4))
    if(row>0):
        messagebox.showinfo("Result","Record insert successfully")

    else:
        messagebox.showinfo("Result","Record not inserted")

    e1.delete(0,'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')

    # Commit the changes and close the connection
    db.commit()
    db.close()

def Delete():
    k=e5.get()
    db = sql.connect(host='localhost', user='root', password='zuber@2002', db='ConnectionTest')
    cursor = db.cursor()
    cur = db.cursor()
    s="Delete from emp where name=%s"
    row=cur.execute(s,k)
    if (row > 0):
        messagebox.showinfo("Result", "Record Delete successfully")

    else:
        messagebox.showinfo("Result", "Record not Deleted")
    db.commit()


def show():
    top.destroy()
    import login


def search():
    k=e6.get()
    db = sql.connect(host='localhost', user='root', password='zuber@2002', db='ConnectionTest')
    cur = db.cursor()
    p = "select * from emp where name=%s"
    t=cur.execute(p,k)
    if (t>0):
        result = cur.fetchall()
        for i in result:
            name=i[0]
            age=i[1]
            salary=i[2]
            phone=i[3]
            print (name,age,salary,phone)
    else:
         messagebox.showinfo("Result","Record not found")


top = tk.Tk()
top.geometry('1500x600')




l = tk.Label(top, text='Registration', bg='green', fg='white', font=('Arial', 30, 'bold'))
l.place(x=500, y=50)

l2 = tk.Label(top, text='Name', bg='green', fg='white', font=('Arial', 20, 'bold'))
l2.place(x=300, y=200)
e1 = tk.Entry(top, font=('Arial', 20, 'bold'))
e1.place(x=400, y=200)

l3 = tk.Label(top, text='Age', bg='green', fg='white', font=('Arial', 20, 'bold'))
l3.place(x=300, y=250)
e2 = tk.Entry(top, font=('Arial', 20, 'bold'))
e2.place(x=400, y=250)

l4 = tk.Label(top, text='Salary', bg='green', fg='white', font=('Arial', 20, 'bold'))
l4.place(x=300, y=300)
e3 = tk.Entry(top, font=('Arial', 20, 'bold'))
e3.place(x=400, y=300)

l5 = tk.Label(top, text='Phone', bg='green', fg='white', font=('Arial', 20, 'bold'))
l5.place(x=300, y=350)
e4 = tk.Entry(top, font=('Arial', 20, 'bold'))
e4.place(x=400, y=350)

e5 = tk.Entry(top, font=('Arial', 20, 'bold'))
e5.place(x=750, y=200)


e6 = tk.Entry(top, font=('Arial', 20, 'bold'))
e6.place(x=800, y=400)

# Create the submit button
b1 = tk.Button(top, text='Submit', font=('Arial', 20, 'bold'), command=insert)
b1.place(x=500, y=400)

b2 = tk.Button(top, text='Delete', font=('Arial', 20, 'bold'), command=Delete)
b2.place(x=800, y=250)

b3 = tk.Button(top, text='Login', font=('Arial', 20, 'bold'), command=show)
b3.place(x=800, y=500)


b4 = tk.Button(top, text='Search', font=('Arial', 20, 'bold'), command=search)
b4.place(x=900, y=500)

top.config(bg='green')
top.mainloop()