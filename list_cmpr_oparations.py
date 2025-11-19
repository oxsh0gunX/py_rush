list1=[]
list2=[]
range_1=int(input("enter the range of the list one "))
range_2=int(input("enter the range of the list two"))

print("enter the elemets for the list one here:")
for ls_1 in range(range_1):
    list1.append(int(input()))
    
print("Ent the elements for list two here:")
for ls_2 in range(range_2):
    list2.append(int(input()))

same_len= ( ( len(list1)) == len(list2) )
same_sum= ( sum(list1) == sum(list2) )
commn_val=set(list1).intersection(list2)
print(f"The same len{same_len}")
print(f"same sum {same_sum}")
print(f"commn value {commn_val}")



