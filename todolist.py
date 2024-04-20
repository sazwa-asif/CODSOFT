#IMPORTING MODULES
from tkinter import *
from tkinter import messagebox

#FUNCTION FOR ADDING NEW TASK
def new_task():
    task = task_entry.get()
    if task != "":
        list_box.insert(END, task)
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

#FUNCTION FOR DELETING TASK
def delete_task():
    if list_box.curselection():
        list_box.delete(ANCHOR)
    else:
        messagebox.showinfo("Info", "No task selected.")

#FUNCTION FOR MARKING TASK AS DONE AFTER COMPLETION
def mark_as_done():
    if list_box.curselection():
        index = list_box.curselection()[0]
        task = list_box.get(index)
        if task.startswith("✓ "):
            task = task[2:]
        else:
            task = "✓ " + task
        list_box.delete(index)
        list_box.insert(index, task)
    else:
        messagebox.showinfo("Info", "No task selected.")

#FUNCTION FOR SAVING LIST
def save_list():
    with open("to_do_list.txt", "w") as file:
        for task in list_box.get(0, END):
            file.write(task + "\n")
    messagebox.showinfo("Info", "To-do list saved successfully!")

#SETTING UP GUI FOR TO DO LIST
root = Tk()
root.geometry("450x450")
root.title("To Do List")
root.config(bg="#2F3C7E")
root.resizable(width=False, height=False)

heading = Label(root, text="TO-DO LIST", font=("Arial Black", 24, "bold"), fg="#FFB5C5", bg="#2F3C7E")
heading.pack(side=TOP, anchor=CENTER)

frame = Frame(root)
frame.pack(pady=10)

list_box = Listbox(frame, width=25, height=8, font=("Arial Black", 14, "bold"), bd=0, fg='#2F3C7E',
                   highlightthickness=0, activestyle="none")
list_box.pack(side=LEFT, fill=BOTH)

scroll_bar = Scrollbar(frame)
scroll_bar.pack(side=RIGHT, fill=BOTH)

list_box.config(yscrollcommand=scroll_bar.set, bg="#FFB5C5")
scroll_bar.config(command=list_box.yview)

task_entry = Entry(root, font=("Arial Black", 14, "bold"), fg="#2F3C7E", bg="#FFB5C5")
task_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

add_button = Button(button_frame, text='ADD TASK', font=("Arial black", 10, "bold"), bg='#FFB5C5', fg="#2F3C7E",
                    padx=3, pady=3, command=new_task)
add_button.pack(fill=BOTH, expand=True, side=LEFT)

delete_button = Button(button_frame, text='DELETE TASK', font=("Arial black",10, "bold"), bg='#FFB5C5',
                       fg="#2F3C7E",
                       padx=3, pady=3, command=delete_task)
delete_button.pack(fill=BOTH, expand=True, side=LEFT)

done_button = Button(button_frame, text='MARK AS DONE', font=("Arial black", 10, "bold"), bg='#FFB5C5', fg="#2F3C7E",
                     padx=3, pady=3 ,command=mark_as_done)
done_button.pack(fill=BOTH, expand=True, side=LEFT)

save_button = Button(button_frame, text='SAVE LIST', font=("Arial black", 10, "bold"), bg='#FFB5C5', fg="#2F3C7E",
                     padx=3, pady=3, command=save_list)
save_button.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()

