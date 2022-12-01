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
    
def picture():
    cam = cv.VideoCapture(0)

    cv.namedWindow("test")

    img_counter = 0
    capture = True
    while capture:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv.imshow("test", frame)

        k = cv.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            capture = False
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1