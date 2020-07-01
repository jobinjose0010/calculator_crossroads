from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()
window.geometry("435x650")
window.maxsize(435,650)
window.minsize(435,650)
window.title("Calculator")
window.config(bg = "#00334e")

operationText = StringVar()
resultText = StringVar()
values=""
values_final=""

def onclick(event=NONE):
    messagebox.showinfo("Info", "Calculator developed by Jobin Jose for Python Challenge conducted by CrossRoads, contact:9847506341, jobinjose0010@gmail.com")

def key_val(value):
    global values
    values = values+value
    operationText.set(values)

def key_equal():
    global values
    values_final = str(eval(values))
    resultText.set(values_final)

def key_C():
    global values
    global values_final
    operationText.set("0")
    resultText.set("0")
    values = ""
    values_final = ""

def key_CE():
    global values
    temp = operationText.get()
    temp = temp[:-1]
    operationText.set(temp)
    values = temp


#************* Frame Setting ********************
screen_frame = Frame(window,background="#00334e")
button_frame = Frame(window,background="#00334e")
screen_frame.place(x=0,y=0,width=400,height=180)
button_frame.place(x=5,y=220,width=410,height=400)


#************* Elements Settings ****************
img = ImageTk.PhotoImage(Image.open("icon.png"))
panel = Label(window, image = img,bg="#00334e")
panel.place(x=400,y=10,width=30,height=30)
panel.bind('<Button-1>', onclick)
screen_input = Entry(screen_frame,width=34,font=3,background="#00334e",relief=FLAT,fg="white",justify=RIGHT,textvariable = operationText)
screen_input.place(x=15,y=100)
screen_output = Entry(screen_frame,width=15,font =("Courier",30),background="#00334e",relief=FLAT,fg="#1E78FF",justify=RIGHT,textvariable = resultText)
screen_output.place(x=27,y=130)
operationText.set("0")
resultText.set("0")

#************* Buttons Settings *****************
button_C = Button(button_frame,width=7,height=3,text="C",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=key_C)
button_C.grid(row=0,column=0,padx=19,pady=10)
button_CE = Button(button_frame,width=7,height=3,text="CE",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=key_CE)
button_CE.grid(row=0,column=1,padx=19,pady=10)
button_perc = Button(button_frame,width=7,height=3,text="%",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("%"))
button_perc.grid(row=0,column=2,padx=19,pady=10)
button_Div = Button(button_frame,width=7,height=3,text="/",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("/"))
button_Div.grid(row=0,column=3,padx=19,pady=10)

button_7 = Button(button_frame,width=7,height=3,text="7",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("7"))
button_7.grid(row=1,column=0,padx=19,pady=10)
button_8 = Button(button_frame,width=7,height=3,text="8",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("8"))
button_8.grid(row=1,column=1,padx=19,pady=10)
button_9 = Button(button_frame,width=7,height=3,text="9",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("9"))
button_9.grid(row=1,column=2,padx=19,pady=10)
button_mul = Button(button_frame,width=7,height=3,text="X",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("*"))
button_mul.grid(row=1,column=3,padx=19,pady=10)

button_4 = Button(button_frame,width=7,height=3,text="4",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("4"))
button_4.grid(row=2,column=0,padx=19,pady=10)
button_5 = Button(button_frame,width=7,height=3,text="5",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("5"))
button_5.grid(row=2,column=1,padx=19,pady=10)
button_6 = Button(button_frame,width=7,height=3,text="6",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("6"))
button_6.grid(row=2,column=2,padx=19,pady=10)
button_sub = Button(button_frame,width=7,height=3,text="_",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("-"))
button_sub.grid(row=2,column=3,padx=19,pady=10)

button_1 = Button(button_frame,width=7,height=3,text="1",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("1"))
button_1.grid(row=3,column=0,padx=19,pady=10)
button_2 = Button(button_frame,width=7,height=3,text="2",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("2"))
button_2.grid(row=3,column=1,padx=19,pady=10)
button_3 = Button(button_frame,width=7,height=3,text="3",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("3"))
button_3.grid(row=3,column=2,padx=19,pady=10)
button_add = Button(button_frame,width=7,height=3,text="+",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("+"))
button_add.grid(row=3,column=3,padx=19,pady=10)

button_0 = Button(button_frame,width=7,height=3,text="0",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("0"))
button_0.grid(row=4,column=0,padx=19,pady=10)
button_dot = Button(button_frame,width=7,height=3,text=".",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("."))
button_dot.grid(row=4,column=1,padx=19,pady=10)
button_eq = Button(button_frame,width=22,height=3,text="EQUAL(=)",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=key_equal)
button_eq.grid(row=4,column=2,padx=19,pady=10,columnspan=2)

window.mainloop()