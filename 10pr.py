import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook, Style
from tkinter import messagebox as mb
from tkinter import  filedialog as fd


def culc_result():
    if clicked.get() == '+':
        r = int(first_num.get()) + int(second_num.get())
        result_lable.configure(text=f'{r}')
    elif clicked.get() == '-':
        r = int(first_num.get()) - int(second_num.get())
        result_lable.configure(text=f'{r}')
    elif clicked.get() == '*':
        r = int(first_num.get()) * int(second_num.get())
        result_lable.configure(text=f'{r}')
    elif clicked.get() == '/':
        if int(second_num.get()) == 0:
            result_lable.configure(text='cant divide by zero')
        else:
            r = int(first_num.get()) / int(second_num.get())
            result_lable.configure(text=f'{r}')

def choose_def():
    result ="choosed: "
    if first.get() == 1: result = f"{result} first"
    if second.get() == 1: result = f"{result} second"
    if third.get() == 1: result = f"{result} third"
    mb.showinfo('info', f'{result}')

def extract_text():
    name = fd.askopenfilename()
    with open(f'{name}') as f:
        txt_field.insert(1.0,f.read())

root = Tk()  # обьект главного окна называется root так принято
root.title("Isaev Alexandr Alexandrovich")


#---------tab's--------------------------------------------
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Calculator")
tab_control.add(tab2, text="Check boxes")
tab_control.add(tab3, text="Text")

# --------calculating tab-----------------------------------
first_num = Entry(tab1)
first_num.grid(column=0, row=0)
second_num = Entry(tab1)
second_num.grid(column=2, row=0)
clicked = StringVar()
clicked.set('+')
dropdown_menu = OptionMenu(tab1, clicked, "+", "-", "/", "*").grid(column=1, row=0)
equals_lable = Label(tab1, text='=')
equals_lable.grid(column=3, row=0)
result_lable = Label(tab1, text=' ')
result_lable.grid(column=4, row=0)
calculate_buttom = Button(tab1, text='calculate the result', command=culc_result).grid(column=0, rowspan=3)

# --------check boxes tab-----------------------------------
first = IntVar()
second = IntVar()
third = IntVar()
first_check = Checkbutton(tab2, variable=first, text='first')
second_check = Checkbutton(tab2, variable=second, text='second')
third_check = Checkbutton(tab2, variable=third, text='third')
first_check.grid(column=0, row=0)
second_check.grid(column=1, row=0)
third_check.grid(column=2, row=0)

check_button = Button(tab2,text='what u choose', command=choose_def).grid(column=0, row=1)

#---------text tab -----------------------------------------
txt_field = Text(tab3)
upload_button = Button(tab3,text="upload text",command=extract_text)
upload_button.grid(column=0, row=0)
txt_field.grid(column=0, row=1,padx= 10, pady=10, sticky='NSEW')


tab_control.pack(padx=10, pady=10,expand=1,fill=tkinter.BOTH)
root.mainloop()
input()
