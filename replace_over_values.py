rang=int(input("enter the range "))
result=[]
for  i in range (rang+1):
    num=int(input("enter the numbers"))

    if num > 100:
        result.append("over")
    else:
        result.append(num)
print(result)