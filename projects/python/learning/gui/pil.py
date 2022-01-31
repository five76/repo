from tkinter import *
win=Tk()
#import PIL
#from PIL import Image
#from PIL import ImageTk
from PIL.ImageTk import PhotoImage
#imgobj=Image.open("/home/ubuntu/DSC_7854.JPG")
photoimg=PhotoImage(file="/home/ubuntu/DSC_7854.JPG")
Button(win,image=photoimg).pack()
win.mainloop()
