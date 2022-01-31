from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename
from quitter import Quitter
import  subprocess
import os

filena=""


def append_to_terminal_text(text) :
    # can append a single character or more to the terminal
    global terminal_text
    
    terminal_listbox.delete(END)
    terminal_text = terminal_text + text
    terminal_listbox.insert(END, terminal_text)
    terminal_listbox.yview_moveto(1)
    return

def sf(comm='cal'):
    last_line_index=terminal_listbox.size()
    terminal_listbox.insert(END,'Coping homeworks')
    path =os.getcwd()+'/'
    #os.environ["PYTHONUNBUFFERED"] = "1"
    
    os.chdir('/home/ubuntu/repo/repo/projects/python/testcpp/')
    #comm = 'ls -al'
    #print(com.split())
    result = subprocess.run(comm.split(), stdout=subprocess.PIPE)#, stderr=subprocess.STDOUT, shell = True, env = os.environ)
    
    #result = subprocess.run(command_summary, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell = True, env = os.environ)
    
    output = result.stdout
    # To make sure we print output line by line and not in one single line we use splitlines.
    output_lines = output.splitlines()
    
    for k in output_lines :
        terminal_listbox.insert(last_line_index, k)
        last_line_index += 1 # Increases line index to make sure output is printed line by line.
    
    return


def check_preparation():
    pass  
    
    #a=askopenfilename()
    #ent.insert(0, a)
    os.chdir(path)

#def of(fil):
#    print(fil)
#    t=input()
#    comm = f"vim {fil}"
#    list_files = subprocess.run(comm.split())
#"gnome-terminal 'sudo apt-get update'"
com = "python3 /home/ubuntu/repo/repo/projects/python/testcpp/git_log_all.py -gp"
root = Tk()
#push = Button(root, text='Set Background Color', command=setbgcolor)
#func=(lambda : openfile())
 
push = Button(root, text='Получить домашние работы', command=(lambda: sf(com)))
push.config(height=3, font=('times', 20, 'bold'))
push.pack(expand=YES, fill=BOTH)

com1 = "python3 /home/ubuntu/repo/repo/projects/python/testcpp/copy_to_tests.py"
push1 = Button(root, text='Подготовить к проверке', command=(lambda: sf(com1)))
push1.config(height=3, font=('times', 20, 'bold'))
push1.pack(expand=YES, fill=BOTH)



#ent = Entry(root)

#row.pack(side=TOP, fill=X)
#lab.pack(side=LEFT)

#ent.pack(side=TOP, expand=YES, fill=X)
#func =(lambda : of(filena))
#push1 = Button(root, text='OpenFile', command=lambda : of(ent.get()))
#push1.config(height=3, font=('times', 20, 'bold'))
#push1.pack(expand=YES, fill=BOTH)

root.title('Command Prompt In Tkinter')
root.geometry('677x343')

# Making a frame, this terminal frame can be packed or used as a toplevel window instead.
terminal = Frame(root, bg = 'black')

# Initializing a listbox to act as terminal with bg and fg of your own choice.
# NOTE:  in the listbox to make it so the selection of listbox items is not visible
# I have changed the highlight color and select color to background color and also have set
# the active style i.e. the style used to display a selection to tk.NONE, and have also set
# the highlight thickness to 0.
terminal_listbox = Listbox(terminal, bg = 'black', fg = 'white', highlightcolor = 'black', highlightthickness = 0, selectbackground = 'black', activestyle = NONE)
terminal_scrollbar = Scrollbar(terminal)
terminal_scrollbar.pack(side = RIGHT, fill = Y)

# packing and stuff.
terminal_listbox.pack(expand = True, fill = BOTH)
terminal.pack(expand = True, fill = BOTH)

# Inserting the copyright thingy.
terminal_listbox.insert(END, 'Tkinter Terminal')
terminal_listbox.insert(END, '© Copyright blah blah')
terminal_listbox.insert(END, 'By Matrix Programmer!')

# Intializes the terminal text for the first line.
terminal_text = '>> '

# Assigns a scrollbar to the terminal.
terminal_listbox.config(yscrollcommand = terminal_scrollbar.set)
terminal_scrollbar.config(command = terminal_listbox.yview)

# THE FIRST EVER INSERTED ITEM DOES NOT APPEAR SO THIS IS A BUFFER ITEM TO FILL THAT SPOT
terminal_listbox.insert(END, '')
terminal_listbox.insert(END, '')

append_to_terminal_text('') # Buffer.

Quitter(root).pack(side=TOP, fill=BOTH)
root.mainloop()

