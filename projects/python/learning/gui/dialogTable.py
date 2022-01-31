# определяет таблицу имя:обработчик с демонстрационными примерами
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat
from pprint import pprint
demos = {
    'Open': askopenfilename,
    'Color': askcolor,
    'Query': lambda:askquestion('Warning','you typed "rm *"\nConfirm?'),
    'Error': lambda: showerror('Error!', "He’s dead, Jim"),
    'Input': lambda: askfloat('Entry', 'Enter credit card number')
}

if __name__ == '__main__':
    pprint(demos)
