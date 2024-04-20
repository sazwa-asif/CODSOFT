# IMPORTING MODULE
from tkinter import *

# SETTING UP GUI FOR CALCULATOR
root = Tk()
root.geometry("350x370")
root.resizable(False, False)
root.title("Calculator")
root.config(bg="#2A3132")

#FUNCTION FOR ENSURING NUMERICAL INPUT IS BEING MADE
def button_click(item):
    global expression
    if str(item).isdigit() or str(item) == '.' or str(item) in ['+', '-', '*', '/']:
        expression = expression + str(item)
        input_text.set(expression)
    else:
        if any(char.isalpha() for char in str(item)):
            input_text.set("Error: Invalid input")
        else:
            input_text.set("Error: Invalid input")
    input_field.icursor(len(input_field.get()))

# FOLLOWING ARE FUNCTIONS FOR DIFFERENT OPERATORS
def button_clear():
    global expression
    expression = ""
    input_text.set("")
    input_field.icursor(len(input_field.get()))

def button_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
    input_field.icursor(len(input_field.get()))

expression = ""

input_text = StringVar()

input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#D3C5E5", bd=6,
                    justify=RIGHT, relief=SUNKEN)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

buttons_frame = Frame(root, width=400, height=300, bg="#2A3132")
buttons_frame.pack()

# FIRST ROW OF CALCULATOR
clear = Button(buttons_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#735DA5", cursor="hand2",
               command=lambda: button_clear(),font=("Arial",8,"bold"))
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#735DA5", cursor="hand2",
                command=lambda: button_click("/"),font=("Arial",8,"bold"))
divide.grid(row=0, column=3, padx=4, pady=4)

# SECOND ROW OF CALCULATOR
seven = Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#D3C5E5", cursor="hand2",
               command=lambda: button_click(7),font=("Arial",8,"bold"))
seven.grid(row=1, column=0, padx=4, pady=4)

eight = Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#D3C5E5", cursor="hand2",
               command=lambda: button_click(8),font=("Arial",8,"bold"))
eight.grid(row=1, column=1, padx=4, pady=4)

nine = Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#D3C5E5", cursor="hand2",
              command=lambda: button_click(9),font=("Arial",8,"bold"))
nine.grid(row=1, column=2, padx=4, pady=4)

multiply = Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#735DA5", cursor="hand2",
                  command=lambda: button_click("*"),font=("Arial",8,"bold"))
multiply.grid(row=1, column=3, padx=4, pady=4)

# THIRD ROW OF CALCULATOR

four = Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#D3C5E5", cursor="hand2",
              command=lambda: button_click(4),font=("Arial",8,"bold"))
four.grid(row=2, column=0, padx=4, pady=4)

five = Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#D3C5E5", cursor="hand2",
              command=lambda: button_click(5),font=("Arial",8,"bold"))
five.grid(row=2, column=1, padx=4, pady=4)

six = Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#D3C5E5", cursor="hand2",
             command=lambda: button_click(6),font=("Arial",8,"bold"))
six.grid(row=2, column=2, padx=4, pady=4)

minus = Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#735DA5", cursor="hand2",
               command=lambda: button_click("-"),font=("Arial",8,"bold"))
minus.grid(row=2, column=3, padx=4, pady=4)

# FOURTH ROW OF CALCULATOR

one = Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#D3C5E5", cursor="hand2",
             command=lambda: button_click(1),font=("Arial",8,"bold"))
one.grid(row=3, column=0, padx=4, pady=4)

two = Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#D3C5E5", cursor="hand2",
             command=lambda: button_click(2),font=("Arial",8,"bold"))
two.grid(row=3, column=1, padx=4, pady=4)

three = Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#D3C5E5", cursor="hand2",
               command=lambda: button_click(3),font=("Arial",8,"bold"))
three.grid(row=3, column=2, padx=4, pady=4)

plus = Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#735DA5", cursor="hand2",
              command=lambda: button_click("+"),font=("Arial",8,"bold"))
plus.grid(row=3, column=3, padx=4, pady=4)

#FIFTH ROW OF CALCULATOR

zero = Button(buttons_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#735DA5", cursor="hand2",
              command=lambda: button_click(0),font=("Arial",8,"bold"))
zero.grid(row=4, column=0, columnspan=2, padx=4, pady=4)

point = Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#735DA5", cursor="hand2",
               command=lambda: button_click("."),font=("Arial",8,"bold"))
point.grid(row=4, column=2, padx=4, pady=4)

equal = Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#735DA5", cursor="hand2",
               command=lambda: button_equal(),font=("Arial",8,"bold"))
equal.grid(row=4, column=3, padx=4, pady=4)

root.mainloop()

