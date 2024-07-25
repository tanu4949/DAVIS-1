#using tabulate
pip install tabulate

from tabulate import tabulate
# Using DICTIONARY
# Data of the Student from Excel
data = [
    {"stdid": "std101", "stdname": "Ashish Kumar", "standard": "10th", "Age": 15, "Hindi": 67, "English": 89, "Maths": 87, "Science": 89, "Computer": 90, "Total": 422},
    {"stdid": "std102", "stdname": "Abhishek Kumar", "standard": "10th", "Age": 15, "Hindi": 34, "English": 45, "Maths": 78, "Science": 45, "Computer": 31, "Total": 233},
    {"stdid": "std103", "stdname": "Aman", "standard": "10th", "Age": 15, "Hindi": 56, "English": 56, "Maths": 78, "Science": 78, "Computer": 45, "Total": 313},
    {"stdid": "std104", "stdname": "Rahul", "standard": "10th", "Age": 15, "Hindi": 78, "English": 67, "Maths": 89, "Science": 89, "Computer": 78, "Total": 402},
    {"stdid": "std105", "stdname": "Ruby", "standard": "10th", "Age": 13, "Hindi": 89, "English": 56, "Maths": 45, "Science": 45, "Computer": 67, "Total": 302},
    {"stdid": "std106", "stdname": "Suman", "standard": "10th", "Age": 13, "Hindi": 67, "English": 67, "Maths": 67, "Science": 67, "Computer": 67, "Total": 335},
    {"stdid": "std107", "stdname": "Saurabh", "standard": "10th", "Age": 15, "Hindi": 45, "English": 23, "Maths": 45, "Science": 78, "Computer": 67, "Total": 258},
    {"stdid": "std108", "stdname": "Sumit", "standard": "10th", "Age": 15, "Hindi": 89, "English": 90, "Maths": 89, "Science": 90, "Computer": 45, "Total": 403},
    {"stdid": "std109", "stdname": "Kamlesh", "standard": "10th", "Age": 15, "Hindi": 78, "English": 45, "Maths": 78, "Science": 78, "Computer": 78, "Total": 337},
    {"stdid": "std110", "stdname": "Rohan", "standard": "10th", "Age": 15, "Hindi": 12, "English": 24, "Maths": 45, "Science": 56, "Computer": 34, "Total": 171}
]
# To print the data in tabular form
print(tabulate(data, headers="keys", tablefmt="grid"))
# Initialize an empty list to store names of students
filtered_students = []
# To check if the student's English marks is greater than 50
for student in data:
    if student["English"] > 50:
        filtered_students.append(student["stdname"])
# Print the names of students
print("Students whose marks in English are greater than 50:")
for name in filtered_students:
    print(name)

print("------------------*------------------*-----------------*------------------")
print("Name and Age of a student who are top four scorer in Maths:")
# Sort data based on Maths scores in descending order
sorted_data = sorted(data, key=lambda x: x["Maths"], reverse=True)
top_four = sorted_data[0:4]
# Prepare table data that contain the name and age of top four scorer of Maths
table_data = [[student["stdname"], student["Age"]] for student in top_four]
# Display the table_data in tabular form
print(tabulate(table_data, headers=["Student Name", "Age"], tablefmt="grid"))

print("------------------*------------------*-----------------*------------------")
print("Name, Id and Age of student who are bottom three scorer in Computer:")
# Sort data based on Computer scores in ascending order
sorted_data = sorted(data, key=lambda x: x["Computer"])
bottom_three = sorted_data[:3]

#Prepare table data that contain the Name ,Id and Age of bottom three scorer in Computer
table_data = [[student["stdname"], student["stdid"], student["Age"]] for student in bottom_three]
# Display the table_data in tabular form
print(tabulate(table_data, headers=["Student Name", "Student ID", "Age"], tablefmt="grid"))
