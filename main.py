from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import ttk

class Pdf_Conversor(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        self.file_path = ""
        self.options = ["PDF"]

        self.sel_frame = LabelFrame(root, text="Conversor PDF", height=100, width=100)
        self.sel_frame.grid(column=0, row=0, padx=10, pady=10)

        self.file_label = Label(self.sel_frame, text="Arquivo: ")
        self.file_label.grid(column=0, row=0, padx=10)
        self.file_entry = Entry(self.sel_frame, width=25)
        self.file_entry.grid(column=1, row=0, padx=10)
        self.browse_bt = Button(self.sel_frame, text="Procurar")
        self.browse_bt.grid(column=2, row=0, padx=10)

        self.file_label = Label(self.sel_frame, text="Formato: ")
        self.file_label.grid(column=0, row=1, padx=10)
        self.menu = ttk.Combobox(self.sel_frame, width=22, values=self.options)
        self.menu.grid(column=1, row=1, padx=10)
        self.convert_bt = Button(self.sel_frame, text="Converter")
        self.convert_bt.grid(column=2, row=1, padx=10)

if __name__ == "__main__":
    root = Tk()
    root.title("Conversor PDF")
    Pdf_Conversor(root)
    root.mainloop()