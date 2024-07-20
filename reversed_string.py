#Python program to reverse words in a string

## initializing the string
string = "Deeptech Python Training"
print("the string is",string)
## splitting the string on space
words = string.split()
## reversing the words using reversed() function
words = list(reversed(words))
## joining the words and printing
a=(" ".join(words))
print("the reversed string is",a)
