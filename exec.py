from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import shutil
from PIL import Image
import os
import WordSegmentation
import cv2
from WordSegmentation import wordSegmentation

##DEF FUNCTIONS

def callback():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    files =(root.filename)
    shutil.copy(files, dst, follow_symlinks=True)
    panel.pack(side="top", fill="none", expand="false")

def clicked():
    panel2.pack(side="top", fill="none", expand="false")



 
root = Tk()
root.geometry("800x600")
dst= (r"C:\Users\Ezio\Desktop\HTR_project\Segment\data")
root.title("Handwriting Recogniser")

##First Button
b = Button(root, text="Upload Image", command=callback)
b.pack()

## Second Button
c = Button(root, text="Segment", command=clicked)
c.pack()

##path for first button image
img = ImageTk.PhotoImage(Image.open("C:/Users/Ezio/Desktop/HTR_project/a.jpg"))
panel = Label(root, image=img)

##path for second button image
img2 = ImageTk.PhotoImage(Image.open("C:/Users/Ezio/Desktop/HTR_project/Segment/out/text_line.png/summary.png"))
panel2 = Label(root, image=img2)


root.mainloop()







