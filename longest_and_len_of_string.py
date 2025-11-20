string=input("Enter the string suprated by comma: ").split(',')
longest=max(string, key=len)
print(f"The longest string is {longest} ")
print("The length of the string is ",len(longest))
