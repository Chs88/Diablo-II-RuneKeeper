import tkinter as tk
import logic as lg

class ResultsWindow(tk.Frame):
    def __init__(self, parent,  *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        ##Declaring widgets
        self.title_label = tk.Label(self.parent, text="Results Page")
        






        ##Rendering widgets
        #Row 0
        self.title_label.grid(row=0, column=0, padx=100, pady=10, sticky=tk.N+tk.W+tk.E+tk.S, columnspan=2, )


        