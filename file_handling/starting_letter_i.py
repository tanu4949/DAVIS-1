#Python program that reads a file, counts and displays words that start with the letter 'i'

s=open("anudip.txt","r")
text = s.read()
words = text.split()
            
# Count words starting with 'i'
count = 0
for word in words:
    if word.startswith('i') or word.startswith('I'):
        count += 1
print(f"Number of words starting with 'i': {count}")
    
    
