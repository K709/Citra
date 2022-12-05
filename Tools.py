from tkinter import *
  
# import filedialog module
from tkinter import filedialog
import cv2 as cv
import os

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Pictures",
                                                        ".png"),
                                                       ("Pictures",
                                                        ".jpg"),
                                                        ("Pictures",
                                                        ".jpeg")))
    return filename
    
def picture():
    cam = cv.VideoCapture(0)

    cv.namedWindow("test")

    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv.imshow("test", frame)

        k = cv.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            cam.release()
            cv.destroyAllWindows()
        elif k%256 == 32:
            # SPACE pressed
            image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            cam.release()
            cv.destroyAllWindows()
            return image

def export(img, width, height):
    new_img = cv.resize(cv.cvtColor(img,cv.COLOR_RGB2BGR),dsize=[width,height])
    file_path = os.listdir(os.getcwd())
    file_name = [match for match in file_path if "Filter_Image" in match]
    img_name = "Filter_Image_"+str(len(file_name))+".jpg"
    cv.imwrite(img_name, new_img)