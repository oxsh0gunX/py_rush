class bank:
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
    
    def deposite(self,depo):
        self.amount+=depo
        print(f"{depo} is sussesfully deposited ")
        print("Current balance is : ",self.amount)

    
    def withdrow(self,widr):
        if self.amount > widr:
            self.amount-=widr
            print("Balnce after withdrow is ",self.amount)
        else:
            print("failed")
name=input("Enther the name : ")
amount=float(input("Enter the amount"))
my=bank(name,amount)

selector=int(input(("Select Option :\n 1)deposite \n2)widrow \n 3)exit ")))

while True:
    if selector ==1:
        depos=float(input("Enter the amount to deposite: "))
        my.deposite(depos)
    elif selector ==2:
        amtn=float(input("Enter the amount to widrow: "))
        my.withdrow(amtn)
    elif selector == 3:
        break 
    else:
        print("invalid choice")
    
