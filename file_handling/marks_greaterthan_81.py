#read a binary file in python and display students whose marks are greater than 81

import pickle
s=open("stu.dat", 'rb') 
records = pickle.load(s)
print("Student records with marks greater than 81:")
for record in records:
    if record['marks'] > 81:
        print(f"Roll No: {record['roll_no']}, Name: {record['name']}, Marks: {record['marks']}")
    
