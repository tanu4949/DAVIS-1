#Python program that reads a file and displays the occurrences of the word "india" in the file:

s=open("india.txt", 'r') 
text = s.read().lower()# Read the entire file and convert to lowercase
word="india"
count = text.count(word.lower())  # Count occurrences of the word (case insensitive)
print("occurrence of word india",count)
    

