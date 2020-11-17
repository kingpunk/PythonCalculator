from tkinter import *

root = Tk()

addNumber = 0

root.title("Simple Calculator")

#text Feild
inputNumber = Entry(root, width=35, borderwidth=5)
inputNumber.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#functions

def buttonClicked(nummber):
  # inputNumber.delete(0, END)
  current = inputNumber.get()
  inputNumber.delete(0, END)
  inputNumber.insert(0, str(current) + str(nummber))
  

def buttonClear():
  inputNumber.delete(0, END)


def buttonAdd(numberAdd):
  global addNumber
  addNumber = numberAdd
  buttonClear()



def buttonEquals():
  secondNumber = int(inputNumber.get())
  buttonClear()
  inputNumber.insert(0, addNumber + secondNumber)
  



#Button

button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:buttonClicked(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:buttonClicked(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:buttonClicked(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:buttonClicked(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:buttonClicked(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:buttonClicked(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:buttonClicked(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:buttonClicked(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:buttonClicked(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda:buttonClicked(0))

#add Button
button_add = Button(root, text="+", padx=39, pady=20, command=lambda:buttonAdd(int(inputNumber.get())))

#equal button
button_equal = Button(root, text="=", padx=91, pady=20, command=buttonEquals)

#clear button
button_clear = Button(root, text="clear", padx=79, pady=20, command=buttonClear)


#Enterying button On Screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)


button_add.grid(row=5, column=0)

button_equal.grid(row=5, column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)


root.mainloop()