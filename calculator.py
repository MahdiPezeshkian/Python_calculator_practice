from tkinter import *

#main window
calculator = Tk()
calculator.geometry("150x170")
calculator.resizable(width = False , height = False)
calculator.title("calculator")


number1 = IntVar()
number1s = StringVar()


number2 = IntVar()
number2s = StringVar()

operator = StringVar()

jam = StringVar()

result = StringVar()




def _1():
    if number1s.get() == "":
        i = "1"
        l = "" + i
        number1.set(1)
        number1s.set("l")
    elif number2s.get() == "":
        number2.set(1)
        number2s.set("1")


def _2():
    if number1s.get() == "":
        number1.set(2)
        number1s.set("2")
    elif number2s.get() == "":
        number2.set(2)
        number2s.set("2")

def _3():
    if number1s.get() == "":
        number1.set(3)
        number1s.set("3")
    elif number2s.get() == "":
        number2.set(3)
        number2s.set("3")

def _4():
    if number1s.get() == "":
        number1.set(4)
        number1s.set("4")
    elif number2s.get() == "":
        number2.set(4)
        number2s.set("4")

def _5():
    if number1s.get() == "":
        number1.set(5)
        number1s.set("5")
    elif number2s.get() == "":
        number2.set(5)
        number2s.set("5")

def _6():
    if number1s.get() == "":
        number1.set(6)
        number1s.set("6")
    elif number2s.get() == "":
        number2.set(6)
        number2s.set("6")

def _7():
    if number1s.get() == "":
        number1.set(7)
        number1s.set("7")
    elif number2s.get() == "":
        number2.set(7)
        number2s.set("7")

def _8():
    if number1s.get() == "":
        number1.set(8)
        number1s.set("8")
    elif number2s.get() == "":
        number2.set(8)
        number2s.set("8")

def _9():
    if number1s.get() == "":
        number1.set(9)
        number1s.set("9")
    elif number2s.get() == "":
        number2.set(9)
        number2s.set("9")

def _0():
    if number1s.get() == "":
        number1.set(0)
        number1s.set("0")
    elif number2s.get() == "":
        number2.set(0)
        number2s.set("0")


def _J():
    operator.set("+")
    result.set(number1.get() + number2.get())

def _T():
    operator.set("-")
    

def _Z():
    operator.set("*")
 

def _TH():
    operator.set("/")
   

def _M():
    if operator.get() == "+":
        result.set(number1.get() + number2.get())
        jam.set("= ")
    elif operator.get() == "*":
        result.set(number1.get() * number2.get())
        jam.set("= ")
    elif operator.get() == "-":
        result.set(number1.get() - number2.get())
        jam.set("= ")
    elif operator.get() == "/":
        result.set(number1.get() / number2.get())
        jam.set("= ")




    








btn1 = Button(calculator , text="1" , command=lambda:_1())
btn1.place( x = 20 , y = 40)

btn2 = Button(calculator , text="2" , command=lambda:_2() )
btn2.place( x = 50 , y = 40)

btn3 = Button(calculator , text="3" , command=lambda:_3() )
btn3.place( x = 80 , y = 40)

btn4= Button(calculator , text="4" , command=lambda:_4() )
btn4.place( x = 20 , y = 70)

btn5 = Button(calculator , text="5" , command=lambda:_5() )
btn5.place( x = 50 , y = 70)

btn6 = Button(calculator , text="6" , command=lambda:_6() )
btn6.place( x = 80 , y = 70)

btn7 = Button(calculator , text="7" , command=lambda:_7() )
btn7.place( x = 20 , y = 100)

btn8 = Button(calculator , text="8" , command=lambda:_8() )
btn8.place( x = 50 , y = 100)

btn9 = Button(calculator , text="9" , command=lambda:_9() )
btn9.place( x = 80 , y = 100)

btn0 = Button(calculator , text="9" , command=lambda:_0() )
btn0.place( x = 50 , y = 130)

btnJ = Button(calculator , text="+" , command=lambda:_J() )
btnJ.place( x = 110 , y = 40)

btnT = Button(calculator , text="- " , command=lambda:_T() )
btnT.place( x = 110 , y = 70)

btnZ = Button(calculator , text="* " , command=lambda:_Z() )
btnZ.place( x = 110 , y = 100)

btnTG = Button(calculator , text="/ " , command=lambda:_TH() )
btnTG.place( x = 110 , y = 130)

btnM = Button(calculator , text="=" , command=lambda:_M())
btnM.place(  x = 80 , y = 130)

#Label
output = Label(calculator , textvariable=number1s )
output.place( x = 20 , y = 10)

output_3 = Label(calculator , textvariable=operator )
output_3.place( x = 40 , y = 10)

output_2 = Label(calculator , textvariable=number2s )
output_2.place( x = 50 , y = 10)

output_5 = Label(calculator , textvariable= jam)
output_5.place( x = 70 , y = 10)


output_4 = Label(calculator , textvariable= result)
output_4.place( x = 90 , y = 10)


print("no error")












calculator.mainloop()