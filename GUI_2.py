from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('Daily')
GUI.geometry('700x500')

L1 =Label(GUI,text='**DAILY**',font=('Supermarket',30),fg='Red' )
L1.pack(ipadx=10,ipady=20)

LB1 = LabelFrame(GUI,text='To do list')
LB1.pack(ipadx=10,ipady=5)

FB2 =Frame(GUI)
FB2.place(x=100,y=80)

GUI.mainloop()