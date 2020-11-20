import tkinter as tk
import logic as lg
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image,  ImageTk
import results_gui as res

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = f"{THIS_FOLDER}/diablogo.jpg"

class MainApp(tk.Frame):
    def __init__(self, parent,  *args, **kwargs,):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
       
        

        

        ##Declaring buttons and text area for the char and stash selection + labels
        #Top Logo
        self.img = ImageTk.PhotoImage(Image.open(IMAGE_PATH))
        self.logo_panel = tk.Label(self, image = self.img)
        #Character file browse
        self.char_browse_button = tk.Button(self, text="Browse...", command=self.char_browse)       
        self.char_browse_text_area = tk.Entry(self, width=60, )
        self.char_browse_label = tk.Label(self, text="Import your Diablo 2 (.d2s) save file")
        ##Plugy Personal Stash Browse
        self.plugy_browse_button = tk.Button(self, text="Browse...", command=self.plugy_stash_browse, state=tk.DISABLED)
        self.plugy_browse_text_area = tk.Entry(self, width=60, state=tk.DISABLED )
        self.plugy_browse_label = tk.Label(self, text="Import your Plugy Personal Stash (.d2x) save file")        
        ##Plugy Shared Stash Browse
        self.stash_browse_button = tk.Button(self, text="Browse...", command=self.shared_stash_browse, state=tk.DISABLED)
        self.stash_browse_text_area = tk.Entry(self, width=60, state=tk.DISABLED )
        self.stash_browse_label = tk.Label(self, text="Import your Plugy Shared Stash (.sss) file", state=tk.DISABLED)
        
        ## Submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_files)
        # self.submit_button = tk.Button(self, text="Submit", command=self.open_results_window)
        
        
        
        ##Check button to add Plugy personal and shared stash
        self.shared_stash_checked = tk.IntVar()
        self.shared_stash_checkbutton = tk.Checkbutton(self, text="Add Plugy Shared Stash", variable=self.shared_stash_checked, onvalue=1, command=self.add_shared_stash, state=tk.DISABLED)

        self.plugy_stash_checked = tk.IntVar()
        self.plugy_stash_checkbutton = tk.Checkbutton(self, text="Add Plugy Personal Stash", variable=self.plugy_stash_checked, onvalue=1, command=self.add_plugy_stash)
        


        ## Rendering widgets ##
        #Row 0
        self.logo_panel.grid(row=0, column=0, padx=10, pady=(5,50), sticky=tk.N, columnspan=2)
        #Row 1
        self.char_browse_label.grid(row=1, column=0, padx=10, sticky=tk.S+tk.W)
        #Row 2
        self.char_browse_text_area.grid(row=2, column=0, padx=10, pady=5, sticky=tk.N+tk.W,)
        self.char_browse_button.grid(row=2, column=1, pady=5, sticky=tk.N+tk.E,)
        #Row 3
        self.plugy_stash_checkbutton.grid(row=3, column=0, padx=5, pady=15, sticky=tk.S+tk.W)
        #Row 4
        self.plugy_browse_label.grid(row=4, column=0, padx=10, sticky=tk.S+tk.W)
        #Row 5
        self.plugy_browse_text_area.grid(row=5, column=0, padx=10, pady=5, sticky=tk.N+tk.W,)
        self.plugy_browse_button.grid(row=5, column=1, pady=10, sticky=tk.S+tk.E)
        #Row 6
        self.shared_stash_checkbutton.grid(row=6, column=0, padx=5, pady=15, sticky=tk.S+tk.W)
        #Row 7
        self.stash_browse_label.grid(row=7, column=0, padx=10, sticky=tk.S+tk.W)
        #Row 8
        self.stash_browse_text_area.grid(row=8, column=0, padx=10, pady=5, sticky=tk.N+tk.W,)
        self.stash_browse_button.grid(row=8, column=1, pady=5, sticky=tk.N+tk.E,)
        #Row 9
        self.submit_button.grid(row=9, column=1, pady=10, sticky=tk.S+tk.E)
        






    def char_browse(self):
        ##deletes anything already entered
        self.char_browse_text_area.delete(0, tk.END)
        ##opens browse dialog window
        ###OPENS THIS FOLDER FOR TESTING PURPOSES, NEED TO CHANGE
        self.filename = filedialog.askopenfilename(initialdir=THIS_FOLDER, title="Select a file", filetypes=(("Diablo 2 Save Files", "*.d2s"),("All Files", "*.*")))
        self.char_browse_text_area.insert(0, self.filename)

    def plugy_stash_browse(self):
        ##deletes anything already entered
        self.plugy_browse_text_area.delete(0, tk.END)
        ##opens browse dialog window
        ###OPENS THIS FOLDER FOR TESTING PURPOSES, NEED TO CHANGE
        self.filename = filedialog.askopenfilename(initialdir=THIS_FOLDER, title="Select a file", filetypes=(("Plugy Personal Stash Files", "*.d2x"),("All Files", "*.*")))
        self.plugy_browse_text_area.insert(0, self.filename)




    def shared_stash_browse(self):
        ##deletes anything already entered
        self.stash_browse_text_area.delete(0, tk.END)
        ##opens browse dialog window
        ###OPENS THIS FOLDER FOR TESTING PURPOSES, NEED TO CHANGE
        self.filename = filedialog.askopenfilename(initialdir=THIS_FOLDER, title="Select a file", filetypes=(("Plugy Shared Stash Files", "*.sss"),("All Files", "*.*")))
        self.stash_browse_text_area.insert(0, self.filename)

    def submit_files(self): 
        ##gets paths for stash and char files
        char_path = self.char_browse_text_area.get()
        plugy_path = self.plugy_browse_text_area.get()
        shared_path = self.stash_browse_text_area.get()
        ##stk.ENDs paths to logic module to check if they are correct file types
        self.load_files_check(char_path, plugy_path, shared_path)

    

    def add_shared_stash(self):
        if self.shared_stash_checked.get() == 1:
            self.stash_browse_text_area.config(state=tk.NORMAL)
            self.stash_browse_button.config(state=tk.NORMAL)
            self.stash_browse_label.config(state=tk.NORMAL)
        else:
            self.stash_browse_text_area.config(state=tk.DISABLED)
            self.stash_browse_button.config(state=tk.DISABLED)
            self.stash_browse_label.config(state=tk.DISABLED)


    def add_plugy_stash(self):
        if self.plugy_stash_checked.get() == 1:
            self.plugy_browse_text_area.config(state=tk.NORMAL)
            self.plugy_browse_button.config(state=tk.NORMAL)
            self.plugy_browse_label.config(state=tk.NORMAL)
            self.shared_stash_checkbutton.config(state=tk.NORMAL)
        else:
            self.shared_stash_checkbutton.deselect()
            self.plugy_browse_text_area.config(state=tk.DISABLED)
            self.plugy_browse_button.config(state=tk.DISABLED)
            self.plugy_browse_label.config(state=tk.DISABLED)
            self.stash_browse_text_area.config(state=tk.DISABLED)
            self.stash_browse_button.config(state=tk.DISABLED)
            self.stash_browse_label.config(state=tk.DISABLED)
            self.shared_stash_checkbutton.config(state=tk.DISABLED)




    def check_file_extension(self, path, ext, display_name):
        if os.path.splitext(path)[1] != (ext) or len(os.path.splitext(path)[1]) == 0:
            messagebox.showerror("Notification", f"Please select a {ext} {display_name}.")
        else:
            return False


    def load_files_check(self, char_path, plugy_path, shared_path):
        validate_char_path = self.check_file_extension(char_path, ".d2s", "Diablo II save file")
        if self.plugy_stash_checked.get() == 0:
            if validate_char_path == False:
                query = lg.Query(is_plugy_added = False, 
                is_shared_added = False, char_path = char_path, plugy_path = plugy_path, shared_path = shared_path)
        elif self.shared_stash_checked.get() == 1:
            if self.check_file_extension(shared_path, ".sss", "Plugy shared stash file") == False:
                query = lg.Query(is_plugy_added = True, 
                is_shared_added = True, char_path = char_path, plugy_path = plugy_path, shared_path = shared_path)
        elif self.plugy_stash_checked.get() == 1:
            if self.check_file_extension(plugy_path, ".d2x", "Plugy personal stash file") == False:
                query = lg.Query(is_plugy_added = True, 
                is_shared_added = False, char_path = char_path, plugy_path = plugy_path, shared_path = shared_path)
        ##Handling Unboundlocalerror so I only need to write query.start() once
        try:             
            query.start()
        except UnboundLocalError:
            pass
        


    def open_results_window(self):
        try: 
            ## Checks if window is already opened, if it is not, raises an error but the error is handled, by opening it. 
            if self.results_window.state() == "normal":
                self.results_window.lift()
            
        except Exception:
            self.results_window = tk.Toplevel(self.parent)
            self.new_window = res.ResultsWindow(self.results_window)
            self.results_window.geometry("500x400")
            self.results_window.title("Results")


def main():
    root = tk.Tk()
    MainApp(root).grid(row=0, column=0, padx=20, pady=10)
    root.title("Diablo II RuneKeeper")
    root.geometry("700x600") # width x height
    root.mainloop()


if __name__ == "__main__":
    main()
    