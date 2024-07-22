#python program for CSV files

import csv
f=open("list.dav",'a',newline='')
wo=csv.writer(f)
data=[["a","b","c","d"],[16,14,10,12],[26,20,89,67],[76,23,45,65]]
wo.writerows(data)
f.close()



f=open("list.dav","r")
re=csv.reader(f)
li=list(re)
for row in li:
    print(row)
f.close()
