# python program for list creation
firstlist=[20,90,30,50,70]
print("the list is",firstlist)
print("------------------------------------------------------------")
#appending in list
x=int(input("enter any number to insert into the list"))
firstlist.append(x)
print("after appending",x,"list is",firstlist)
print("------------------------------------------------------------")
#appending another list in firstlist(put list as one as another type in existing list)
secondlist=[40,70,56,78]
print("second list is",secondlist)
firstlist.append(secondlist)
print("after inserting second list",firstlist)
print("------------------------------------------------------------")
#using extend function on the list(clarify each element in list as  single)
thirdlist=[65,130,195]
print("third list is",thirdlist)
firstlist.extend(thirdlist)
print("after extending thirdlist",firstlist)
print("------------------------------------------------------------")
#to insert element at a particular position(using insert function)(index,element)
firstlist.insert(4,147)
print("after inserting 147 at 5th position in firstlist",firstlist)
print("------------------------------------------------------------")






#python program for deletion operations in list

print("The list is")
firstlist=[20,90,30,50,70]
print(*firstlist)
print("---------------------------------------------------------")
#to delete data from a last position using POP function
print("delete data from a last position from list")
firstlist.pop()
print("after poping list is",firstlist)
print("---------------------------------------------------------")
#to delete data from a particular position(index)
print("delete data from 3rd position")
firstlist.pop(2)
print("after poping 3rd element of list is",firstlist)
print("---------------------------------------------------------")
#to delete data from list using REMOVE function (it does not uses index but the exact number)
print("delete dataitem 50 from list")
firstlist.remove(50)
print("after removing 50 from list is",firstlist)
print("---------------------------------------------------------")
#to delete the complete list using CLEAR function but list  structure will be there
print("delete the complete list ")
firstlist.clear()
print("after clearing all the element of list is",firstlist)
print("---------------------------------------------------------")


#python program for traversing in list
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
