from tkinter import filedialog
from tkinter import *
import shutil
import os
import sys

def callback():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    files =(root.filename)
    shutil.copy(files, dst, follow_symlinks=True)
    
    print (files)

def callback2():
    #os.system(r"C:\Users\Ezio\Desktop\HTR_project\Segment\src\main.py")
   # execfile(r"C:\Users\Ezio\Desktop\HTR_project\Segment\src\main.py")
   exec(open("C:/Users/Ezio/Desktop/HTR_project/Segment/src/main.py").read())
    

 
root = Tk()
root.geometry("500x500")
dst= (r"C:\Users\Ezio\Desktop\HTR_project\Segment\data")
root.title("Handwriting Recogniser")
b = Button(root, text="Upload Image", command=callback)
b.pack()


c = Button(root, text="Segment Image", command=callback2)
c.pack()



mainloop()
