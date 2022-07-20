from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os

# instalizing tk
root = Tk()
root.geometry("630x700+400+100")
root.title("PDF viewer")
root.configure(bg="white")

# main part of program


def browseFiles():
    filename = filedialog.askopenfilename(intialdir=os.getcwd(),
                                          title="Selectionne un fichier pdf",
                                          filetype=(("PDF File", ".pdf"),
                                                    ("PDF File", ".PDF"),
                                                    ("All file", ".txt")))
v1=pdf.ShowPdf()
v2=v1.pdf_view(root,pdf_location=open(filename,"r"),width=77,height=100)


Button(root, text="ouvrir", command=browseFiles, width=40,
       font="arial 20", bd=4).pack()

root.mainloop()
