import tkinter as tk

def on_closing():
    pass  # No hace nada si intentan cerrar la ventana

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)