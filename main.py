from tkinter import *
from tkinter.ttk import *
from time import  strftime

root = Tk()
root.title('JAM DIGITAL')

def waktu():
    format = strftime('%H:%M:%S %p')
    label.config(text=format)
    label.after(1000,waktu)

label = Label(root, font=('ds-digital', 80), background='black', foreground='cyan')
label.pack(anchor='center')
waktu()
mainloop()
