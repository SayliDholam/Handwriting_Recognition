
from customtkinter import *
import subprocess
from PIL import Image, ImageTk
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")  
db = client["Data_Base1"]  
collection = db["S1_RegisterLogin"]  

app = CTk()
app.geometry("500x480")
app.title("Registration Page")
app.configure(bg="black")
set_default_color_theme("blue")


def register_user():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    age_valid = age.isdigit()
    email_valid = "@" in email

    if not age_valid:
        age_entry.set("Invalid input")
    if not email_valid:
        email_entry.set("Invalid input")

    if age_valid and email_valid:

        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "email": email,
            "username": username,
            "password": password
        }
        collection.insert_one(user_data)

        print("Registration Info:")
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Age:", age)
        print("Email:", email)
        print("Username:", username)
        print("Password:", password)

        CTkLabel(master=app, text="Registration successful!").pack(pady=10, padx=20)


        app.destroy()
        subprocess.Popen(["python", "Welcome.py"])


CTkLabel(master=app, text="Registration Page").pack(pady=20)

first_name_entry = CTkEntry(master=app, placeholder_text="First Name")
first_name_entry.pack(pady=10, padx=20)

last_name_entry = CTkEntry(master=app, placeholder_text="Last Name")
last_name_entry.pack(pady=10, padx=20)

age_entry = CTkEntry(master=app, placeholder_text="Age")
age_entry.pack(pady=10, padx=20)

email_entry = CTkEntry(master=app, placeholder_text="Email")
email_entry.pack(pady=10, padx=20)

username_entry = CTkEntry(master=app, placeholder_text="Username")
username_entry.pack(pady=10, padx=20)

password_entry = CTkEntry(master=app, placeholder_text="Password", show="*")
password_entry.pack(pady=10, padx=20)

CTkButton(master=app, text="Register", command=register_user).pack(pady=20, padx=20)

app.mainloop()


