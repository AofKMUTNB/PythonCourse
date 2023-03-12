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

def Button1() :
    formula = str()
    text= 'You can do it'
    messagebox.showinfo('let do it',text)

FB1 = Frame(GUI)
FB1.place(x=295,y=220)
B2 = ttk.Button(FB1,text='Do it',command=Button1)
B2.pack(ipadx=10,ipady=15)

Box1 = ttk.Entry(LB1)
Box1.grid(row=2,column=0,padx=20,pady=20)
GUI.mainloop()