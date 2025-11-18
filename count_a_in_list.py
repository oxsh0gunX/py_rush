num_of_name=int(input("How many name you want to enter"))
names=[]
for name in range(num_of_name):
    Name=input("Enter the name here: ")
    names.append(Name)
count=0
for temp in names:
    count+=temp.count('a')

print(f"The number of the  a in the name is {count}")