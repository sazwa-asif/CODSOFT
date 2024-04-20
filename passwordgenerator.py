# IMPORTING MODULES
import random
import string
from tkinter import *
from tkinter import messagebox


# FUNCTION FOR GENERATING PASSWORD
def generate_password(length, use_special_chars):
    if use_special_chars:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password


# FUNCTION FOR DISPLAYING PASSWORD
def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive integer greater than 0.")
            return

        use_special_chars = use_special_chars_var.get()
        password = generate_password(length, use_special_chars)
        password_display.config(state="normal")
        password_display.delete(1.0, END)
        password_display.insert(END, password)
        password_display.config(state="disabled")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the length.")


# SETTING UP GUI FOR PASSWORD GENERATOR
root = Tk()
root.title("Password Generator")
root.config(bg="darkslategray")
root.geometry("500x250")
root.resizable(width=False, height=False)

frame1 = Frame(root, bg="darkslategray")
frame1.pack(side=TOP)
heading = Label(frame1, text="PASSWORD GENERATOR", font=("Arial Black", 24, "bold"), fg="#FCE6C9", bg="darkslategray")
heading.pack(side=TOP, anchor=CENTER)

frame2 = Frame(root, bg="darkslategray")
frame2.pack(pady=20)

length_label = Label(frame2, text="Enter the length of the password", font=("Arial Black", 12, "bold"), fg="#FCE6C9",
                     bg="darkslategray")
length_label.grid(row=0, column=0)

length_entry = Entry(frame2, font=("Arial", 12, "bold"), fg="darkslategray")
length_entry.grid(row=0, column=1, padx=10)

use_special_chars_var = BooleanVar()
use_special_chars_checkbox = Checkbutton(frame2, text="Include special characters", variable=use_special_chars_var,
                                         font=("Arial", 12,"bold"), fg="#FCE6C9", bg="darkslategray",selectcolor="green")
use_special_chars_checkbox.grid(row=1,column=0)

generate_button = Button(frame2, text="Generate Password", command=generate_and_display_password, font=("Arial", 12,"bold"),
                         bg="#FCE6C9", fg="darkslategray")
generate_button.grid(row=1,column=1,padx=10,pady=20)

password_display = Text(root, height=2, width=20, state="disabled", fg="darkslategray", font=("Arial", 14, "bold"))
password_display.pack()

root.mainloop()




