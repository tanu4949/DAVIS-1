#binary file in python and take roll no, marks, name as much the user want 
import pickle
s=open("stu.dat", 'wb')
records = []
while True:
    roll_no = input("Enter roll number (or type 'exit' to stop): ")
    if roll_no.lower() == 'exit':
        break
while True:
    marks = (input("Enter marks(or type 'exit' to stop): "))
    if marks.lower() == 'exit':
        break
while True:
    name = input("Enter name(or type 'exit' to stop): ")
    if name.lower() == 'exit':
        break
    
                
                
record = {'roll_no':roll_no,'marks': marks,'name': name}
records.append(record)
print("Record added successfully.")
            
#write records to the file using pickle
pickle.dump(records, s)
s.close
            

    
    
