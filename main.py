from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog as fd

class Demo(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        tabControl = ttk.Notebook(root)
        tabControl.configure(width=400, height=300)

        self.option = StringVar()
        self.options = ["Option Menu", "Combo Box"]
        self.option.set(0)

        self.first_tab = ttk.Frame(tabControl)
        tabControl.add(self.first_tab, text="Tab 1")
        tabControl.grid()

        self.second_tab = ttk.Frame(tabControl)
        tabColtrol.add(self.second_tab, text="Tab 2")
        tabControl.grid()

        self.widgets()

    def widgets(self):
        label_frame = LabelFrame(self.first_tab, text="Label Frame", width=300, height=300)
        label_frame.grid(column=0, row=0)
        label_frame.grid_propagate(0)

        entry = Entry(label_frame, width=45)
        entry.grid(column=0, row=1, columnspan=3)
        entry.insert(0, "Entry Field")

        radiobutton_1 = Radiobutton(label_frame,text="Radio 1", value=0)
        radiobutton_1.grid(column=0, row=2)
        radiobutton_2 = Radiobutton(label_frame, text="Radio 2", value=1)
        radiobutton_2.grid(column=1,row=2)

        Checkbutton = Checkbutton(label_frame, text = "Check")
        Checkbutton.grid(column=0, row=3)
