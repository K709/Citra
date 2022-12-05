from tkinter import *
from PIL import ImageTk, Image
import Tools
import Filter
import numpy as np

ori_img = None
filter_img = None
#Create The Method to Call Method in Another Class

def createFrame():
    global root, ori_img, filter_img

    root = Tk()
    root.title("Image Filter Buset")  # title of the GUI window
    root.maxsize(1000, 600)  # specify the max size the window can expand to
    root.config(bg="skyblue")  # specify background color

    # Create left and right frames
    left_frame = Frame(root, width=200, height=400, bg='grey')
    left_frame.grid(row=0, column=0, padx=10, pady=5)

    right_frame = Frame(root, width=650, height=400, bg='grey')
    right_frame.grid(row=0, column=1, padx=10, pady=5)
    
    img = filter_img
    if(img != None):
        # Create frames and labels in left_frame
        Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

        
        # load image to be "edited"
        width, height = img.size

        while(width>650 or height>400):
            img = img.resize((int(width/2),int(height/2)))
            width, height = img.size

        image = ImageTk.PhotoImage(img)
        original_image = ImageTk.PhotoImage(ori_img.resize((int(width/2),int(height/2))))  # resize image using subsample
        Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)

        # Display image in right_frame
        Label(right_frame, image=image).grid(row=0,column=0, padx=5, pady=5)

    # Create tool bar frame
    tool_bar = Frame(left_frame, width=180, height=185)
    tool_bar.grid(row=2, column=0, padx=5, pady=5)

    # Example labels that serve as placeholders for other widgets
    Label(tool_bar, text="Tools", width=15).grid(row=0, column=0, padx=5, pady=3)  # ipadx is padding inside the Label widget
    Label(tool_bar, text="Filters", width=15).grid(row=0, column=1, padx=5, pady=3)

    # Example labels that could be displayed under the "Tool" menu
    Button(tool_bar, text="Select An Image", command=select, width=15).grid(row=1, column=0, padx=5, pady=5)
    Button(tool_bar, text="Take A Picture", command=picture, width=15).grid(row=2, column=0, padx=5, pady=5)

    if(img != None):
        Button(tool_bar, text="Export", command=export, width=15).grid(row=3, column=0, padx=5, pady=5)

        # Example labels that could be displayed under the "Filter" menu
        Button(tool_bar, text="Pencil Sketch", command=pencil, width=15).grid(row=1, column=1, padx=5, pady=5)
        Button(tool_bar, text="Cartoonize", command=cartoonize, width=15).grid(row=2, column=1, padx=5, pady=5)
        Button(tool_bar, text="Sephia", command=sephia, width=15).grid(row=3, column=1, padx=5, pady=5)
        Button(tool_bar, text="Anaglyph", command=anaglyph, width=15).grid(row=4, column=1, padx=5, pady=5)

    else:
        b1 = Button(tool_bar, text="Export", command="", width=15)
        b1['state'] = DISABLED
        b1.grid(row=3, column=0, padx=5, pady=5)
        
        # Example labels that could be displayed under the "Filter" menu
        b2 = Button(tool_bar, text="Pencil Sketch", command="", width=15)
        b2['state'] = DISABLED
        b2.grid(row=1, column=1, padx=5, pady=5)

        b3 = Button(tool_bar, text="Cartoonize", command="", width=15)
        b3['state'] = DISABLED
        b3.grid(row=2, column=1, padx=5, pady=5)

        b4 = Button(tool_bar, text="Sephia", command="", width=15)
        b4['state'] = DISABLED
        b4.grid(row=3, column=1, padx=5, pady=5)

        b5 = Button(tool_bar, text="Anaglyph", command="", width=15)
        b5['state'] = DISABLED
        b5.grid(row=4, column=1, padx=5, pady=5)

    root.mainloop()

def select():
    global ori_img, root, filter_img
    img_path = Tools.browseFiles()
    ori_img = Image.open(img_path)
    filter_img = ori_img
    root.destroy()
    createFrame()

def picture():
    global ori_img, root, filter_img
    ori_img = Image.fromarray(Tools.picture())
    filter_img = ori_img
    root.destroy()
    createFrame()

def export():
    global filter_img,ori_img
    img = np.array(ori_img)
    width, height = ori_img.size
    new_img = np.array(filter_img)
    Tools.export(new_img, width, height)

def pencil():
    global filter_img, root, ori_img
    img = np.array(ori_img)
    filter_img = Image.fromarray(Filter.pencil(img))
    root.destroy()
    createFrame()

def cartoonize():
    global filter_img, root, ori_img
    img = np.array(ori_img)
    filter_img = Image.fromarray(Filter.cartoonize(img))
    root.destroy()
    createFrame()

def sephia():
    global filter_img, root, ori_img
    img = np.array(ori_img)
    filter_img = Image.fromarray(Filter.sephia(img))
    root.destroy()
    createFrame()

def anaglyph():
    global filter_img, root, ori_img
    img = np.array(ori_img)
    filter_img = Image.fromarray(Filter.anaglyph(img))
    root.destroy()
    createFrame()
    
createFrame()