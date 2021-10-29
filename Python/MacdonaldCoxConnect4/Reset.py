class Reset:

    def __init__(self,player1):
        self.player1Mark=player1
        self.xy=True
        while (self.xy):                 #CAN PROBABLY MAKE THIS THE CLASS*************
            if (self.player1Mark =="X" or  self.player1Mark =="O"):
                self.xy=False
            else:
                self.xy=True
                self.player1Mark=input("that was not a choice\nWhat would you like to be... X or O? ").upper() 
                
                

    def __str__(self):
        if self.xy==False:
            return (self.player1Mark.upper())