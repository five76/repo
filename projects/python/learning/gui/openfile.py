
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename
from quitter import Quitter
import  subprocess

filena=""

def sf():
        a=askopenfilename()
        ent.insert(0, a)
    

def of(fil):
    print(fil)
    t=input()
    comm = f"vim {fil}"
    list_files = subprocess.run(comm.split())


root = Tk()
#push = Button(root, text='Set Background Color', command=setbgcolor)
#func=(lambda : openfile())
push = Button(root, text='OpenFile', command=sf)
push.config(height=3, font=('times', 20, 'bold'))
push.pack(expand=YES, fill=BOTH)
ent = Entry(root)

#row.pack(side=TOP, fill=X)
#lab.pack(side=LEFT)
ent.pack(side=TOP, expand=YES, fill=X)
#func =(lambda : of(filena))
push1 = Button(root, text='OpenFile', command=lambda : of(ent.get()))
push1.config(height=3, font=('times', 20, 'bold'))
push1.pack(expand=YES, fill=BOTH)
Quitter(root).pack(side=TOP, fill=BOTH)
root.mainloop()