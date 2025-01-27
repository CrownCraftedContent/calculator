from tkinter import *


def buttonPress(passed):
    global equation_text
    equation_text = equation_text + str(passed)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))  # eval will parse the expression passed into it
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:  # cannot divide by zero
        equation_label.set("arithmetic error")
        equation_text = ""
    except SyntaxError:  # cannot jumble operation characters together improperly (grammar)
        equation_label.set("syntax error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


window = Tk()
window.title("Crowned Calculator")
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Consolas',20), bg='white', width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: buttonPress(1))
button1.grid(row=0,column=0)
button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: buttonPress(2))
button2.grid(row=0, column=1)
button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: buttonPress(3))
button3.grid(row=0, column=2)
button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: buttonPress(4))
button4.grid(row=1,column=0)
button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: buttonPress(5))
button5.grid(row=1, column=1)
button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: buttonPress(6))
button6.grid(row=1, column=2)
button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: buttonPress(7))
button7.grid(row=2,column=0)
button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: buttonPress(8))
button8.grid(row=2, column=1)
button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: buttonPress(9))
button9.grid(row=2, column=2)
button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: buttonPress(0))
button0.grid(row=3, column=0)
# Operations
plus = Button(frame, text="+", height=4, width=9, font=35,
                 command=lambda: buttonPress("+"))
plus.grid(row=0, column=3)
minus = Button(frame, text="-", height=4, width=9, font=35,
                 command=lambda: buttonPress("-"))
minus.grid(row=1, column=3)
multiply = Button(frame, text="*", height=4, width=9, font=35,
                 command=lambda: buttonPress("*"))
multiply.grid(row=2, column=3)
divide = Button(frame, text="/", height=4, width=9, font=35,
                 command=lambda: buttonPress("/"))
divide.grid(row=3, column=3)
equal = Button(frame, text="=", height=4, width=9, font=35,
                 command=equals)
equal.grid(row=3, column=2)
decimal = Button(frame, text=".", height=4, width=9, font=35,
                 command=lambda: buttonPress("."))
decimal.grid(row=3, column=1)

clear = Button(window, text="clear", height=4, width=12, font=35,
                 command=clear)
clear.pack()
window.mainloop()
