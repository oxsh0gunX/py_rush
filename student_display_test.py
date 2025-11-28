#name rollno mark py
class student:
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no
    def print(self):
        print(f"your name is {self.name} ,your age is {self.age}and your roll number is {self.roll_no}")
        
class_call=student("safvan",21,23)
class_call.print()
