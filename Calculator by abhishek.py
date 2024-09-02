# Calculator by Abhishek jain
import tkinter as tk
from tkinter import *
from math import sqrt

# Main window setup
win = tk.Tk()

# Function for handling button input
def getdata(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# Function for handling square button
def square():
    try:
        current = float(entry.get())
        entry.delete(0, END)
        entry.insert(0, current ** 2)
    except ValueError:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Function for handling square root button
def square_root():
    try:
        current = float(entry.get())
        entry.delete(0, END)
        entry.insert(0, sqrt(current))
    except ValueError:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Function for handling clear button
def clear():
    entry.delete(0, END)

# Function for handling equals button
def equals():
    try:
        calculation = entry.get()
        calculation = clc_percentage(calculation)
        entry.delete(0, END)
        entry.insert(0, eval(calculation))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Function for handling Percentage calculation
def clc_percentage(expression):
    operators = ['+', '-', '*', '/']
    for operator in operators:
        if operator in expression:
            
            # split the operator

            parts = expression.split(operator)
            for i in range(len(parts)):
                part = parts[i].strip()
                
                # percentage calculation

                if '%' in part:
                    base_value = float(part.replace('%', ''))
                    percentage_value = base_value / 100
                    if i > 0:
                        if operator == '+':
                            parts[i] = str(float(parts[i-1]) * percentage_value)
                        elif operator == '-':
                            parts[i] = str(float(parts[i-1]) * percentage_value)
                        elif operator == '*':
                            parts[i] = str(float(parts[i-1]) * percentage_value)
                        elif operator == '/':
                            parts[i] = str(float(parts[i-1]) * percentage_value)
            return operator.join(parts)
    return expression

# Function for handling backspace button
def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])

# Main window configuration
win.geometry("325x500+50+50")
win.title("Calculator by Abhishek Jain")
win.iconbitmap("clc.ico")
win["bg"]= "black"
win.resizable(False, False)

# Entry widget
entry = Entry(win, relief="sunken", font=("Times New Roman", 50, "bold"), bd=5, justify='right')
entry.place(x=10, y=10, height=90, width=305)

# Button placement in First Row
button_AC = Button(win, text="AC", font=("Times New Roman", 24, "bold"), bd=2, bg="#f53636", command=clear)
button_AC.place(x=10, y=105, height=60, width=72.5)

button_sq = Button(win, text="x²", font=("Times New Roman", 24, "bold"), bd=2, bg="#36f5e9", command=square)
button_sq.place(x=87.5, y=105, height=60, width=72.5)

button_sqroot = Button(win, text="√x", font=("Yu Gothic UI Semibold", 24, "bold"), bd=2, bg="#36f5e9", command=square_root)
button_sqroot.place(x=165, y=105, height=60, width=72.5)

button_del = Button(win, text="⇦", font=("Yu Gothic UI Semibold", 24, "bold"), bd=2, bg="orange", command=backspace)
button_del.place(x=242.5, y=105, height=60, width=72.5)

#--------------------------------------------------------------------------------------------------
# Button placement in Second Row

button_per = Button(win, text="%", font=("Times New Roman", 24, "bold"), bd=2, bg="#36f5e9", command=lambda: getdata('%'))
button_per.place(x=10, y=170, height=60, width=72.5)

button_div = Button(win, text="÷", font=("Yu Gothic UI Semibold", 24, "bold"), bd=2, bg="#36f5e9", command=lambda: getdata('/'))
button_div.place(x=87.5, y=170, height=60, width=72.5)

button_mul = Button(win, text="×", font=("Times New Roman", 24, "bold"), bd=2, bg="#36f5e9", command=lambda: getdata('*'))
button_mul.place(x=165, y=170, height=60, width=72.5)

button_sub = Button(win, text="-", font=("Times New Roman", 24, "bold"), bd=2, bg="#36f5e9", command=lambda: getdata('-'))
button_sub.place(x=242.5, y=170, height=60, width=72.5)

#--------------------------------------------------------------------------------------------------
# Button placement in Third Row

button_7 = Button(win, text="7", font=("Times New Roman", 24, "bold"),bg= "white", bd=2, command=lambda: getdata(7))
button_7.place(x=10, y=235, height=60, width=72.5)

button_8 = Button(win, text="8", font=("Times New Roman", 24, "bold"),bg= "white", bd=2, command=lambda: getdata(8))
button_8.place(x=87.5, y=235, height=60, width=72.5)

button_9 = Button(win, text="9", font=("Times New Roman", 24, "bold"),bg= "white", bd=2, command=lambda: getdata(9))
button_9.place(x=165, y=235, height=60, width=72.5)

button_add = Button(win, text="+", font=("Times New Roman", 24, "bold"), bd=2, bg="#36f5e9", command=lambda: getdata('+'))
button_add.place(x=242.5, y=235, height=125, width=72.5)

#--------------------------------------------------------------------------------------------------
# Button placement in Forth Row

button_4 = Button(win, text="4", font=("Times New Roman", 24, "bold"), bg= "white", bd=2, command=lambda: getdata(4))
button_4.place(x=10, y=300, height=60, width=72.5)

button_5 = Button(win, text="5", font=("Times New Roman", 24, "bold"),bg= "white", bd=2, command=lambda: getdata(5))
button_5.place(x=87.5, y=300, height=60, width=72.5)

button_6 = Button(win, text="6", font=("Times New Roman", 24, "bold"),bg= "white", bd=2, command=lambda: getdata(6))
button_6.place(x=165, y=300, height=60, width=72.5)

#--------------------------------------------------------------------------------------------------
# Button placement in Fifth Row

button_1 = Button(win, text="1", font=("Times New Roman", 24, "bold"),bg= "white", bd=2, command=lambda: getdata(1))
button_1.place(x=10, y=365, height=60, width=72.5)

button_2 = Button(win, text="2", font=("Times New Roman", 24, "bold"),bg= "white", bd=2, command=lambda: getdata(2))
button_2.place(x=87.5, y=365, height=60, width=72.5)

button_3 = Button(win, text="3", font=("Times New Roman", 24, "bold"),bg= "white", bd=2, command=lambda: getdata(3))
button_3.place(x=165, y=365, height=60, width=72.5)

button_equal = Button(win, text="=", font=("Times New Roman", 24, "bold"), bd=2, fg="#36caf5", bg="#3697f5", command=equals)
button_equal.place(x=242.5, y=365, height=125, width=72.5)

#--------------------------------------------------------------------------------------------------
# Button placement in Sixth Row

button_0 = Button(win, text="0", font=("Times New Roman", 24, "bold"),bg= "white", bd=2, command=lambda: getdata(0))
button_0.place(x=10, y=430, height=60, width=150)

button_dec = Button(win, text=".", font=("Times New Roman", 24, "bold"),bg= "white", bd=2, command=lambda: getdata('.'))
button_dec.place(x=165, y=430, height=60, width=72.5)

# Start the GUI event loop
win.mainloop()
