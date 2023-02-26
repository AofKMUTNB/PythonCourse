from tkinter import *
space =Tk()
space.title('My Calculator')
#space.geometry("500*500")
#space.configure(bg="#2d2d2d")


content =""
txt_input = StringVar(value="0")


def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

    
def equal():
    global content
    calculate = float(eval(content))
    txt_input.set(calculate)

    
display = Entry(font=('arial',30,'bold'),fg="black",bg="#f6f6f6",textvariable=txt_input,justify='right')
display.grid(columnspan=4,padx=0,pady=0)


def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,"8")

btn7 = Button(fg="black",font=('arial',30,'bold'),text="7",command=lambda:btn(7),padx=30,pady=15).grid(row=1, column=0)
btn8 = Button(fg="black",font=('arial',30,'bold'),text="8",command=lambda:btn(7),padx=30,pady=15).grid(row=1, column=1)
btn9 = Button(fg="black",font=('arial',30,'bold'),text="9",command=lambda:btn(7),padx=30,pady=15).grid(row=1, column=2)
