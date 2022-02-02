from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('File Browser')
root.iconbitmap("apple.ico")
root.geometry("500x500")

def files():
    root.filename = filedialog.askopenfilename(initialdir='C:\Users\joeyb\OneDrive\Documents\GitHub\File_Transfer_Assignment',title="Select File",filetypes(("txt files","*.txt"),("all files","*.*")))

b1 = Button(root, text="FILE OPEN", command = files)
b1.pack()
my_label = Label(root, text= "ALL DONE!")
my_label.pack()

root.mainloop()
