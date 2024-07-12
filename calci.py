import tkinter as tknt
on = False

def press(num):
    if on:
        global exp
        exp = exp + str(num)
        equation.set(exp)

def equalpress():
    if on:
        try:
            global exp
            total = str(eval(exp))
            equation.set(total)
            exp = ""
        except:
            equation.set(" error ")
            exp = ""

def clr():
    if on:
        global exp
        exp = ""
        equation.set("")

def delete():
    if on:
        global exp
        exp = exp[:-1]
        equation.set(exp)

def prcnt():
    if on:
        global exp
        try:
            rel = str(eval(exp) / 100)
            equation.set(rel)
            exp = ""
        except:
            equation.set(" error ")
            exp = ""

def turn_on():
    global on
    on = True
    clr()
    entry_box.config(state='normal')

def turn_off():
    global on
    on = False
    clr()
    entry_box.config(state='disabled')

if __name__ == "__main__":
    gui = tknt.Tk()
    gui.configure(background="black")
    gui.title("Simple Calculator")
    gui.geometry("271x380")

    exp = ""
    equation = tknt.StringVar()
    entry_box = tknt.Entry(gui, textvariable=equation, state='disabled', font=('Arial', 20), bd=15, insertwidth=6, width=16, borderwidth=4)
    entry_box.grid(columnspan=5, ipadx=10)
    btn1 = tknt.Button(gui, text=' 1 ', foreground='black', background='grey', command=lambda: press(1), height=3, width=8)
    btn1.grid(row=2, column=0)
    btn2 = tknt.Button(gui, text=' 2 ', foreground='black', background='grey', command=lambda: press(2), height=3, width=8)
    btn2.grid(row=2, column=1)
    btn3 = tknt.Button(gui, text=' 3 ', foreground='black', background='grey', command=lambda: press(3), height=3, width=8)
    btn3.grid(row=2, column=2)
    btn4 = tknt.Button(gui, text=' 4 ', foreground='black', background='grey', command=lambda: press(4), height=3, width=8)
    btn4.grid(row=3, column=0)
    btn5 = tknt.Button(gui, text=' 5 ', foreground='black', background='grey', command=lambda: press(5), height=3, width=8)
    btn5.grid(row=3, column=1)
    btn6 = tknt.Button(gui, text=' 6 ', foreground='black', background='grey', command=lambda: press(6), height=3, width=8)
    btn6.grid(row=3, column=2)
    btn7 = tknt.Button(gui, text=' 7 ', foreground='black', background='grey', command=lambda: press(7), height=3, width=8)
    btn7.grid(row=4, column=0)
    btn8 = tknt.Button(gui, text=' 8 ', foreground='black', background='grey', command=lambda: press(8), height=3, width=8)
    btn8.grid(row=4, column=1)
    btn9 = tknt.Button(gui, text=' 9 ', foreground='black', background='grey', command=lambda: press(9), height=3, width=8)
    btn9.grid(row=4, column=2)
    btn0 = tknt.Button(gui, text=' 0 ', foreground='black', background='grey', command=lambda: press(0), height=3, width=8)
    btn0.grid(row=5, column=0)

    plus = tknt.Button(gui, text=' + ', foreground='black', background='light blue', command=lambda: press("+"), height=3, width=8)
    plus.grid(row=2, column=3)
    minus = tknt.Button(gui, text=' - ', foreground='black', background='light blue', command=lambda: press("-"), height=3, width=8)
    minus.grid(row=3, column=3)
    multiply = tknt.Button(gui, text=' * ', foreground='black', background='light blue', command=lambda: press("*"), height=3, width=8)
    multiply.grid(row=4, column=3)
    divide = tknt.Button(gui, text=' / ', foreground='black', background='light blue', command=lambda: press("/"), height=3, width=8)
    divide.grid(row=5, column=3)

    equal = tknt.Button(gui, text=' = ', foreground='black', background='yellow', command=equalpress, height=3, width=8)
    equal.grid(row=6, column=0, columnspan=4, sticky="nsew")
    clr = tknt.Button(gui, text='clr', foreground='black', background='light blue', command=clr, height=3, width=8)
    clr.grid(row=1, column=2)
    delete= tknt.Button(gui, text='Del', foreground='black', background='light blue', command=delete, height=3, width=8)
    delete.grid(row=1, column=3)
    dot= tknt.Button(gui, text=' . ', foreground='black', background='grey', command=lambda: press("."), height=3, width=8)
    dot.grid(row=5, column=1)
    prcnt = tknt.Button(gui, text=' % ', foreground='black', background='light blue', command=prcnt, height=3, width=8)
    prcnt.grid(row=5, column=2)

    on = tknt.Button(gui, text='ON', foreground='black', background='green', command=turn_on, height=3, width=8)
    on.grid(row=1, column=0)
    off = tknt.Button(gui, text='OFF', foreground='black', background='red', command=turn_off, height=3, width=8)
    off.grid(row=1, column=1)

    gui.mainloop()
