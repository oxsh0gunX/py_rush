#swap 1 and last in the 
#str is better for this ops 
string=input("Enter the string Text here: ")
str_1st=string[0]
str_last=string[-1]
str_mid=string[1:-1]
print( str_last + str_mid + str_last)
