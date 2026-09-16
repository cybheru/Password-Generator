from os import link
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from generator import generate_password
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x350")
root.resizable(False, False)
bg_color = "#3742D8"

title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 22, "bold"),
    bg=bg_color,
    fg="white"
)
title.pack(pady=25)

length_label = tk.Label(
    root,
    text="Enter Password Length",
    background="#18A5AA",
    font=("Arial", 12)
   
   
)
length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
length_entry.pack(pady=10)

def generate():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning("Invalid Length", "Password Length minimum 8 honi chahiye.")
            return

        password = generate_password(length)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)


    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

generate_button = tk.Button(
    root,
    text="🔐Generate Password",
    background="#109674",
    font=("Arial", 12, "bold"),
    command=generate

)
generate_button.pack(pady=10)

password_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=32,
    justify="center"
)
password_entry.pack(pady=10)

def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "✅ Password copied successfully")
        
    else:
        messagebox.showwarning("Warning", "Please generate a password first")

copy_button = tk.Button(
    root,
    text="Copy Password",
    background="#0E4E5E",
    font=("Arial", 11),
    command=copy_password
)
copy_button.pack(pady=5)

def clear_password():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

clear_button = tk.Button(
    root,
    text="Clear",
    background="#BE1469",
    font=("Arial", 11),
    command=clear_password
)
clear_button.pack(pady=5)

root.mainloop()