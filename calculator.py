from tkinter import *
from math import*

root = Tk()
root.geometry("415x346")
# defining the title
root.title("calculator ")
root.config(background="light blue")
root.iconbitmap('C:/Users/ASUS/Downloads/a.ico')

entry = Entry(root, width=40,borderwidth=15)
entry.grid(row = 0,column=0, columnspan=3,  padx=10, pady=10)



def  click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def clear():
    entry.delete(0, END)

def add():
    first_number = entry.get()
    global f_num
    global math
    math="addition"
    f_num = int(first_number)
    entry.delete(0, END)


def multiply ():
    first_num= entry.get()
    global f_num
    global math
    math="Multiplication"
    f_num = int(first_num)
    entry.delete(0,END)

def substraction ():
    first_num= entry.get()
    global f_num
    global math
    math="substraction"
    f_num = int(first_num)
    entry.delete(0,END)

def divide ():
    first_num= entry.get()
    global f_num
    global math
    math ="division"
    f_num = int(first_num)
    entry.delete(0,END)

def equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math =="addition":
        entry.insert(0, f_num + int(second_number))
    elif math =="Multiplication":
        entry.insert(0,f_num * int(second_number))
    elif math =="substraction":
        entry.insert(0,f_num - int(second_number))
    elif math =="division":
        entry.insert(0,f_num / int(second_number))

# defining buttons
button1 = Button(root, text='1', fg='black', bg='light green',padx=40, pady=20,borderwidth=5,command=lambda: click(1))
button2 = Button(root, text='2', fg='black', bg='light green',padx=40, pady=20 ,borderwidth=5,command=lambda: click(2))
button3 = Button(root, text='3', fg='black', bg='light green',padx=44, pady=20, borderwidth=5,command=lambda: click(3))
button4 = Button(root, text='4', fg='black', bg='light green', padx=40, pady=20,borderwidth=5, command=lambda: click(4))
button5 = Button(root, text='5', fg='black', bg='light green',padx=40, pady=20,borderwidth=5,command=lambda: click(5))
button6 = Button(root, text='6', fg='black', bg='light green',padx=44, pady=20,borderwidth=5,command=lambda: click(6))

button7 = Button(root, text='7', fg='black', bg='light green',padx=40, pady=20,borderwidth=5,command=lambda: click(7))
button8 = Button(root, text='8', fg='black', bg='light green',padx=40, pady=20,borderwidth=5,command=lambda: click(8))
button9 = Button(root, text='9', fg='black', bg='light green',padx=45, pady=20,borderwidth=5,command=lambda: click(9))
button0 = Button(root, text='0', fg='black', bg='light green',padx=40, pady=20,borderwidth=5,command=lambda: click(0))
add = Button(root, text=' + ', fg='black', bg='orange',padx=35,borderwidth=5, pady=20, command=add)
equal = Button(root, text=' = ', fg='black', bg='orange',padx=40,borderwidth=5, pady=20,command=equal)
clear = Button(root, text='Clear', fg='black', bg='orange',padx=30, pady=20,borderwidth=5, command=clear)

multiply = Button(root, text='*', fg='black', bg= 'orange', padx=40, pady=20,borderwidth=5, command=multiply)
substraction = Button(root, text='-', fg='black', bg= 'orange', padx=40, pady=20,borderwidth=5, command=substraction)
divide = Button(root, text='/', fg='black', bg= 'orange', padx=40, pady=20,borderwidth=5,command=divide)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=1)
add.grid(row=1, column=3)
equal.grid(row=4, column=2)
clear.grid(row=4, column=0)
multiply.grid(row =2, column=3)
substraction.grid(row =3, column=3)
divide.grid(row =4, column=3)
# start the GUI
root.mainloop()


