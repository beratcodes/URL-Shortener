# ----------------------------------------
# Project : URL-Shortener
# Author  : beratcodes
# Date    : 2025-12-30
# ----------------------------------------
import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip

# FUNC
def shorten_url():
    long_url = long_entry.get()
    response = requests.get(f'http://tinyurl.com/api-create.php?url={long_url}')
    short_url = response.text
    result_label.config(text=f'Shorten Link: {short_url}')
    copy_button.config(state=tk.NORMAL)

def copy_to_clipboard():
    short_url = result_label.cget("text")[13:]
    pyperclip.copy(short_url)
    messagebox.showinfo("Copied","Short URL is copied.")

# GUI
# .ico file
photo = tk.PhotoImage(file= "url.ico")

app_window = tk.Tk()
app_window.title("URL Shortener")
app_window.resizable(0,0)
app_window.iconphoto(True, photo)

# Entry, Label, Buttons
long_label = tk.Label(app_window, text="Insert Long Link:")
long_entry = tk.Entry(app_window, width=40)
result_label = tk.Label(app_window, text="")
shorten_button = tk.Button(app_window, text="Shorten", command=shorten_url)
copy_button = tk.Button(app_window, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)

# Grid System
long_label.grid(row=0, column=0, padx=10, pady=10)
long_entry.grid(row=0, column=1, padx=10, pady=10)
shorten_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
app_window.mainloop()