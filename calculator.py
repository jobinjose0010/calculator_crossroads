from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from math import *

window = Tk()
window.geometry("435x750")
window.maxsize(435,750)
window.minsize(435,750)
window.title("Calculator")
window.config(bg = "#00334e")
window.iconbitmap('iconmain.ico')
operationText = StringVar()
resultText = StringVar()

values=""
values_final=""

def onclick(event=NONE):
    info_msg= "Calculator developed by Jobin Jose for Python Challenge conducted by CrossRoads,\n\ncontact no: 9847506341\nEmail:\tjobinjose0010@gmail.com ,\n\tjobinjoseonline@gmail.com\n\n" \
              "Basic Features:\n\t* I have included most needed operations in this\n\t calculator\n\t* If any error from user part will give an alert\n\tmessage that contains the problem.\n\n" \
              "Basic errors:\n\t* Division by Zero\n\t* Usage of SQRT in wrong way\n\t* Other wrong Mathematical Syntaxes\n\nBasic Usages:\n\t" \
              "'SQRT' Usage:\n\tstep1:- click on '√' button\n\tstep2:- click on '(' button\n\t"\
              "step3:- Enter the number to find Square Root\n\tstep5:- click on ')' button\n\n\t" \
              "'Ans' Usage:\n\tInorder to use 'Ans' function you must have an\n\tanswer in the answer display(second display)\n\t'Ans' will add the previous final result into the\n\toperator screen"
    messagebox.showinfo("Info",info_msg)

def key_val(value):
    global values
    values = values+value
    operationText.set(values)

def key_equal():
    try:
        global values
        values_final = str(eval(values))
        if(values_final=="<built-in function sqrt>"):
            text_err = "No values is assigned for SQRT \n\nSQRT is ued in wrong way\n\tusage:\n\tstep1:- click on '√' button\n\tstep2:- click on '(' button\n\t" \
                 "step3:- Enter the number to find Square Root\n\tstep5:- click on ')' button"
            messagebox.showwarning('Warning',text_err)
        else:
            resultText.set(values_final)

    except(ZeroDivisionError):
        error1 = "Division by Zero is not acceptable"
        messagebox.showwarning("warning",error1)

    except:
        error2 = "Reasons for Error:\n\nReason1:- SQRT is ued in wrong way\n\tusage:\n\tstep1:- click on '√' button\n\tstep2:- click on '(' button\n\t" \
                 "step3:- Enter the number to find Square Root\n\tstep5:- click on ')' button\n\nReason2:- Typed wrong math structure"
        messagebox.showwarning("warning",error2)


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
    if(temp == ""):
        operationText.set("0")

def Ans():
    global  values
    ans_value = str(resultText.get())
    if(ans_value == "0"):
        messagebox.showwarning('Warning',"'Ans' should use if you have a result in the Second Display(Result display)")
    else:
        values = values + ans_value
    operationText.set(values)



#************* Frame Setting ********************
screen_frame = Frame(window,background="#00334e")
button_frame = Frame(window,background="#00334e")
screen_frame.place(x=0,y=0,width=400,height=180)
button_frame.place(x=5,y=220,width=410,height=500)


#************* Elements Settings ****************
heading = Label(screen_frame,text='My Calculator',fg="white",width=15,font=("segoe ui",18,"bold"),background="#00334e")
heading.place(x=1,y=10)
sub_heading = Label(screen_frame,text='CrossRoads python challenge',fg="#1E78FF",width=25,font=("segoe ui",8,"bold"),background="#00334e")
sub_heading.place(x=35,y=45)
img = ImageTk.PhotoImage(Image.open("icon.png"))
panel = Label(window, image = img,bg="#00334e")
panel.place(x=400,y=10,width=30,height=30)
panel.bind('<Button-1>', onclick)
screen_input = Label(screen_frame,width=34,font=3,background="#00334e",relief=FLAT,fg="white",anchor='e',textvariable = operationText)
screen_input.place(x=15,y=100)
screen_output = Label(screen_frame,width=15,font =("Courier",30),background="#00334e",relief=FLAT,fg="#1E78FF",anchor='e',textvariable = resultText)
screen_output.place(x=27,y=130)
operationText.set("0")
resultText.set("0")

