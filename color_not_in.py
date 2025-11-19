# color not in second list
color_range_1=int(input("Enter the rang of the list 1"))
color_range_2=int(input("Enter the range of the list  2"))
color1=[]
color2=[]
result=[]
print("Enter the colors for the list 1:")
for x in range(color_range_1):
    val_color_1=input()
    color1.append(val_color_1)

print("Enter the colors for the list 2: ")
for y in range(color_range_2):
    val_color_2=input()
    color2.append(val_color_2)

for colors_1 in color1:
    if colors_1 not in color2:
        result.append(colors_1)

for colors_2 in color2:
    if colors_2 not in color1:
        result.append(colors_2)
print(result)
    
