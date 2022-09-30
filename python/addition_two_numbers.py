import tkinter
from tkinter import *

sum_result = 0
def sum():
    f_number = int(first_number.get())
    s_number = int(second_number.get())
    sum_result = f_number + s_number
    result_text_print["text"] = f"The result is: {sum_result}" 
    
window = tkinter.Tk()
window.title("Addition of two numbers")

text_orientation = tkinter.Label(window, text="What's first number?", width=45)
text_orientation.pack()

first_number = tkinter.Entry(window)
first_number.pack()

second_text = tkinter.Label(window, text="What's second number?")
second_text.pack()

second_number = tkinter.Entry(window)
second_number.pack()

sum_btn = tkinter.Button(text="Sum!", command=sum)
sum_btn.pack()

result_text_print = tkinter.Label(text="", height=3)
result_text_print.pack()

window.mainloop()