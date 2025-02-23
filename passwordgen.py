import string
import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password():
    length = length_var.get()

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0!")
        return

    character_list = ""
    if digits_var.get():
        character_list += string.digits
    if letters_var.get():
        character_list += string.ascii_letters
    if special_var.get():
        character_list += string.punctuation

    if not character_list:
        messagebox.showerror("Error", "Please choose at least one character type!")
        return

    password = "".join(random.choice(character_list) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copying", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")


tk.Label(root, text="Password length:").pack()
length_var = tk.IntVar(value=12)
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()

digits_var = tk.BooleanVar()
letters_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Numbers (0-9)", variable=digits_var).pack()
tk.Checkbutton(root, text="Letters (a-z, A-Z)", variable=letters_var).pack()
tk.Checkbutton(root, text="Special characters (@, #, & etc.)", variable=special_var).pack()

password_entry = tk.Entry(root, font=("Arial", 14), justify="center")
password_entry.pack(pady=10)

tk.Button(root, text="Generate password", command=generate_password).pack()
tk.Button(root, text="Copy", command=copy_to_clipboard).pack()
root.mainloop()