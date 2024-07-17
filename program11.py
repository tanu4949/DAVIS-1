#creating list
list1=[3,6,8,12,45,90,67,32]
print(list1)
#print list without formatting
print(*list1)
#traversing the list using for loop
for x in list1:
    print(x,end=",")
#-----------------------
#fetching the 3rd member
print(list[2])
#--------------------
#fetching the list of 20 items in backward order by using forward indexing
list2=[3,6,8,12,45,90,67,32,1,2,3,4,5,6,7,8,9,10,11,12]
i=len(list2)-1
for i in range(i,-1,-1):
    print(list2[i],end=",")
