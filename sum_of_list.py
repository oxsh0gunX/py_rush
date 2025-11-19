# sum_of_list_items.py
num_range=int(input("Enter the range of the number here: "))
list_of_num=[]
sum=0
print("Enter the values to list")
for value in range(num_range):
    nums=int(input())
    list_of_num.append(nums)

for numbers in list_of_num:
    sum+=numbers

print(f"The sum of the list of the number is :{sum}")
