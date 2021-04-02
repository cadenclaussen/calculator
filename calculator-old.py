from tkinter import *


currentNumber = ""
currentNumberInt = 0
lastNumber = 0
operation = ""
memory = 0


def main():
    global currentNumber, currentNumberInt, lastNumber, operation, memory

    master = Tk()
    master.title("Calculator")
    master.geometry("475x710")

    Button(master, text="MS", command=memorySave, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=1, column=0)
    Button(master, text="MR", command=memoryRecall, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=1, column=1)
    Button(master, text="MC", command=memoryClear, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=1, column=2)
    Button(master, text="M-", command=memoryMinus, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=1, column=3)
    Button(master, text="M+", command=memoryPlus, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=1, column=4)

    Button(master, text="√", command=calculationSquareRoot, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=2, column=0)
    Button(master, text="∛", command=calculationCubeRoot, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=2, column=1)
    Button(master, text="㎡", command=calculationSquared, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=2, column=2)
    Button(master, text="㎥", command=calculationCubed, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=2, column=3)
    Button(master, text="÷", command=mathDivide, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=2, column=4)

    Button(master, text="%", command=modifyPercent, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=3, column=0)
    Button(master, text="7", command=number7, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=3, column=1)
    Button(master, text="8", command=number8, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=3, column=2)
    Button(master, text="9", command=number9, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=3, column=3)
    Button(master, text="x", command=mathMultiply, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=3, column=4)

    Button(master, text="±", command=modifyNegate, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=4, column=0)
    Button(master, text="4", command=number4, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=4, column=1)
    Button(master, text="5", command=number5, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=4, column=2)
    Button(master, text="6", command=number6, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=4, column=3)
    Button(master, text="-", command=mathSubtraction, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=4, column=4)

    Button(master, text="C", command=clear, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=5, column=0)
    Button(master, text="1", command=number1, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=5, column=1)
    Button(master, text="2", command=number2, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=5, column=2)
    Button(master, text="3", command=number3, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=5, column=3)
    Button(master, text="+", command=mathAdd, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(rowspan=2, row=5, column=4, sticky=N+S)

    Button(master, text="AC", command=clearAll, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=6, column=0)
    Button(master, text="0", command=number0, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=6, column=1)
    Button(master, text=".", command=modifyDecimal, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=6, column=2)
    Button(master, text="=", command=mathEquals, font=("Helvetica", 24), height=3, width=5, padx=5, pady=5).grid(row=6, column=3)

    currentNumber = StringVar()
    setCurrentNumber(0)
    Label(master, textvar=currentNumber, font=("Helvetica", 32), justify=RIGHT, anchor=E, height=1, width=5, padx=10, pady=10, borderwidth=5, bg="light grey", fg="black").grid(columnspan=5, row=0, column=0, sticky=W+E)

    master.mainloop()


def number(n):
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    setCurrentNumber(currentNumberInt * 10 + n)
    print("number", n)

def number0():
    number(0)

def number1():
    number(1)

def number2():
    number(2)

def number3():
    number(3)

def number4():
    number(4)

def number5():
    number(5)

def number6():
    number(6)

def number7():
    number(7)


def number8():
    number(8)

def number9():
    number(9)

def mathAdd():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("mathAdd")
    operation = "add"

def mathSubtraction():
    print("mathSubtraction")

def mathMultiply():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("mathMultiply")

def mathDivide():
    print("mathDivide")

def mathEquals():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    currentNumber = (currentNumber, operation)

def calculationSquareRoot():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("calculationSquareRoot")

def calculationCubeRoot():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("calculationFourthPower")

def calculationSquared():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("calculationSquared")

def calculationCubed():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("calculationCubed")

def clear():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("clear")

def clearAll():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    setCurrentNumber(0)

def memoryClear():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("memoryClear")

def memoryMinus():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("memoryMinus")

def memoryPlus():
    print("memoryPlus")

def memoryRecall():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("memoryRecall")

def memorySave():
    global currentNumber, currentNumberInt, lastNumber, operation, memory

def modifyDecimal():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("modifyDecimal")

def modifyNegate():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("modifyNegate")

def modifyPercent():
    global currentNumber, currentNumberInt, lastNumber, operation, memory
    print("modifyPercent")


def setCurrentNumber(n):
    global currentNumberInt, currentNumber
    currentNumberInt = n
    currentNumber.set(n)
    print("currentNumber", currentNumber.get())
    print("currentNumberInt", currentNumberInt)

main()
