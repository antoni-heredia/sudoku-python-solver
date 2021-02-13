# use 'tkinter' instead of 'Tkinter' if using python 3.x
import tkinter as tk 

class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.button = tk.Button(self, text="Change text", command=self.on_change_text)
        self.canvas = tk.Canvas(self, width=400, height=400)

        self.button.pack(side="top", anchor="w")
        self.canvas.pack(side="top", fill="both", expand=True)

        # every canvas object gets a unique id, which can be used later
        # to change the object. 
        self.text_id = self.canvas.create_text(10,10, anchor="nw", text="Hello, world")

    def on_change_text(self):
        self.canvas.itemconfig(self.text_id, text="Goodbye, world")

if __name__ == "__main__":
    root = tk.Tk()
    view = Example(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()