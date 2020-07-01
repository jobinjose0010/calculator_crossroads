from tkinter import *
window = Tk()
window.geometry("400x700")
window.maxsize(400,700)
window.minsize(400,700)
window.title("Calculator")
window.config(bg = "#222222")

#************* Frame Setting ********************
screen_frame = Frame(window,background="red")
button_frame = Frame(window,background="red")
screen_frame.place(x=0,y=0,width=400,height=180)
button_frame.place(x=0,y=220,width=400,height=400)

window.mainloop()