from tkinter import *
  
# import filedialog module
from tkinter import filedialog
import cv2 as cv

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Pictures",
                                                        ".png"),
                                                       ("Pictures",
                                                        ".jpg")))
    return filename
    