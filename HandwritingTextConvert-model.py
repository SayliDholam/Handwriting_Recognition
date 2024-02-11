
import pytesseract
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, filedialog
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")  
db = client["Data_Base1"]  
collection = db["S1_HandwritingSamples"]


pytesseract.pytesseract.tesseract_cmd = r"D:\Softwares Setup\Tesseract_Python\tesseract.exe"

def recognize_handwriting(image_path, text_display):
    try:

        image = Image.open(image_path)

        recognized_text = pytesseract.image_to_string(image)

        text_display.config(state=tk.NORMAL)
        text_display.delete(1.0, tk.END)  
        text_display.insert(tk.END, recognized_text)
        text_display.config(state=tk.DISABLED)


        insert_into_mongodb(image_path, recognized_text)
    except Exception as e:
        print("Error during handwriting recognition:", str(e))

def insert_into_mongodb(image_path, recognized_text):
    try:
     
        document = {"image_path": image_path, "recognized_text": recognized_text}
        collection.insert_one(document)
        print("Data inserted into MongoDB successfully.")
    except Exception as e:
        print("Error during MongoDB insertion:", str(e))

def browse_image():
    file_path = filedialog.askopenfilename(
        title="Select Image", 
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")],
        initialdir="/"
    )
    if file_path:
        image_path_entry.delete(0, tk.END)
        image_path_entry.insert(tk.END, file_path)
        load_and_display_image(file_path)

def load_and_display_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((400, 400))  
    imgtk = ImageTk.PhotoImage(image)
    image_label.config(image=imgtk)
    image_label.image = imgtk
    recognize_handwriting(image_path, text_display)


window = tk.Tk()
window.title("Handwriting Recognition")


style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#2196F3", foreground="#000")

frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

browse_button = ttk.Button(frame, text="Browse", command=browse_image, style="TButton")
image_path_entry = ttk.Entry(frame, width=40, style="TEntry")

image_label = ttk.Label(window)
text_label = tk.Label(window, text="Detected Text:")
text_display = tk.Text(window, height=10, width=50, state=tk.DISABLED, wrap=tk.WORD)

browse_button.grid(row=0, column=0, padx=(0, 10), pady=10, sticky=tk.W)
image_path_entry.grid(row=0, column=1, padx=(0, 10), pady=10, sticky=(tk.W, tk.E))

image_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
text_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
text_display.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

window.mainloop()



