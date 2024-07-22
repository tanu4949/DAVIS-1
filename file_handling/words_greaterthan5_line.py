#Python program that reads a file and displays lines that contain more than 5 words:

s=open("note.txt", 'r') 
lines = s.readlines() 
# Iterate through each line
count=0
for line in lines:
    words = line.split()
    if len(words) > 5:
        count=count+1
        # Display the line
        print(line.strip())
print("lines having more than 5 words:",count)
