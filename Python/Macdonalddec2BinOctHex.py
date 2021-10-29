from tkinter import *              #the * = wildcord or when you import, it is everything
import tkinter.scrolledtext as tksc


#checkList=[]

groot = Tk()

def command():
    global numberEntry
    answerTextbox.insert(END,"1")           #if the textbox doesn't have anything in it it will add something so that every time the button is clicked it can delete what's in it
    answerTextbox.delete(1.0,END)           #this will delete what is in the textbox
    answerTextbox.update()
    

 
    while "." in (numberEntry.get()):                       #this will make sure there are no decimals in the entry
        numberEntry.delete(0,END)
        numberEntry.insert(END,"No Decimals")
        numberEntry.update()

    globalNumber=int(numberEntry.get())
    number=globalNumber

    #print("This is number",number)

    binCheckList=[]
    i=0
    while int(number)>=2**i:
        #insert will allow you to put where you want(location,value)
        binCheckList.insert(0,2**i)
        i+=1
    #print(bin(decimal))

#this loop calculates the bin string
    for i in range(len(binCheckList)):
        #if the 2**checklist[i] is less than or equal to our integer
        if int(number) >= binCheckList[i]:
            number-=binCheckList[i]
            binCheckList[i]="1"
            
        else:
            binCheckList[i]="0"
    out=""
    for b in binCheckList:
        out+=b
    #print ("This is the bin: ",out)
    answerTextbox.insert(END,"This is the bin: "+out)
    answerTextbox.update()


    number=globalNumber
    #print("This is number",number)
    octCheckList=[]
    binList=["000",'001','010','011','100','101','110','111']
    octList=['0',"1",'2','3','4','5','6','7']
    i=0
    while number>=2**i:
        #insert will allow you to put where you want(location,value)
        octCheckList.insert(0,2**i)
        i+=1
    #print(bin(decimal))
    #print(checkList)


#this loop calculates the bin string
    for i in range(len(octCheckList)):
        #if the 2**checklist[i] is less than or equal to our integer
        if number >= octCheckList[i]:
            number-=octCheckList[i]
            octCheckList[i]="1"
            
        else:
            octCheckList[i]="0"
    length=len(octCheckList)

    if length%3==1:
        octCheckList.insert(0,"0")
        octCheckList.insert(0,"0")
    elif length%3==2:
        octCheckList.insert(0,"0")

    out=""
    for b in octCheckList:
        out+=b
    #print (out)

    length=len(octCheckList)
    #print(length)
    octL=""
    ran=length/3
    for i in range(int(ran)):
        
        new=(octCheckList[0]+octCheckList[1]+octCheckList[2])
        #print(new)
        #print(octCheckList)
        for i in range(3):
            octCheckList.pop(0)
        for i in range (len(binList)):
            if binList[i]==new:
                #print(binList[i])
                #print(new)
                octL+=octList[i]

    #print("This is the oct: ",octL)
    answerTextbox.insert(END,"\nThis is oct: "+octL)
    answerTextbox.update()

    number=globalNumber
    #print("This is number",number)
    hexCheckList=[]
    i=0
    while number>=16**i:
        #insert will allow you to put where you want(location,value)
        hexCheckList.insert(0,16**i)
        i+=1
    #print(bin(decimal))
    #print(hexCheckList)

    #this loop calculates the bin string
    for i in range(len(hexCheckList)):
        #if the 2**checklist[i] is less than or equal to our integer
        if number >= hexCheckList[i]:
            check=hexCheckList[i]
            hexCheckList[i]=int(number/hexCheckList[i])
            number=int(number%check)
            #print(hexCheckList[i])
            #print(decimal)

        if hexCheckList[i]>=10:
            hexCheckList[i]+=55
            hexCheckList[i]=chr(hexCheckList[i])
    out=""
    for b in hexCheckList:
        out+=str(b)
    #print ("This is the hex: ",out)
    answerTextbox.insert(END,"\nThis is the hex: "+out)
    answerTextbox.update()




frameURL= Frame(groot,pady=10,bg="black")
frameURL.pack()

numberEntry= Entry(frameURL,font=("comic sans", 14))
numberEntry.pack(side=LEFT)

CalculateBTN= Button(frameURL,text="Calculate",command=command,background="blue")
CalculateBTN.pack(side=LEFT)

#scorlledText widget for the command output
answerTextbox=tksc.ScrolledText(frameURL, height=10,width=100) 
answerTextbox.pack(padx=10)

groot.mainloop()