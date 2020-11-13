import tkinter as tk

class ResultsWindow(tk.Frame):
    def __init__(self, parent,  *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        ##Declaring widgets
        self.title_label = tk.Label(self.parent, text="Results Page")
        self.test_button = tk.Button(self.parent, text="test")






        ##Rendering widgets
        #Row 0
        self.title_label.grid(row=0, column=0, padx=10, pady=(5,50), sticky=tk.N, columnspan=2)


        self.test_button.grid(row=2, column=2)