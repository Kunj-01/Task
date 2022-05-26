list1 = ['a','b','a','c','d','e','f','a','b','c','d']

dict1 = dict()
for i in list1:
	if(dict1.get(i)==None):
		dict1[i] = 1
	else:
		dict1[i] += 1
print(dict1)