#replcae the 1st char whitht the $ after the 1at
string=input("Enter the string here: ")
str_first=string[0]
str_temp=str_first
for ch in string[1:]:
    if ch == str_first:
        str_temp+="$"
    else:
        str_temp+=ch
print(str_temp)
