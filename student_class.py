class student:
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no
        
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"ROll Number:{self.roll_no}")
        
num_range=int(input("Enter the range here : "))
result=[]

for x in range(num_range):
    name=input("Enter the name: ")
    age=int(input("Enter the age: "))
    roll_no=int(input("Enter the Roll Number: "))
    
    my_class=student(name,age,roll_no)
    
    s=(name,age,roll_no)
    result.append(s)
# print(result)

for y in result:
    my_class.display()
    
