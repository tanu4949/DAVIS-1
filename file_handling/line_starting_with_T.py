#Python program that reads a file, counts the lines starting with the letter 'T'

s=open("story.txt", 'r')
lines = s.readlines()
count = 0
            
# Iterate through each line
for line in lines:
    if line.strip().startswith('T') or line.strip().startswith('t'):
        count += 1
        print(line.strip())  # Display the line
            
print(f"Number of lines starting with 'T' or 't': {count}")
    
