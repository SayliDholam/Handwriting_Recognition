
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from tkinter import ttk

app = tk.Tk()
app.geometry("900x520")
app.title("Welcome Page")
app.resizable(False, False)


bg_image = Image.open("bgimg.png")  
bg_image = ImageTk.PhotoImage(bg_image)


bg_label = tk.Label(app, image=bg_image)
bg_label.place(relwidth=1, relheight=1)


def open_register_page():
    app.destroy() 
    subprocess.Popen(["python", "Register.py"])

def open_login_page():
    app.destroy()  
    subprocess.Popen(["python", "Login.py"])


button_font = ("Georgia", 15)  
button_width = 13
button_padx = 13
button_pady = 13

style = ttk.Style()
style.configure("TButton", padding=(button_padx, button_pady))
style.configure("TButton", borderwidth=6)
style.configure("TButton", relief="groove")
style.configure("TButton", font = button_font)


style.map("TButton",
          foreground=[('active', 'blue')],
          background=[('active', 'red')])


register_button = ttk.Button(app, text="Register", command=open_register_page, style="TButton",
                             width=button_width, padding=(button_padx, button_pady))
register_button.place(relx=0.5, rely=0.4, anchor="center")

login_button = ttk.Button(app, text="Sign In", command=open_login_page, style="TButton",
                          width=button_width, padding=(button_padx, button_pady))
login_button.place(relx=0.5, rely=0.6, anchor="center")


app.mainloop()

