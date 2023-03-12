from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('Data Recording Program')
GUI.geometry('500x400')
GUI['bg'] = 'orange'

style = ttk.Style()
style.configure('TButton', background='blue', foreground='blue')

L1 = Label(GUI,text='รายรับรายจ่าย', font=('Angsana New',30),fg='green')
L1.grid(row=0,column=0,columnspan=2)

def Button1():
    text = 'ตอนนี้มีเงินในบัญชี  ' + str(int(E1.get()) - int(E2.get())) + 'บาท'
    messagebox.showinfo('เงินในบัญชี',text)
    
L2 = Label(GUI,text='รายได้', font=('Angsana New',15),fg='black')
L2.grid(row=1,column=0,padx=20,pady=20,sticky='W')

E1 = Entry(GUI)
E1.grid(row=1,column=1,padx=20,pady=20)

L3 = Label(GUI,text='รายจ่าย', font=('Angsana New',15),fg='black')
L3.grid(row=2,column=1,padx=20,pady=20,sticky='W')

GUI.mainloop()