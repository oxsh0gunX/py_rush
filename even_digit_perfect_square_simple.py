start=int(input("Enter the startig poing of the number"))
end=int(input("Enter the ending poing of the number"))
# for to str to check exact 4 next check even find root root=num** 0.5 if root *root == for loop itration then store to the list that is it
result=[]
for number in range(start,end+1):
    number_string=str(number)
    if len(number_string) == 4:
        if (number_string[0] in '02468' and number_string[1] in '02468' and number_string[2] in '02468' and number_string[3] in '02468'):
            root=int(number ** 0.5)
            if (root * root == number):
                result.append(number)
print(result)
