from tkinter import *              #the * = wildcord or when you import, it is everything


groot = Tk()
groot.configure(bg='black')


frameEntry= Frame(groot,pady=10,bg="black")
frameEntry.pack()

#(rdsB4FinalPercentage * 80) + (finalExamPercentage * 20) = Final Grade      so you'll want to calucalte the finalExamPercentage for this problem


def calculate():
    global currentGradeEntry,gradeYouWantEntry,finalExamEntry
    currentGrade=currentGradeEntry.get()
    finalGrade=gradeYouWantEntry.get()
    while finalGrade.isalpha()==True or currentGrade.isalpha()==True:       #this checks to see if there are any numbers in the entry
        if finalGrade.isalpha()==True:                                  #if there is it will print that it needs to be a number
            gradeYouWantEntry.delete(0,END)
            gradeYouWantEntry.insert(END,"Needs to be a number")
            gradeYouWantEntry.update()
        else: 
            currentGradeEntry.delete(0,END)
            currentGradeEntry.insert(END,"Needs to be a number")
            currentGradeEntry.update()
        return 
    #this calulates the grads
    current=(((int(currentGrade))/100)*80)
    final=(int(finalGrade))
    examGrade=(((final)-current)/20 ) *100  
    finalExamGrade=round(examGrade, 2)              #this rounds the number             https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python#:~:text=Just%20use%20the%20formatting%20with,rounding%20down%20to%202%20decimals.&text=You%20can%20use%20the%20round%20function.&text=You%20can%20use%20the%20string%20formatting%20operator%20of%20python%20%22%25%22.
    #print(current,final,finalExamGrade)
    #This will put the number into the entry
    finalExamEntry.delete(0,END)                    
    finalExamEntry.insert(END,finalExamGrade)
    finalExamEntry.update()

    






currentGradeLBL=Label(frameEntry, text="Enter Your Current Grade: ",
                    compound="center",          #move the graphics to where you say it will go
                    font=("Times New Roman",14),    #what type of font and size
                    bd=3,                           #border for the label
                    relief=FLAT,                 #the 3d background button
                    fg="mediumpurple3",             # foreground color
                    bg="black")                     #background color
currentGradeLBL.pack(side=LEFT)




currentGradeEntry= Entry(frameEntry,font=("comic sans", 14))
currentGradeEntry.pack(side=LEFT,pady=5)


gradeYouWantLBL=Label(frameEntry, text="Enter the Grade You Want(percentage): ",
                    compound="center",          #move the graphics to where you say it will go
                    font=("Times New Roman",14),    #what type of font and size
                    bd=3,                           #border for the label
                    relief=FLAT,                 #the 3d background button
                    fg="mediumpurple3",             # foreground color
                    bg="black")                     #background color
gradeYouWantLBL.pack(side=LEFT)




gradeYouWantEntry= Entry(frameEntry,font=("comic sans", 14))
gradeYouWantEntry.pack(side=LEFT,pady=5)



CalculateBTN= Button(frameEntry,text="Calculate",command=calculate,background="blue")
CalculateBTN.pack(side=BOTTOM,pady=5)


frameGrade= Frame(groot,pady=10,bg="black")
frameGrade.pack()

finalExamLBL=Label(frameGrade, text="The Grade You Need On the Final : ",
                    compound="center",          #move the graphics to where you say it will go
                    font=("Times New Roman",14),    #what type of font and size
                    bd=3,                           #border for the label
                    relief=FLAT,                 #the 3d background button
                    fg="mediumpurple3",             # foreground color
                    bg="black")                     #background color
finalExamLBL.pack(side=TOP)

finalExamEntry= Entry(frameGrade,font=("comic sans", 14))
finalExamEntry.pack(side=TOP,pady=5)




groot.mainloop()