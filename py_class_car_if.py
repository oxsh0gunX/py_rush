class car:
    def __init__(self,model,brand,year):
        self.model=model
        self.brand=brand
        self.year=year
    def show_detials(self):
        print("Model:",self.model)
        print("Brand",self.brand)
        print("year",self.year)
    def Is_new(self):
        if self.year >= 2023:
            print(f"{self.model} is new car ")
        else:
            print(f"{self.model} is not new car ")
            
    def display(self):
        self.show_detials()
        self.Is_new()
        
my_class=car("dfdf","dfd",2020)
my_class.display()
        
        
