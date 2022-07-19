from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os

#instalizing tk
root=Tk()
root.geometry("630x700+400+100")
root.title("PDF viewer")
root.configure(bg="white")

Button(root, text="ouvrir", command=browseFiles, width=40, 
       font="arial 20", bd=4).pack()

root.mainloop()