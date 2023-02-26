from tkinter import *      #tk คือโปรแกรม
from tkinter import ttk    #theme of tk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')                  #ขนาดหน้าโปรแกรม

def Button1():                           #คลิกแล้วขึ้นป๊อปอัพ
    Text = 'Error'
    messagebox.showerror('เงินในบัญชี',Text)
B1 = ttk.Button(GUI,text='B1',command=Button1)
B1.pack(ipadx=20,ipady=20)               #ipad xบวกไปอีก20pixel y+20pixel


###
def Button2():                           #คลิกแล้วขึ้นป๊อปอัพ
    Text = 'ตอนนี้มี200'
    messagebox.showinfo('เงินในบัญชี',Text)

FB1 = Frame(GUI)
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='B2',command=Button2)
B2.pack(ipadx=20,ipady=20)
###
GUI.mainloop()