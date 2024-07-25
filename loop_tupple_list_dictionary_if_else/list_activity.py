#python program for displaying the list elements in tabular form and performing queries

from tabulate import tabulate
data = [
     ["std101", "Ashish Kumar", "10th", 15, 67, 89, 87, 89, 90, 422],
     ["std102", "Abhishek Kumar", "10th", 15, 34, 54, 78, 45, 31, 233],
     ["std103", "Aman", "10th", 15, 56, 56, 78, 78, 45, 313],
     ["std104", "Rahul", "10th", 15, 78, 67, 89, 89, 78, 402],
           ["std105", "Ruby", "10th", 13, 89, 56, 45, 45, 67, 302],
            ["std106", "Suman", "10th", 13, 67, 67, 67, 67, 67, 335],
             ["std107", "Saurabh", "10th", 15, 45, 23, 45, 78, 67, 258],
              ["std108", "Sumit", "10th", 15, 89, 90, 89, 90, 45, 403],
               ["std109", "Kamlesh", "10th", 15, 78, 45, 78, 78, 78, 337],
                ["std110", "Rohan", "10th", 15, 12, 24, 45, 56, 34, 171] ]
headers = ["stdid", "stdname", "standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]
print(tabulate(data, headers=headers, tablefmt="grid"))

print("-----------------print whose marks >50 in english-----------------")
for row in data:
      if row[5]>50:
        print(row[1])
print()

print("------------name and age of top4 scorers of maths------------")
score=sorted(data,key=lambda row:row[6],reverse=True)
print('name','age')
print(score[0][1],score[0][3])
print(score[1][1],score[0][3])
print(score[2][1], score[0][3])
print(score[3][1], score[0][3])
print()
