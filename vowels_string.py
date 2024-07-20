#Python program to count and display the vowels of a given text

input_string ="Welcome to python Training"
print("the input text is",input_string)
count = 0
String = input_string.lower()
for vowel in String:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' :
        count+=1
if count == 0:
    print('No vowels found')
else:
    print('Total numbers of vowels in text are :' + str(count))
