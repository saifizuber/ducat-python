import tkinter as tk




top = tk.Tk()
top.geometry('1200x600')

# Create the labels and entry widgets
l = tk.Label(top, text='Login', bg='green', fg='white', font=('Arial', 30, 'bold'))
l.place(x=500, y=50)

l2 = tk.Label(top, text='Name', bg='green', fg='white', font=('Arial', 20, 'bold'))
l2.place(x=300, y=200)
e1 = tk.Entry(top, font=('Arial', 20, 'bold'))
e1.place(x=400, y=200)

l3 = tk.Label(top, text='Age', bg='green', fg='white', font=('Arial', 20, 'bold'))
l3.place(x=300, y=250)
e2 = tk.Entry(top, font=('Arial', 20, 'bold'))
e2.place(x=400, y=250)



# Create the submit button


b3 = tk.Button(top, text='Login', font=('Arial', 20, 'bold'))
b3.place(x=400, y=300)

top.config(bg='green')
top.mainloop()