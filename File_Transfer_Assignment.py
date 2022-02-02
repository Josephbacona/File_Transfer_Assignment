import shutil
import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import tkinter
from tkinter import *

win = Tk()

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')

        self.varFName = StringVar()
        self.varLName = StringVar()

        self.lblSource = Label(self.master,text='Select Source: ', font=("Helvetia", 16), fg='black', bg='lightgray' )
        self.lblSource.grid(row=0,column=0,padx=(30,0), pady=(30,0))

        self.lblSource = Label(self.master,text='Select Source: ', font=("Helvetia", 16), fg='black', bg='lightgray' )
        self.lblSource.grid(row=0,column=0,padx=(30,0), pady=(30,0))

        # Create a source Button
        tk.button_source.grid(row=1,column=0,padx=(30,0), pady=(30,0))(win, text="Browse", command=open_file)

        self.lblDestination = Label(self.master,text='Select Destination: ', font=("Helvetia", 16), fg='black', bg='lightgray' )
        self.lblDestination.grid(row=2,column=0,padx=(30,0), pady=(30,0))

        # Create a destination Button
        tk.Button.grid(row=3,column=0,padx=(30,0), pady=(30,0))(win, text="Browse", command=open_file)

        self.lblDisplay = Label(self.master,text='', font=("Helvetia", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3,column=1,padx=(30,0), pady=(30,0))

        self.txtSource = Entry(self.master,text=self.varFName, font=("Helvetia", 16), fg='black', bg='lightblue')
        self.txtSource.grid(row=0,column=1,padx=(30,0), pady=(30,0))
        
        self.txtDestination = Entry(self.master,text=self.varLName, font=("Helvetia", 16), fg='black', bg='lightblue')
        self.txtDestination.grid(row=1,column=1,padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Move Files", width=10, height=2)
        self.btnSubmit.grid(row=2,column=1,padx=(30,0), pady=(30,0), sticky=NE)
        #self.btnSubmit.pack(fill = BOTH, expand = True)

     


def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
   if file:
      content = file.read()
      file.close()
      print("%d characters in this file" % len(content))

win.mainloop()



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

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
'''
for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

#This source is for files that were added or modified in the last 24 hours
source2 = 'newFiles/'

#The destination is a folder that the home office can access
destination2 = 'newFilesCopied/'
newfiles = os.listdir(source2)



for i in newfiles:
    #we are saying move the newly created or modified files repressented
    #by 'i' to their destination
    shutil.move(source2+i, destination2)
'''

