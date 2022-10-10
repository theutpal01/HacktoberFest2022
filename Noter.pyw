from tkinter import *
notepad=Tk()
h,w=1200,700
notepad.title("Noter")
notepad.geometry("1200x700")
notepad.config(bg="white")

text=Text(notepad,bg="white"
          ,width=h,height=h,font="100",border=0,fg="red")

text.insert(1.0,"#// Developer >>>>Yuvraj<<<< version: 1.1  \n\n")
text.insert(2.0,"")
text.pack()


notepad.mainloop()
      
