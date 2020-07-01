from tkinter import *
window = Tk()
window.geometry("400x700")
window.maxsize(400,700)
window.minsize(400,700)
window.title("Calculator")
window.config(bg = "#222222")

operationText = StringVar()
resultText = StringVar()

#************* Frame Setting ********************
screen_frame = Frame(window,background="#222222")
button_frame = Frame(window,background="#222222")
screen_frame.place(x=0,y=0,width=400,height=180)
button_frame.place(x=0,y=220,width=400,height=400)


#************* Elements Settings ****************
screen_input = Entry(screen_frame,width=34,font=3,background="#222222",relief=FLAT,fg="white",justify=RIGHT,textvariable = operationText)
screen_input.place(x=15,y=100)
screen_output = Entry(screen_frame,width=15,font =("Courier",30),background="#222222",relief=FLAT,fg="#1E78FF",justify=RIGHT,textvariable = resultText)
screen_output.place(x=27,y=130)
operationText.set("352+458-485")
resultText.set("1250")

window.mainloop()