#************* Buttons Settings *****************
button_C = Button(button_frame,width=7,height=3,text="C",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=key_C)
button_C.grid(row=0,column=0,padx=19,pady=10)
button_CE = Button(button_frame,width=7,height=3,text="CE",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=key_CE)
button_CE.grid(row=0,column=1,padx=19,pady=10)
button_ans = Button(button_frame,width=7,height=3,text="Ans",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=Ans)
button_ans.grid(row=0,column=2,padx=19,pady=10)
button_root = Button(button_frame,width=7,height=3,text="√",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("sqrt"))
button_root.grid(row=0,column=3,padx=19,pady=10)

button_right = Button(button_frame,width=7,height=3,text="(",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("("))
button_right.grid(row=1,column=0,padx=19,pady=10)
button_left = Button(button_frame,width=7,height=3,text=")",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val(")"))
button_left.grid(row=1,column=1,padx=19,pady=10)
button_perc = Button(button_frame,width=7,height=3,text="%",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("%"))
button_perc.grid(row=1,column=2,padx=19,pady=10)
button_Div = Button(button_frame,width=7,height=3,text="/",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("/"))
button_Div.grid(row=1,column=3,padx=19,pady=10)

button_7 = Button(button_frame,width=7,height=3,text="7",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("7"))
button_7.grid(row=2,column=0,padx=19,pady=10)
button_8 = Button(button_frame,width=7,height=3,text="8",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("8"))
button_8.grid(row=2,column=1,padx=19,pady=10)
button_9 = Button(button_frame,width=7,height=3,text="9",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("9"))
button_9.grid(row=2,column=2,padx=19,pady=10)
button_mul = Button(button_frame,width=7,height=3,text="X",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("*"))
button_mul.grid(row=2,column=3,padx=19,pady=10)

button_4 = Button(button_frame,width=7,height=3,text="4",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("4"))
button_4.grid(row=3,column=0,padx=19,pady=10)
button_5 = Button(button_frame,width=7,height=3,text="5",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("5"))
button_5.grid(row=3,column=1,padx=19,pady=10)
button_6 = Button(button_frame,width=7,height=3,text="6",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("6"))
button_6.grid(row=3,column=2,padx=19,pady=10)
button_sub = Button(button_frame,width=7,height=3,text="_",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("-"))
button_sub.grid(row=3,column=3,padx=19,pady=10)

button_1 = Button(button_frame,width=7,height=3,text="1",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("1"))
button_1.grid(row=4,column=0,padx=19,pady=10)
button_2 = Button(button_frame,width=7,height=3,text="2",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("2"))
button_2.grid(row=4,column=1,padx=19,pady=10)
button_3 = Button(button_frame,width=7,height=3,text="3",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("3"))
button_3.grid(row=4,column=2,padx=19,pady=10)
button_add = Button(button_frame,width=7,height=3,text="+",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=lambda: key_val("+"))
button_add.grid(row=4,column=3,padx=19,pady=10)

button_0 = Button(button_frame,width=7,height=3,text="0",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("0"))
button_0.grid(row=5,column=0,padx=19,pady=10)
button_dot = Button(button_frame,width=7,height=3,text=".",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#ffffff",command=lambda: key_val("."))
button_dot.grid(row=5,column=1,padx=19,pady=10)
button_eq = Button(button_frame,width=22,height=3,text="EQUAL(=)",font=("segoe ui",10,"bold"),bg="#004d73",relief=SUNKEN,fg="#FFB200",command=key_equal)
button_eq.grid(row=5,column=2,padx=19,pady=10,columnspan=2)

window.mainloop()