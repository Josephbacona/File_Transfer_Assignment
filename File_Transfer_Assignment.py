import shutil
import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import tkinter
from tkinter import *
from datetime import timedelta
import datetime



def chooseSource():
    myDir = fd.askdirectory()
    source_dir.delete(0,END)
    source_dir.insert(0, myDir)

def chooseDestination():
    myDir = fd.askdirectory()
    destination_dir.delete(0,END)
    destination_dir.insert(0, myDir)

def moveFiles():
    source = source_dir.get()
    destination = destination_dir.get()
    files = os.listdir(source)
    for i in files:
        filePath = os.path.join(source, i)

        twentyfour_hours_ago = datetime.datetime.now() - timedelta(hours = 24)
        mod_time = os.path.getmtime(filePath)
        datetime_of_file = datetime.datetime.fromtimestamp(mod_time)

        print(twentyfour_hours_ago)
        if twentyfour_hours_ago < datetime_of_file:
            #we are sating move the files repressented by 'i' to their new destination
            shutil.move(source + '/' + i, destination)
            print(i)

win = tkinter.Tk()

win.resizable(width=False, height=False)
win.geometry('{}x{}'.format(700, 400))
win.title('Learning Tkinter!')
win.config(bg='lightgray')

win.varFName = StringVar()
win.varLName = StringVar()

# Create a source Button
btnSource = Button(win,text='Select Source: ', font=("Helvetia", 16), fg='black', bg='lightgray', command=chooseSource)
btnSource.grid(row=0,column=0,padx=(30,0), pady=(30,0))

source_dir = Entry(win,text=win.varFName, font=("Helvetia", 16), fg='black', bg='lightblue')
source_dir.grid(row=0,column=1,padx=(30,0), pady=(30,0))

# Create a destination Button
btnDestination = Button(win,text='Select Destination: ', font=("Helvetia", 16), fg='black', bg='lightgray', command=chooseDestination)
btnDestination.grid(row=1,column=0,padx=(30,0), pady=(30,0))

destination_dir = Entry(win,text=win.varLName, font=("Helvetia", 16), fg='black', bg='lightblue')
destination_dir.grid(row=1,column=1,padx=(30,0), pady=(30,0))

lblDisplay = Label(win,text='', font=("Helvetia", 16), fg='black', bg='lightgray')
lblDisplay.grid(row=3,column=1,padx=(30,0), pady=(30,0))

btnSubmit = Button(win, text="Move Files", width=10, height=2, command=moveFiles)
btnSubmit.grid(row=2,column=1,padx=(30,0), pady=(30,0), sticky=NE)

win.mainloop() 