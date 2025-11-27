#square
#datatime
#radnom number
import math
import datetime
import random

number=int(input("Enter the number here: "))
start=int(input("Enter the range for random guss starting and ending"))
end=int(input())

sqrt_of_num=math.sqrt(number)
random_num=random.randint(start,end)
current_date=datetime.datetime.now() 

print(f"the square of the {number} is {sqrt_of_num}")
print(f"Random number between {start} and {end} is {random_num} ")
print(f"The current date is {current_date}")
