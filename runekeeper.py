import tkinter as tk
import logic as lg
from tkinter import filedialog
from tkinter import messagebox
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ##Root, title and window size
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        







if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root).pack(side="top", fill="both", expand=True)
    root.title("Diablo II RuneKeeper")
    root.geometry("600x400")
    root.mainloop()