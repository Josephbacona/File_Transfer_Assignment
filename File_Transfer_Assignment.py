import shutil
import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import tkinter
from tkinter import *

def open_file():
   file = fd.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
   if file:
      content = file.read()
      file.close()
      print("%d characters in this file" % len(content))

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected File',
        message=filename
    )

def new_Files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='new_Files',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='New Files',
        message=filename
    )

win = tkinter.Tk()

win.resizable(width=False, height=False)
win.geometry('{}x{}'.format(700, 400))
win.title('Learning Tkinter!')
win.config(bg='lightgray')

win.varFName = StringVar()
win.varLName = StringVar()

# Create a source Button
btnSource = Button(win,text='Select Source: ', font=("Helvetia", 16), fg='black', bg='lightgray', command=open_file )
btnSource.grid(row=0,column=0,padx=(30,0), pady=(30,0))

txtSource = Entry(win,text=win.varFName, font=("Helvetia", 16), fg='black', bg='lightblue')
txtSource.grid(row=0,column=1,padx=(30,0), pady=(30,0))

# Create a destination Button
btnDestination = Button(win,text='Select Destination: ', font=("Helvetia", 16), fg='black', bg='lightgray', command=select_file )
btnDestination.grid(row=1,column=0,padx=(30,0), pady=(30,0))

txtDestination = Entry(win,text=win.varLName, font=("Helvetia", 16), fg='black', bg='lightblue')
txtDestination.grid(row=1,column=1,padx=(30,0), pady=(30,0))

lblDisplay = Label(win,text='', font=("Helvetia", 16), fg='black', bg='lightgray')
lblDisplay.grid(row=3,column=1,padx=(30,0), pady=(30,0))

btnSubmit = Button(win, text="Move Files", width=10, height=2)
btnSubmit.grid(row=2,column=1,padx=(30,0), pady=(30,0), sticky=NE)

win.mainloop() 