#IMPORTING MODULES
import tkinter as tk
from tkinter import messagebox

contacts = {}

#FUNCTION FOR ADDING CONTACTS
def add_contact():
    name = name_entry.get()
    contact = contact_entry.get()

    if name and contact:
        if name in contacts:
            messagebox.showerror("Error", "Contact already exists!")
        else:
            contacts[name] = contact
            messagebox.showinfo("Success", "Contact added successfully!")
            populate_listbox()
            name_entry.delete(0, tk.END)
            contact_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter name and contact!")

#FUNCTION FOR DELETING CONTACT
def delete_contact():
    selected_index = contacts_list.curselection()
    if selected_index:
        selected_contact = contacts_list.get(selected_index[0])
        name = selected_contact.split(":")[0].strip()

        if name in contacts:
            del contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            populate_listbox()
        else:
            messagebox.showerror("Error", "Contact not found!")
    else:
        messagebox.showerror("Error", "Please select a contact to delete!")


def populate_listbox():
    contacts_list.delete(0, tk.END)
    for name, contact in contacts.items():
        contacts_list.insert(tk.END, f"{name}: {contact}")

#FUNCTION FOR SEARCHING A CONTACT
def search_contact():
    name = name_entry.get()

    if name in contacts:
        contact = contacts[name]
        messagebox.showinfo("Contact", f"{name}: {contact}")
    else:
        messagebox.showerror("Error", "Contact not found!")

#FUNCTION FOR UPDATING CONTACT
def update_contact():
    selected_index = contacts_list.curselection()
    if selected_index:
        selected_contact = contacts_list.get(selected_index)
        old_name = selected_contact.split(":")[0].strip()
        old_contact = selected_contact.split(":")[1].strip()
        new_name = name_entry.get()
        new_contact = contact_entry.get()

        if old_name in contacts:
            del contacts[old_name]
            contacts[new_name] = new_contact
            messagebox.showinfo("Success", "Contact updated successfully!")
            populate_listbox()
            name_entry.delete(0, tk.END)
            contact_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Contact not found!")
    else:
        messagebox.showerror("Error", "Please select a contact to update!")

# SETTING UP GUI FOR CONTACT BOOK
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x350")
root.config(bg="#00246B")

heading_label = tk.Label(root, text="CONTACT BOOK", bg="#00246B", fg="#CADCFC", font=("Arial", 20, "bold"))
heading_label.pack(pady=3)

left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)
left_frame.config(bg="#00246B")


name_label = tk.Label(left_frame, text="NAME:",bg="#00246B",fg="#CADCFC",font=("Arial",12,"bold"))
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

name_entry = tk.Entry(left_frame,bg="#CADCFC",fg="#00246B",font=("Arial",8,"bold"))
name_entry.grid(row=0, column=1, padx=10, pady=10)

contact_label = tk.Label(left_frame, text="CONTACT:",bg="#00246B",fg="#CADCFC",font=("Arial",12,"bold"))
contact_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

contact_entry = tk.Entry(left_frame,bg="#CADCFC",fg="#00246B",font=("Arial",8,"bold"))
contact_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(left_frame, text="ADD", command=add_contact,bg="#CADCFC",fg="#00246B",font=("Arial",12,"bold"))
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

delete_button = tk.Button(left_frame, text="DELETE", command=delete_contact,bg="#CADCFC",fg="#00246B",font=("Arial",12,"bold"))
delete_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")

search_button = tk.Button(left_frame, text="SEARCH", command=search_contact,bg="#CADCFC",fg="#00246B",font=("Arial",12,"bold"))
search_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")

update_button = tk.Button(left_frame, text="UPDATE", command=update_contact,bg="#CADCFC",fg="#00246B",font=("Arial",12,"bold"))
update_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="we")

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
right_frame.config(bg="#00246B")

contacts_list = tk.Listbox(right_frame,bg="#CADCFC",fg="#00246B",font=("Arial",12,"bold"))
contacts_list.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=contacts_list.yview,bg="blue")
scrollbar.pack(side=tk.RIGHT, fill="y")

contacts_list.config(yscrollcommand=scrollbar.set)

populate_listbox()

root.mainloop()
