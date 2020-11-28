import tkinter as tk
import logic as lg

class ResultsWindow(tk.Frame):
    def __init__(self, parent,  *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        ##Declaring widgets
        self.scrollbar = tk.Scrollbar(self.parent)
        self.text_window = tk.Text(self.parent, height=50, width=50,state='disabled')
        self.test_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."






        ##Rendering widgets
        #Row 0
        self.text_window.pack(side=tk.LEFT, fill=tk.Y)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.text_window.yview)
        self.text_window.config(yscrollcommand=self.scrollbar.set)
        self.toggle_read_only()
        self.text_window.insert(tk.END, self.test_text)
        self.toggle_read_only()


    def toggle_read_only(self):
        if self.text_window.cget('state') == 'disabled':
            self.text_window.config(state='normal')
        elif self.text_window.cget('state') == 'normal':
            self.text_window.config(state='disabled')


        