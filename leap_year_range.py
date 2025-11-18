start=int(input("enter the start and the end of the year"))
end=int(input())
for year in range(start,end):
    if year % 4 == 0:
        print(year)
    elif year % 100 == 0:
        continue
    elif year % 400 ==0:
        print(year)