#program to count the occurrences of each word in a given sentence
str = "To change the overall look your document. To change the look available in the gallery"
c={}
txt = str.split(" ")
for t in txt:
	if t in c:
		c[t] += 1
	else:
		c[t] = 1
print(c)
