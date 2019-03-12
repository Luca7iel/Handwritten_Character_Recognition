from tkinter import filedialog
from tkinter import *
import shutil,os
 
import tkinter as tk
win =tk.Tk()

win.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

print (win.filename)
files =(win.filename)
for f in files:
    shutil.copy(f,'C:\Users\Ezio\Desktop\HTR_project\1.Word Segmentation\data')



##win.title("Handwriting Recogniser")

##win.mainloop()
