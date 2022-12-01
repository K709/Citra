from tkinter import *
from PIL import ImageTk, Image
import Tools

img = None
#Create The Method to Call Method in Another Class
def select():
    img_path = Tools.browseFiles()
    img = Image.open(img_path)
    
    
def picture():
    picture = ""

def export():
    export = ""


# Create The GUI
root = Tk()  # create root window
root.title("Image Filter Buset")  # title of the GUI window
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color

# Create left and right frames
left_frame = Frame(root, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

if(img != None):
    # Create frames and labels in left_frame
    Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

    # load image to be "edited"
    width, height = img.size

    while(width>650 or height>400):
        img = img.resize((int(width/2),int(height/2)))
        width, height = img.size
        print(width, height)

    image = ImageTk.PhotoImage(img)
    original_image = ImageTk.PhotoImage(img.resize((int(width/2),int(height/2))))  # resize image using subsample
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
    Button(tool_bar, text="Pencil Sketch", command="", width=15).grid(row=1, column=1, padx=5, pady=5)
    Button(tool_bar, text="Cartoonize", command="", width=15).grid(row=2, column=1, padx=5, pady=5)
    Button(tool_bar, text="Sephia", command="", width=15).grid(row=3, column=1, padx=5, pady=5)
    Button(tool_bar, text="Anaglyph", command="", width=15).grid(row=4, column=1, padx=5, pady=5)

else:
    b1 = Button(tool_bar, text="Export", command=export, width=15)
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
