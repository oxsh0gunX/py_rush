# Bank
# deposit(amount)

# withdraw(amount)

# show_balance()
# name amout accno

class Bank:
    def __init__(self,name,amount,accno):
        self.name=name
        self.amount=amount
        self.accno=accno
        
        
    def deposot(self,deposite):
        self.amount=self.amount+deposite

    def withdraw(self,widrwo):
        if self.amount < widrwo :
            print("insufficent balance")
    def show_amount(self):
        print("Account holder name is : ",self.name)
        
    
        
my_class=Bank("safvan",400,1234)
my_class.deposot(500)
my_class.deposot(400)
my_class.withdraw(3444)
my_class.show_amount()
