from tkinter import *

window=Tk()
window.title("Calculator")
window.geometry("500x700")
window.configure(bg="#f0f0f0")
window.resizable(False,False)

#Entrybox
entry=Entry(window,width=32,font=("Arial",20),bg="white",fg="black",borderwidth=2)
entry.place(x=5,y=10)

#Function
def click(num):
    result=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(result)+str(num))

#Buttons
button1=Button(window,text="1",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=lambda:click(1))
button1.place(x=20,y=70)

button2=Button(window,text="2",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=lambda:click(2))
button2.place(x=120,y=70)

button3=Button(window,text="3",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=lambda:click(3))
button3.place(x=220,y=70)

button4=Button(window,text="4",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=lambda:click(4))
button4.place(x=20,y=150)

button5=Button(window,text="5",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=lambda:click(5))
button5.place(x=120,y=150)

button6=Button(window,text="6",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=lambda:click(6))
button6.place(x=220,y=150)

button7=Button(window,text="7",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=lambda:click(7))
button7.place(x=20,y=230)

button8=Button(window,text="8",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=lambda:click(8))
button8.place(x=120,y=230)

button9=Button(window,text="9",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=lambda:click(9))
button9.place(x=220,y=230)

button0=Button(window,text="0",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=lambda:click(0))
button0.place(x=120,y=310)

#Operators

def add():
    n1=entry.get()
    global math
    math="addition"
    global i
    i=int(n1)
    entry.delete(0,END)

button_add=Button(window,text="+",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=add)
button_add.place(x=320,y=70)

def sub():
    n1=entry.get()
    global math
    math="subtraction"
    global i
    i=int(n1)
    entry.delete(0,END)

button_sub=Button(window,text="-",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=sub)
button_sub.place(x=320,y=150)

def mul():
    n1=entry.get()
    global math
    math="multiplication"
    global i
    i=int(n1)
    entry.delete(0,END)

button_mul=Button(window,text="*",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=mul)
button_mul.place(x=320,y=230)

def div():
    n1=entry.get()
    global math
    math="division"

    global i
    i=int(n1)
    entry.delete(0,END)
button_div=Button(window,text="/",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=div)
button_div.place(x=320,y=310)

def equal():
    n2=entry.get()
    entry.delete(0,END)
    if math=="addition":
        entry.insert(0,i+int(n2))
    elif math=="subtraction":
        entry.insert(0,i-int(n2))
    elif math=="multiplication":
        entry.insert(0,i*int(n2))
    elif math=="division":
        entry.insert(0,i/int(n2))



button_eq=Button(window,text="=",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=equal)
button_eq.place(x=220,y=310)

def clear():
    entry.delete(0,END)

button_clear=Button(window,text="C",height=3,width=7,font=("Arial",12,"bold"),cursor="hand2",command=clear)
button_clear.place(x=20,y=310)




window.mainloop()