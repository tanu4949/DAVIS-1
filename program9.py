#list creation
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
