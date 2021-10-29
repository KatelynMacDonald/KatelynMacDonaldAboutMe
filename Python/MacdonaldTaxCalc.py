from tkinter import *

groot = Tk()
groot.geometry("312x400")

expression=""
inputText=StringVar()


def btnClear():
    global expression
    expression=""
    inputText.set("")

def btnClick(btnTXT):
    global expression
    expression = expression + str(btnTXT)               #if the button is clicked it will add the value to the expression
    inputText.set(expression)

def radioBtnClick():                        #if the radio button is clicked it will add the value to the expression
    global expression
    expression = expression + str(radio.get())
    inputText.set(expression)

def btnEqual():
    global expression
    result=str(eval(expression))        #eval function evalutes the string expression
    inputText.set(result)
    expression=""




print("If you want a custom tax ammount just type in the box a * and the decimal number of the percent")

#frames

inputFrame = Frame(groot,width=312, height=50)
inputFrame.pack(side=TOP)

buttonFrame= Frame(groot,width=300,height=300)
buttonFrame.pack()


#entry field

inputField = Entry(inputFrame,font=('arial',18,'bold'),width=50,justify=RIGHT, textvariable=inputText)
inputField.grid(row=0,column=0)
inputField.pack()




radio=StringVar()           #this is the variable for the radio buttons
#buttons

btnC=Button(buttonFrame,width=32,height=3,text="C",command=btnClear).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
#btn10percent = Button(buttonFrame,width=10,height=3,text="10%",command=lambda:btnClick("*1.1")).grid(row=0,column=3,padx=1,pady=1)
btn10percent =Radiobutton(buttonFrame, text = "10%",variable=radio,command=radioBtnClick,value=("*1.1"), indicator = 0,background = "light blue").grid(row=0,column=3,padx=1,pady=1)



btn7 = Button(buttonFrame,width=10,height=3,text="7",command=lambda:btnClick("7")).grid(row=1,column=0,padx=1,pady=1)
btn8 = Button(buttonFrame,width=10,height=3,text="8",command=lambda:btnClick("8")).grid(row=1,column=1,padx=1,pady=1)
btn9 = Button(buttonFrame,width=10,height=3,text="9",command=lambda:btnClick("9")).grid(row=1,column=2,padx=1,pady=1)
#btn15percent = Button(buttonFrame,width=10,height=3,text="15%",command=lambda:btnClick("*1.15")).grid(row=1,column=3,padx=1,pady=1)
btn15percent =Radiobutton(buttonFrame, text = "15%",variable=radio,command=radioBtnClick,value=("*1.15"), indicator = 0,background = "light blue").grid(row=1,column=3,padx=1,pady=1)


btn4 = Button(buttonFrame,width=10,height=3,text="4",command=lambda:btnClick("4")).grid(row=2,column=0,padx=1,pady=1)
btn5 = Button(buttonFrame,width=10,height=3,text="5",command=lambda:btnClick("5")).grid(row=2,column=1,padx=1,pady=1)
btn6 = Button(buttonFrame,width=10,height=3,text="6",command=lambda:btnClick("6")).grid(row=2,column=2,padx=1,pady=1)
#btn20percent = Button(buttonFrame,width=10,height=3,text="20%",command=lambda:btnClick("*1.2")).grid(row=2,column=3,padx=1,pady=1)
btn20percent =Radiobutton(buttonFrame, text = "20%",variable=radio,command=radioBtnClick,value=("*1.2"), indicator = 0,background = "light blue").grid(row=2,column=3,padx=1,pady=1)



btn1 = Button(buttonFrame,width=10,height=3,text="1",command=lambda:btnClick("1")).grid(row=3,column=0,padx=1,pady=1)
btn2 = Button(buttonFrame,width=10,height=3,text="2",command=lambda:btnClick("2")).grid(row=3,column=1,padx=1,pady=1)
btn3 = Button(buttonFrame,width=10,height=3,text="3",command=lambda:btnClick("3")).grid(row=3,column=2,padx=1,pady=1)
#btn25percent = Button(buttonFrame,width=10,height=3,text="25%",command=lambda:btnClick("*1.25")).grid(row=3,column=3,padx=1,pady=1)
btn25percent =Radiobutton(buttonFrame, text = "25%",variable=radio,command=radioBtnClick,value=("*1.25"), indicator = 0,background = "light blue").grid(row=3,column=3,padx=1,pady=1)


btn0 =Button(buttonFrame,width=21,height=3,text="0",command=lambda:btnClick("0")).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
btnDot = Button(buttonFrame,width=10,height=3,text=".",command=lambda:btnClick(".")).grid(row=4,column=2,padx=1,pady=1)
btnEqual = Button(buttonFrame,width=10,height=3,text="=",command=btnEqual).grid(row=4,column=3,padx=1,pady=1)


labelFrame= Frame(groot)
labelFrame.pack()



text=Label(labelFrame, text="If you want a custom tax ammount \njust type in the box a * and the decimal\nnumber of the percent ",
    compound="center",font=("Times New Roman",14),bd=3,relief=FLAT,fg="mediumpurple3",bg="black").pack(padx=1)




groot.mainloop()