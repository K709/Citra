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
    image = cv.imread(filename)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return image
    