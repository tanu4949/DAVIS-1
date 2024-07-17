Dict = {'name': 'ritu','standard':12, 'percentage': 80}
print("the dictionary is",Dict)
print("only keys are:-")
for i in Dict:
    print(i)
print("--------------------------------------------------------")

print("printing values of dictionary one by one")
for i in Dict:
    print(Dict[i])

print("--------------------------------------------------------")
#updating value of a key in dictionary
Dict['percentage']=82
print("after updating the value of percentage")
print(Dict)

#updating the dictionary by adding dict2 to dict1
print("the first dictionary is",Dict)
Dict2={'hindi':67,'age':18,'english':78,'name':'fanny'}
print("the second dictionary is",Dict2)
Dict.update(Dict2)
print("the updated dictionary is",Dict)
print("--------------------------------------------------------")
#adding new key-value pair
print("after adding new key to the dictionary")
Dict.update({'fees':'given'})
print(Dict)
print("--------------------------------------------------------")
#printing all the keys using function keys()
print("printing all the keys")
print(Dict.keys())

print("--------------------------------------------------------")
#printing all the values using function values()
print("printing all the values")
print(Dict.values())

print("--------------------------------------------------------")
#pop works on index
print("deleting key-> standard from dictionary")
Dict.pop("standard")
print("after deleting:-",Dict)

print("--------------------------------------------------------")
print("deleting last key-value pair")
#popitem works on key value pair
Dict.popitem()
print(Dict)

print("--------------------------------------------------------")
#returning list of items(each item will be in form of tuple with two member that is key-value) using items() function
print("returning dictionary in couple of tuple under list")
print(Dict.items())

print("--------------------------------------------------------")
#other functions are copy(),clear(),get()
#using the get function to get the values
print("using the using the get function to get the values")
print(Dict.get('standard','element dont exist'))

#providing universal values to the keys by using fromkeys(key,value) function
print("after using fromkeys() function")
print(Dict.fromkeys('name','stuti'))
