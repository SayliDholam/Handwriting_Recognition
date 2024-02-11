
from customtkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import subprocess
from pymongo import MongoClient, errors


client = MongoClient("mongodb://localhost:27017/")  
db = client["Data_Base1"]  
collection = db["S1_RegisterLogin"]  

app = CTk()
app.geometry("500x480")
app.title("Login Page")
app.configure(bg="black")
set_default_color_theme("blue")


def create_success_button():
    success_button = CTkButton(master=app, text="Login Successful", 
        command=lambda: subprocess.Popen(["python", "HandwritingTextConvert-model.py"]))
    success_button.pack(pady=20, padx=20)


def login_user():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    try:
        user_data = collection.find_one({"username": entered_username, "password": entered_password})

        if user_data:
            print("Login Successful")
            create_success_button()
            app.destroy()
            subprocess.Popen(["python", "HandwritingTextConvert-model.py"])
        else:
            print("Login Failed")
            login_fail_label = CTkLabel(master=app, text="Login Failed" )
            login_fail_label.pack(pady=10, padx=20)

    except errors.PyMongoError as e:
        print(f"MongoDB Error: {e}")


CTkLabel(master=app, text="Login Page").pack(pady=20)

username_entry = CTkEntry(master=app, placeholder_text="Username")
username_entry.pack(pady=10, padx=20)

password_entry = CTkEntry(master=app, placeholder_text="Password", show="*")
password_entry.pack(pady=10, padx=20)

CTkButton(master=app, text="Login", command=login_user).pack(pady=20, padx=20)

app.mainloop()
